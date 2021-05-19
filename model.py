from typing import Dict
from PySide2.QtCore import Signal, Slot, QObject, QTimer
import cv2, h5py, math
import numpy as np
import matplotlib.pyplot as plt

# deep sort imports
from deep_sort import preprocessing, nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker

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

MAX_DETECTION_NUM = 50
nn_budget = None
nms_max_overlap = 1.0
input_size = 416

model_filename = 'model_data/mars-small128.pb'
weights_path = './checkpoints/yolov4-416'

class_id_map = {
    'none'  : '0',
    'truck' : '1',
    'car'   : '2',
    'bus'   : '3'
}
class_id_map.update({item[1]: item[0] for item in class_id_map.items()})

class Model(QObject):
    frame_update_signal = Signal(np.ndarray, int)
    max_frame_update_signal = Signal(int)
    process_done_signal = Signal()
    error_signal = Signal(str)
    vehicle_count_signal = Signal(int,int,int,np.ndarray)

    def __init__(self):
        super().__init__()
        # Definition of the parameters
        self.sess = None
        self.infer = None
        self.encoder = None
        self.saved_model_loaded = None
        self.max_cosine_distance = 0.4
        self.iou_thresh = 0.45
        self.score_thresh = 0.7
        self.input_video_path = ''
        self.output_video_path = ''
        self.output_data_path = ''
        self.cache_data = None
        self.vid = None
        self.detected_vehicles = None
        self.frame_counter = 0
        self.initialize_counting()

        #initialize color map
        cmap = plt.get_cmap('tab20b')
        self.colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]

#======================= Setters  ===========================

    def initialize_counting(self):
        self.detected_vehicles = {class_id : {} for class_name, class_id in class_id_map.items()}

    def setInputVideoPath(self, path):
        self.input_video_path = path
        self.vid = cv2.VideoCapture(self.input_video_path)

    def setOutputVideoPath(self, path):
        self.output_video_path = path

    def setOutputDataPath(self, path):
        self.output_data_path = path

    def setCacheDataPath(self, path):
        self.cache_data_path = path

        # parse cache data and send signal with max frame num
        cache = h5py.File(self.cache_data_path, 'r')
        cache_data = cache.get('dataset_1')
        self.cache_data = np.array(cache_data)

        self.max_frame_update_signal.emit(self.cache_data.shape[0])        

    def setParams(self, params:dict):
        self.iou_thresh = params['iou_thresh']
        self.score_thresh = params['score_thresh']
        self.max_cosine_distance = params['cos_dist']
        self.filt_x_vec = params['x_vect']
        self.filt_y_vec = params['y_vect']
        self.filt_width = params['filt_width']
        self.filt_dist = params['filt_dist']
        self.filt_frame = params['filt_frames']

#==================== Counting Functions ========================

    def countVehicles(self, frame, frame_num, detection) -> bool:
        class_id = detection[0]
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
        tracker_dict = self.detected_vehicles[str(class_id)]

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
            return True
        
        # reset distance travelled if previous detected frame is too far off
        elif frame_num - tracker_dict[uid]['prev_frame_num'] > self.filt_frame:
            tracker_dict[uid]['prev_centroid'] = centroid

        # compute distance traveled
        prev_centroid = tracker_dict[uid]['prev_centroid']
        tracker_dict[uid]['dist'] = tracker_dict[uid]['dist'] + math.dist(prev_centroid, centroid)
        tracker_dict[uid]['prev_centroid'] = centroid
        tracker_dict[uid]['prev_frame_num'] = frame_num

        # count the object if distance traveled exceeds a threshold
        if tracker_dict[uid]['dist'] > self.filt_dist:
            # computer direction vector
            initial_centroid = tracker_dict[uid]['initial_centroid']
            vect = [cx - initial_centroid[0], cy - initial_centroid[1]]

            # only count vehicles travelling south
            x_min = self.filt_x_vec - self.filt_width
            x_max = self.filt_x_vec + self.filt_width

            if (x_min < vect[0] < x_max) and (vect[1] > 0) == (self.filt_y_vec > 0):
                tracker_dict[uid]['counted'] = True

                cnt = sum([param['counted'] for id, param in tracker_dict.items()])
                img = self.getVehicleImage(detection, frame)
                self.vehicle_count_signal.emit(class_id, int(uid), cnt, img)
                return True

    @Slot()
    def startCounting(self):
        if not self.validateInputFiles():
            return

        total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # tally total frame num in cahce data and video
        if total_frames != self.cache_data.shape[0]:
            self.error_signal.emit('Video and cache frame count does not match')
            return

        # reinitialize dict for counting
        self.detected_vehicles = {class_id : {} for class_name, class_id in class_id_map.items()}

        # go to first frame
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
        for frame_num, frame_data in enumerate(self.cache_data):
            _, frame = self.vid.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            for detection in frame_data:
                self.countVehicles(frame, frame_num, detection)
                        
        self.process_done_signal.emit()
                
    @Slot()
    def analyzeFrames(self):
        if self.counting_timer.isActive():   
            success , frame = self.vid.read()
            if success:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_data = self.cache_data[self.frame_counter]

                for detection in frame_data:
                    class_name = self.getClassName(str(detection[0]))
                    uid = detection[1]
                    x_min = detection[2]
                    y_min = detection[3]
                    x_max = detection[4]
                    y_max = detection[5]

                    detected = self.countVehicles(frame, self.frame_counter, detection)
                    frame = self.drawBoundingBox(frame, class_name, uid, x_min, y_min, x_max, y_max, detected)

                self.frame_counter += 1
                self.frame_update_signal.emit(frame, self.frame_counter)
            else:
                self.counting_timer.stop()
                self.frame_counter = 0
                self.process_done_signal.emit()
        else:
            self.counting_timer.setInterval(30)
            self.counting_timer.start()
            
    @Slot()
    def startCountingAnalysis(self):
        self.counting_timer = QTimer()
        self.counting_timer.timeout.connect(self.analyzeFrames)
        if not self.validateInputFiles():
            return

        total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # tally total frame num in cahce data and video
        if total_frames != self.cache_data.shape[0]:
            self.error_signal.emit('Video and cache frame count does not match')
            return

        # reinitialize dict for counting
        self.detected_vehicles = {class_id : {} for class_name, class_id in class_id_map.items()}

        # go to first frame
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.analyzeFrames()

    def validateInputFiles(self) -> bool:
        if self.cache_data is None:
            self.error_signal.emit('Cache data not specified!')
            return False
        elif self.vid is None:
            self.error_signal.emit('No input video specified')
            return False
        else:
            return True

    @Slot(int)
    def previewFrame(self, frame_num):
        if not self.validateInputFiles():
            return

        # go to specified frame
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        _, frame = self.vid.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        # draw bb box 
        for detection in self.cache_data[frame_num]:
            class_name = self.getClassName(str(detection[0]))
            uid = detection[1]
            x_min = detection[2]
            y_min = detection[3]
            x_max = detection[4]
            y_max = detection[5]

            frame = self.drawBoundingBox(frame, class_name, uid, x_min, y_min, x_max, y_max)

        # draw counting annotation

        # update frame signal
        self.frame_update_signal.emit(frame, frame_num)

#==================== Inference Functions ========================

    def stopInference(self):
        self.stop_inference = True

    @Slot()
    def startInference(self):
        if not self.validateInputFiles():
            return

        self.stop_inference = False
        self.detected_vehicles = {class_id : {} for class_name, class_id in class_id_map.items()}

        # calculate cosine distance metric
        metric = nn_matching.NearestNeighborDistanceMetric("cosine", self.max_cosine_distance, nn_budget)
        # initialize tracker
        tracker = Tracker(metric)

        # load standard tensorflow saved model for YOLO and Deepsort
        if self.sess is None:
            # load configuration for object detector
            config = ConfigProto()
            config.gpu_options.allow_growth = True
            self.sess = Session(config=config)
            self.saved_model_loaded = tf.saved_model.load(weights_path)
            self.infer = self.saved_model_loaded.signatures['serving_default']
            self.encoder = gdet.create_box_encoder(model_filename, batch_size=1)

        # begin video capture
        total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        self.max_frame_update_signal.emit(total_frames)

        # go to first frame
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)

        # get video ready to save locally 
        # by default VideoCapture returns float instead of int
        width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.vid.get(cv2.CAP_PROP_FPS))
        codec = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.output_video_path, codec, fps, (width, height))

        # initialize buffer to store cache
        cache = []

        # buffer to track and count vehicles
        cars = {}
        trucks = {}
        car_cnt = 0
        truck_cnt = 0

        frame_num = 0
        # while video is running
        while not self.stop_inference:
            frame_data = np.zeros((MAX_DETECTION_NUM, 6), dtype=int)

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
            pred_bbox = self.infer(batch_data)
            for key, value in pred_bbox.items():
                boxes = value[:, :, 0:4]
                pred_conf = value[:, :, 4:]

            boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
                boxes=tf.reshape(boxes, (tf.shape(boxes)[0], -1, 1, 4)),
                scores=tf.reshape(
                    pred_conf, (tf.shape(pred_conf)[0], -1, tf.shape(pred_conf)[-1])),
                max_output_size_per_class=MAX_DETECTION_NUM,
                max_total_size=MAX_DETECTION_NUM,
                iou_threshold= self.iou_thresh,
                score_threshold= self.score_thresh
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
            features = self.encoder(frame, bboxes)
            detections = [Detection(bbox, score, class_name, feature) for bbox, score, class_name, feature in zip(bboxes, scores, names, features)]

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
                
                x_min = int(bbox[0])
                y_min = int(bbox[1])
                x_max = int(bbox[2])
                y_max = int(bbox[3])
                id = int(track.track_id)

                # add to hdf buffer
                class_id = self.getClassId(class_name)
                frame_data[obj_num] = [class_id, id, x_min, y_min, x_max, y_max]

                # Count vehicles
                detected = self.countVehicles(frame, frame_num, frame_data[obj_num])

                # draw bbox on screen
                frame = self.drawBoundingBox(frame, class_name, id, x_min, y_min, x_max, y_max, highlight=detected)
                
                obj_num = obj_num + 1

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

#==================== Helper Functions ========================

    def getVehicleImage(self, detection, frame) -> np.ndarray:
        # xmin, ymin, xmax, ymax
        x_min = detection[2]
        y_min = detection[3]
        x_max = detection[4]
        y_max = detection[5]
        width = x_max - x_min
        height = y_max - y_min

        img = frame[y_min:y_max, x_min:x_max]
        return np.ascontiguousarray(img).copy()

    def getClassId(self, class_name:str) -> int:
        id = class_id_map.get(class_name)
        if id is None:
            id = 0
        return id

    def getClassName(self, class_id:int) -> str:
        name =  class_id_map.get(class_id)
        return name

    def drawBoundingBox(self, frame:np.ndarray, class_name:str, id:int, x_min, y_min, x_max, y_max, highlight=False):
        color = self.colors[id % len(self.colors)]
        color = [i * 255 for i in color]
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)
        cv2.rectangle(frame, (x_min, y_min-30), (x_min+(len(class_name)+len(str(id)) )*17, y_min), color, -1)
        cv2.putText(frame, class_name + "-" + str(id),(x_min, int(y_min-10)),0, 0.75, (255,255,255),2)

        if highlight:
            # highlight in green
            frame = frame.astype(np.float)
            frame[y_min:y_max, x_min:x_max, 0] = 0
            frame[y_min:y_max, x_min:x_max, 2] = 0
            frame = frame.astype(np.uint8)
        return frame