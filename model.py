from typing import Dict
from PySide2.QtCore import Signal, Slot, QObject
import cv2, h5py, math
import numpy as np
import matplotlib.pyplot as plt

# deep sort imports
from deep_sort import preprocessing, nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker

MAX_DETECTION_NUM = 50
max_cosine_distance = 0.4
nn_budget = None
nms_max_overlap = 1.0
iou_thresh = 0.45
score_thresh = 0.7
input_size = 416

class Model(QObject):
    frame_update_signal = Signal(np.ndarray, int)
    max_frame_update_signal = Signal(int)
    process_done_signal = Signal()
    error_signal = Signal(str)
    vehicle_count_signal = Signal(int,int,int,np.ndarray)

    def __init__(self):
        super().__init__()
        # Definition of the parameters
        self.input_video_path = ''
        self.output_video_path = ''
        self.output_data_path = ''
        self.vid = None

    def setInputVideoPath(self, path):
        self.input_video_path = path

    def setOutputVideoPath(self, path):
        self.output_video_path = path

    def setOutputDataPath(self, path):
        self.output_data_path = path

    def setCacheDataPath(self, path):
        self.cache_data_path = path

    def stopInference(self):
        self.stop_inference = True

    def countVehicles(self, frame_num, detection, tracker_dict:dict) -> bool:
        uid = str(detection[1])

        # xmin, ymin, xmax, ymax
        x_min = detection[2]
        y_min = detection[3]
        x_max = detection[4]
        y_max = detection[5]
        width = x_max - x_min
        height = y_max - y_min
        cx = x_min + (width / 2)
        cy = y_min + (height / 2)
        centroid = [cx, cy]
        # detecting for the first time
        if uid not in tracker_dict.keys():
            tracker_dict[uid] = {
                'initial_centroid' : [cx, cy], 
                'prev_centroid': [cx, cy],
                'prev_frame_num': frame_num,
                'dist': 0,
                'counted': False
                }
            return False

        # already counted this car, skip
        elif tracker_dict[uid]['counted'] == True:
            return False
        
        # reset distance travelled if previous detected frame is too far off
        elif frame_num - tracker_dict[uid]['prev_frame_num'] > 10:
            tracker_dict[uid]['prev_centroid'] = centroid

        # compute distance traveled
        prev_centroid = tracker_dict[uid]['prev_centroid']
        tracker_dict[uid]['dist'] = tracker_dict[uid]['dist'] + math.dist(prev_centroid, centroid)
        tracker_dict[uid]['prev_centroid'] = centroid
        tracker_dict[uid]['prev_frame_num'] = frame_num

        # count the object if distance traveled exceeds a threshold
        if tracker_dict[uid]['dist'] > 500:
            # computer direction vector
            initial_centroid = tracker_dict[uid]['initial_centroid']
            vect = [cx - initial_centroid[0], cy - initial_centroid[1]]

            # only count vehicles travelling south
            if (vect[0] < 0) and (vect[1] > 0):
                tracker_dict[uid]['counted'] = True
                return True

    @Slot()
    def startCounting(self):
        self.vid = cv2.VideoCapture(self.input_video_path)
        total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # tally total frame num in cahce data and video
        cache_data = h5py.File(self.cache_data_path, 'r')
        cache = cache_data.get('dataset_1')
        cache = np.array(cache)
        
        if total_frames != cache.shape[0]:
            self.error_signal.emit('Video and cache frame count does not match')
            return

        self.max_frame_update_signal.emit(total_frames)

        cars = {}
        trucks = {}
        car_cnt = 0
        truck_cnt = 0

        for frame_num, frame_data in enumerate(cache):
            _, frame = self.vid.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # self.frame_update_signal.emit(frame, frame_num)

            for detection in frame_data:
                class_id = detection[0]
                uid = detection[1]

                if class_id == 0:
                    continue
                elif class_id == 1:
                    detected = self.countVehicles(frame_num, detection, trucks)
                    if detected:
                        truck_cnt = truck_cnt + 1
                        img = self.getVehicleImage(detection, frame)
                        self.vehicle_count_signal.emit(class_id, uid, truck_cnt, img)
                        
                elif class_id == 2:
                    detected = self.countVehicles(frame_num, detection, cars)
                    if detected:
                        car_cnt = car_cnt + 1
                        img = self.getVehicleImage(detection, frame)
                        self.vehicle_count_signal.emit(class_id, uid, car_cnt, img)
                        
        self.process_done_signal.emit()
                

    def getVehicleImage(self, detection, frame) -> np.ndarray:
        # xmin, ymin, xmax, ymax
        x_min = detection[2]
        y_min = detection[3]
        x_max = detection[4]
        y_max = detection[5]
        width = x_max - x_min
        height = y_max - y_min

        img = frame[y_min:y_max, x_min:x_max]
        return np.ascontiguousarray(img)

    @Slot()
    def startInference(self):
        self.stop_inference = False

        import tensorflow as tf
        physical_devices = tf.config.experimental.list_physical_devices('GPU')
        if len(physical_devices) > 0:
            tf.config.experimental.set_memory_growth(physical_devices[0], True)
        from tensorflow.python.saved_model import tag_constants
        from tensorflow.compat.v1 import ConfigProto
        from tensorflow.compat.v1 import Session
        from core.yolov4 import filter_boxes
        from core.config import cfg
        import core.utils as utils
        from tools import generate_detections as gdet

        # initialize deep sort
        model_filename = 'model_data/mars-small128.pb'
        encoder = gdet.create_box_encoder(model_filename, batch_size=1)
        # calculate cosine distance metric
        metric = nn_matching.NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
        # initialize tracker
        tracker = Tracker(metric)
        print('deepsort')

        # load configuration for object detector
        config = ConfigProto()
        config.gpu_options.allow_growth = True
        session = Session(config=config)

        # load standard tensorflow saved model
        weights_path = './checkpoints/yolov4-416'
        saved_model_loaded = tf.saved_model.load(weights_path)
        infer = saved_model_loaded.signatures['serving_default']

        # begin video capture
        self.vid = cv2.VideoCapture(self.input_video_path)
        total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        self.max_frame_update_signal.emit(total_frames)

        # get video ready to save locally 
        # by default VideoCapture returns float instead of int
        width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.vid.get(cv2.CAP_PROP_FPS))
        codec = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.output_video_path, codec, fps, (width, height))

        # initialize buffer to store cache
        cache = []

        frame_num = 0
        # while video is running
        while not self.stop_inference:
            frame_data = np.zeros((MAX_DETECTION_NUM, 6))

            return_value, frame = self.vid.read()
            if return_value:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                print('Video has ended or failed, try a different video format!')
                break

            image_data = cv2.resize(frame, (input_size, input_size))
            image_data = image_data / 255.
            image_data = image_data[np.newaxis, ...].astype(np.float32)

            batch_data = tf.constant(image_data)
            pred_bbox = infer(batch_data)
            for key, value in pred_bbox.items():
                boxes = value[:, :, 0:4]
                pred_conf = value[:, :, 4:]

            boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
                boxes=tf.reshape(boxes, (tf.shape(boxes)[0], -1, 1, 4)),
                scores=tf.reshape(
                    pred_conf, (tf.shape(pred_conf)[0], -1, tf.shape(pred_conf)[-1])),
                max_output_size_per_class=MAX_DETECTION_NUM,
                max_total_size=MAX_DETECTION_NUM,
                iou_threshold= iou_thresh,
                score_threshold= score_thresh
            )

            # convert data to numpy arrays and slice out unused elements
            num_objects = valid_detections.numpy()[0]
            bboxes = boxes.numpy()[0] # first item, because batch size = 1 
            bboxes = bboxes[0:int(num_objects)]
            scores = scores.numpy()[0]
            scores = scores[0:int(num_objects)]
            classes = classes.numpy()[0]
            classes = classes[0:int(num_objects)]

            # format bounding boxes from normalized ymin, xmin, ymax, xmax ---> xmin, ymin, width, height
            original_h, original_w, _ = frame.shape
            bboxes = utils.format_boxes(bboxes, original_h, original_w)

            # store all predictions in one parameter for simplicity when calling functions
            pred_bbox = [bboxes, scores, classes, num_objects]

            # read in all class names from config
            class_names = utils.read_class_names(cfg.YOLO.CLASSES)
            
            # custom allowed classes (uncomment line below to customize tracker for only people)
            allowed_classes = ['truck', 'car', 'bus']

            # loop through objects and use class index to get class name, allow only classes in allowed_classes list
            names = []
            deleted_indx = []
            for i in range(num_objects):
                class_indx = int(classes[i])
                class_name = class_names[class_indx]
                if class_name not in allowed_classes:
                    deleted_indx.append(i)
                else:
                    names.append(class_name)
            names = np.array(names)
            count = len(names)
            
            # delete detections that are not in allowed_classes
            bboxes = np.delete(bboxes, deleted_indx, axis=0)
            scores = np.delete(scores, deleted_indx, axis=0)

            # encode yolo detections and feed to tracker
            features = encoder(frame, bboxes)
            detections = [Detection(bbox, score, class_name, feature) for bbox, score, class_name, feature in zip(bboxes, scores, names, features)]

            #initialize color map
            cmap = plt.get_cmap('tab20b')
            colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]

            # run non-maxima supression
            boxs = np.array([d.tlwh for d in detections])
            scores = np.array([d.confidence for d in detections])
            classes = np.array([d.class_name for d in detections])
            indices = preprocessing.non_max_suppression(boxs, classes, nms_max_overlap, scores)
            detections = [detections[i] for i in indices]       

            # Call the tracker
            tracker.predict()
            tracker.update(detections)

            obj_num = 0
            # update tracks
            for track in tracker.tracks:
                if not track.is_confirmed() or track.time_since_update > 1:
                    continue 
                bbox = track.to_tlbr()
                class_name = track.get_class()
                
                # add to hdf buffer
                class_id = 0
                if class_name == 'truck':
                    class_id = 1
                elif class_name == 'car':
                    class_id = 2
                frame_data[obj_num] = [class_id, int(track.track_id), int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])]
                obj_num = obj_num + 1

                # draw bbox on screen
                color = colors[int(track.track_id) % len(colors)]
                color = [i * 255 for i in color]
                cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), color, 2)
                cv2.rectangle(frame, (int(bbox[0]), int(bbox[1]-30)), (int(bbox[0])+(len(class_name)+len(str(track.track_id)))*17, int(bbox[1])), color, -1)
                cv2.putText(frame, class_name + "-" + str(track.track_id),(int(bbox[0]), int(bbox[1]-10)),0, 0.75, (255,255,255),2)

            result = np.asarray(frame)
            result = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(result)

            cache.append(frame_data)

            # update frame on UI
            self.frame_update_signal.emit(frame, frame_num)

            print('Frame #: ', frame_num)
            frame_num = frame_num + 1

        # Save cache file as hdf file
        cache_data = h5py.File(self.output_data_path, 'w')
        cache = np.asarray(cache, dtype=int)
        cache_data.create_dataset('dataset_1', data=cache)
        cache_data.close()

        self.process_done_signal.emit()

    def previewFrame(self, frame_num):
        # go to specific frame
        if self.vid is not None:
            self.vid.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            _, frame = self.vid.read()