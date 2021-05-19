
from typing import Tuple
from PySide2.QtCore import QPoint, QUrl, Signal, Slot
from PySide2.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QWidget
from PySide2.QtGui import QImage, QPixmap, Qt, QIcon
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from qt.Ui_Form import Ui_Form
import numpy as np
import cv2, os, math
import pyqtgraph as pg

class ViewController(QWidget, Ui_Form):
    startInferenceSignal = Signal()
    startCountingSignal = Signal()
    startCountingAnalysisSignal = Signal()

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.setupUi(self)
        self.inputVideoFile = ''
        self.outputVideoFile = ''
        self.outputDataFile = ''
        self.cacheDataFile = ''
        self.mediaPlayer = QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.videoFrame)
        self.carPreviewTable.setHorizontalHeaderLabels(['Preview', 'ID'])
        self.truckPreviewTable.setHorizontalHeaderLabels(['Preview', 'ID'])
        self.frameView.ui.histogram.hide()
        self.frameView.ui.roiBtn.hide()
        self.frameView.ui.menuBtn.hide()
        self.frameView.view.setMouseEnabled(False,False)
        
        self.visualizeMarkerStart = QPoint(200,200)
        self.visualizeMarkerEnd = QPoint(500,500)
        self.visualizeMarker = pg.LineROI(self.visualizeMarkerStart, self.visualizeMarkerEnd, 50)
        self.finishLine = pg.RectROI((200,200), (200,200), rotatable=True, resizable=True)
        # self.finishLine.addRotateHandle((0.5,0), (0,0))

        self.setupSignalSlots()
        # development
        
        self.setVideo(os.getcwd() + '/data/video/VehicleTest.mp4')
        self.setCacheData(os.getcwd() + '/data/video/VehicleTest.h5')

    def setupSignalSlots(self):
        self.loadVideoBtn.clicked.connect(self.openVideoFile)
        self.playBtn.clicked.connect(self.toggleVideoState)
        self.mediaPlayer.durationChanged.connect(self.setVideoSliderRange)
        self.mediaPlayer.positionChanged.connect(self.setVideoTime)
        self.videoSlider.valueChanged.connect(self.mediaPlayer.setPosition)

        self.setOutputFileBtn.clicked.connect(self.getOutputFileName)
        self.startInferenceBtn.clicked.connect(self.startInference)
        self.startInferenceSignal.connect(self.model.startInference)
        self.model.frame_update_signal.connect(self.updateFrame)
        self.model.max_frame_update_signal.connect(self.updateMaxFrameNum)
        self.loadCacheBtn.clicked.connect(self.openCacheFile)
        self.countBtn.clicked.connect(self.startCounting)
        self.startCountingSignal.connect(self.model.startCounting)
        self.countAnalyzeBtn.clicked.connect(self.startCountingAnalysis)
        self.startCountingAnalysisSignal.connect(self.model.startCountingAnalysis)
        self.model.vehicle_count_signal.connect(self.updateVehicleCount)
        self.model.process_done_signal.connect(self.onProcessDone)
        self.stopProcessBtn.clicked.connect(self.stopProcess)

        self.frameSlider.valueChanged.connect(self.model.previewFrame)
        self.visualizeChk.toggled.connect(self.visualizeCountingParam)
        self.finishLineChk.toggled.connect(self.showFinishLine)

#====================== File Dialog Functions =====================

    def openVideoFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Video", '', "mp4 (*.mp4)")
        if (file_path != ''):
            self.setVideo(file_path)

    def openCacheFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Cache Data", '', "hdf (*.h5)")
        if (file_path != ''):
            self.setCacheData(file_path)

    def getOutputFileName(self):
        file_path, _ = QFileDialog().getSaveFileName()
        if file_path != '':
            self.setOutputFile(file_path)

#======================= Setting Data sources ========================

    def setVideo(self, file_path):
        self.inputVideoFile = file_path
        self.inputVideoFileLabel.setText(file_path)
        self.model.setInputVideoPath(self.inputVideoFile)

        # content = QMediaContent(QUrl.fromLocalFile(file_path))
        # self.mediaPlayer.setMedia(content)
        # self.mediaPlayer.play()
        # self.mediaPlayer.pause()

        # set the output file name to match as well
        self.setOutputFile(file_path)

    def setOutputFile(self, file_path):
        if '.mp4' in file_path:
            file_path = file_path.replace('.mp4', '')
        self.outputVideoFile = file_path + '.avi'
        self.outputDataFile = file_path + '.h5'
        self.outputFileLabel.setText(file_path)
        self.model.setOutputVideoPath(self.outputVideoFile)
        self.model.setOutputDataPath(self.outputDataFile)

    def setCacheData(self, file_path):
        self.cacheDataFile = file_path
        self.cacheDataLabel.setText(file_path)
        self.model.setCacheDataPath(file_path)

#=================== Video Playback Functions ========================

    def setVideoSliderRange(self, duration):
        self.videoSlider.setMaximum(duration)
        if duration >= 0:
            self.videoMaxTime.setText(self._hhmmss(duration))

    def setVideoTime(self, position):
        if position >= 0:
            self.videoTime.setText(self._hhmmss(position))

        # Disable the events to prevent updating triggering a setPosition event (can cause shuttering).
        self.videoSlider.blockSignals(True)
        self.videoSlider.setValue(position)
        self.videoSlider.blockSignals(False)

    def _hhmmss(self, ms):
        h, r = divmod(ms, 360000)
        m, r = divmod(r, 60000)
        s, _ = divmod(r, 1000)
        return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))

    def toggleVideoState(self):
        if self.mediaPlayer.MediaStatus() != QMediaPlayer.NoMedia:
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                self.mediaPlayer.pause()
            else:
                self.mediaPlayer.play()

#================= Vehicle Counting Functions =========================

    @Slot(bool)
    def showFinishLine(self, checked):
        if checked:
            self.frameView.addItem(self.finishLine)
            # self.finishLine.sigRegionChangeFinished.connect(self.getFinishLineBounds)
        else:
            self.frameView.removeItem(self.finishLine)


    @Slot(bool)
    def visualizeCountingParam(self, checked):
        if checked:
            # add arrow with length defined in distance
            self.frameView.addItem(self.visualizeMarker)
            self.visualizeMarker.sigRegionChangeFinished.connect(self.updateCountingParams)

            # positions = self.visualizeMarker.getSceneHandlePositions()
            # start = positions[0][1]
            # end = positions[1][1]
            # center = start + (end - start)/2
            # cx = center.x()
            # cy = center.y()
            # w = self.widthFilterVectorSpn.value()
            # dx = self.xFilterVectorSpn.value() / 2
            # hypo = self.distFilterSpn.value()/ 2
            # dy = math.sqrt(hypo*hypo - dx*dx)
            # if self.yFilterVectorSpn.value() < 0:
            #     dy = -dy

            # pos_start = QPoint(cx - dx, cy + dy)
            # pos_end = QPoint(cx + dx, cy - dy )

        else:
            self.frameView.view.removeItem(self.visualizeMarker)


    def getMarkerPos(self) -> Tuple[QPoint, QPoint]:
        positions = self.visualizeMarker.getSceneHandlePositions()
        start = positions[0][1]
        end = positions[1][1]

        # convert to image coordinate system
        start = self.frameView.getView().mapSceneToView(start)
        start = self.frameView.getView().mapFromViewToItem(self.frameView.imageItem, start)
        end = self.frameView.getView().mapSceneToView(end)
        end = self.frameView.getView().mapFromViewToItem(self.frameView.imageItem, end)
        return start, end

    def updateCountingParams(self):
        width = self.visualizeMarker.size()[1]
        start, end = self.getMarkerPos()

        # calculate filter distance from line length
        dist = math.dist([start.x(), start.y()], [end.x(), end.y()])

        # calculate x & y filter values from line vector
        dx = (end - start).x()
        dy = (end - start).y()

        self.distFilterSpn.setValue(dist)
        self.xFilterVectorSpn.setValue(dx)
        self.yFilterVectorSpn.setValue(dy)
        self.widthFilterVectorSpn.setValue(width)

    def startCounting(self):
        if self.cacheDataFile != '':
            self.prepareforAnalysis()
            self.startCountingSignal.emit()
        else:
            QMessageBox.warning(self, 'Error', 'No cache file selected!')

    def startCountingAnalysis(self):
        if self.cacheDataFile != '':
            self.prepareforAnalysis()
            self.startCountingAnalysisSignal.emit()
        else:
            QMessageBox.warning(self, 'Error', 'No cache file selected!')


    @Slot(int,int,int,np.ndarray)
    def updateVehicleCount(self, class_id, uid, count, img):
        if class_id == 1:
            self.truckCount.display(count)
            table = self.truckPreviewTable
        elif class_id == 2:
            self.carCount.display(count)
            table = self.carPreviewTable
        elif class_id == 3:
            self.busCount.display(count)
            table = self.busPreviewTable
        else:
            return

        item = QTableWidgetItem()
        pixmap = self.convert_cv_qt(img, 100, 100)
        item.setData(Qt.DecorationRole, pixmap)
        table.setItem(count-1,0,item)
        item = QTableWidgetItem(str(uid))
        table.setItem(count-1,1,item)

#================== Inference Functions ======================

    def startInference(self):
        self.prepareforAnalysis()
        self.startInferenceSignal.emit()
    
    def stopProcess(self):
        self.model.stopInference()
        self.model.stopCountingAnalysis()
        self.enableControls(True)

#=================== Helper Functions =========================

    def prepareforAnalysis(self):
        # set parameters
        self.model.setParams(
            {
                'count_method'  : self.countMethodCmb.currentIndex(),
                'iou_thresh'    : self.iouThreshSpn.value(),
                'score_thresh'  : self.scoreThreshSpn.value(),
                'cos_dist'      : self.cosineDistSpn.value(),
                'x_vect'        : self.xFilterVectorSpn.value(),
                'y_vect'        : self.yFilterVectorSpn.value(),
                'filt_width'    : self.widthFilterVectorSpn.value(),
                'filt_dist'     : self.distFilterSpn.value(),
                'filt_frames'   : self.skipFrameFilterSpn.value(),
                'finish_line'   : self.getFinishLineBounds(),
            }
        )

        # change video display to frames updated by Qlabel
        self.videoSwitcher.setCurrentIndex(1)

        # clear the preview table
        self.carPreviewTable.clear()
        self.truckPreviewTable.clear()

        self.enableControls(False)

    def getFinishLineBounds(self):
        pos = self.finishLine.viewPos()
        if pos is None:
            return [0,0,0,0]
            
        size = self.finishLine.size()

        return [int(pos.x()), int(pos.y()), int(size.x()), int(size.y())]

        # print('start vis: ' + str(size.x()) + ',' + str(size.y()))
        # print('###########################')

    def enableControls(self, state=True):
        self.mediaGBox.setEnabled(state)
        self.inferenceGBox.setEnabled(state)
        self.countingGBox.setEnabled(state)
        self.frameSlider.setEnabled(state)
        self.stopProcessBtn.setEnabled(not state)

    def onProcessDone(self):
        self.enableControls(True)

    @Slot(int)
    def updateMaxFrameNum(self, frame_num):
        self.maxFrameNum.setText(str(frame_num))
        self.frameSlider.setMaximum(frame_num)

    @Slot(np.ndarray, int)
    def updateFrame(self, cv_img, frame_num):
        # """Updates the image_label with a new opencv image"""
        # qt_img = self.convert_cv_qt(cv_img, self.frameLabel.width(), self.frameLabel.height())
        # self.frameLabel.setPixmap(qt_img)
        self.frameView.setImage(cv_img)
        # self.frameView.view.setAspectLocked(False)
        self.frameView.view.setXRange(0, cv_img.shape[1])
        self.frameView.view.setYRange(0, cv_img.shape[0])
        self.frameNum.setText(str(frame_num))
    
    def convert_cv_qt(self, rgb_image, width, height):
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(width, height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)