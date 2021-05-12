
from PySide2.QtCore import QUrl, Signal, Slot
from PySide2.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QWidget
from PySide2.QtGui import QImage, QPixmap, Qt, QIcon
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from qt.Ui_Form import Ui_Form
import numpy as np
import cv2, os

class ViewController(QWidget, Ui_Form):
    startInferenceSignal = Signal()
    stopInferenceSignal = Signal()
    startCountingSignal = Signal()

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

        self.setupSignalSlots()
        # development
        
        self.setVideo(os.getcwd() + '/data/video/VehicleTest.mp4')
        self.setCacheData(os.getcwd() + '/outputs/data.h5')

    def setupSignalSlots(self):
        self.loadVideoBtn.clicked.connect(self.openVideoFile)
        self.playBtn.clicked.connect(self.toggleVideoState)
        self.mediaPlayer.durationChanged.connect(self.setVideoSliderRange)
        self.mediaPlayer.positionChanged.connect(self.setVideoTime)
        self.videoSlider.valueChanged.connect(self.mediaPlayer.setPosition)

        self.setOutputFileBtn.clicked.connect(self.getOutputFileName)
        self.startInferenceBtn.clicked.connect(self.startInference)
        self.stopInferenceBtn.clicked.connect(self.stopInference)
        self.startInferenceSignal.connect(self.model.startInference)
        self.stopInferenceSignal.connect(self.model.stopInference)
        self.model.frame_update_signal.connect(self.updateFrame)
        self.model.max_frame_update_signal.connect(self.updateMaxFrameNum)
        self.loadCacheBtn.clicked.connect(self.openCacheFile)
        self.countBtn.clicked.connect(self.startCounting)
        self.startCountingSignal.connect(self.model.startCounting)
        self.model.vehicle_count_signal.connect(self.updateVehicleCount)
        self.model.process_done_signal.connect(self.onProcessDone)

        self.frameSlider.valueChanged.connect(self.model.previewFrame)

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

        content = QMediaContent(QUrl.fromLocalFile(file_path))
        self.mediaPlayer.setMedia(content)
        self.mediaPlayer.play()
        self.mediaPlayer.pause()

        # set the output file name to match as well
        self.setOutputFile(file_path)

    def setOutputFile(self, file_path):
        if '.mp4' in file_path:
            file_path = file_path.replace('.mp4', '')
        self.outputVideoFile = file_path + '.avi'
        self.outputDataFile = file_path + '.hdf'
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

    def startCounting(self):
        if self.cacheDataFile != '':
            self.prepareforAnalysis()
            self.startCountingSignal.emit()
        else:
            QMessageBox.warning(self, 'Error', 'No cache file selected!')

    @Slot(int,int,int,np.ndarray)
    def updateVehicleCount(self, class_id, uid, count, img):
        if class_id == 1:
            self.truckCount.display(count)
            item = QTableWidgetItem()
            pixmap = self.convert_cv_qt(img, 100, 100)
            item.setData(Qt.DecorationRole, pixmap)
            self.truckPreviewTable.setItem(count-1,0,item)
            item = QTableWidgetItem(str(uid))
            self.truckPreviewTable.setItem(count-1,1,item)
        elif class_id == 2:
            self.carCount.display(count)
            item = QTableWidgetItem()
            pixmap = self.convert_cv_qt(img, 100, 100)
            item.setData(Qt.DecorationRole, pixmap)
            self.carPreviewTable.setItem(count-1,0,item)
            item = QTableWidgetItem(str(uid))
            self.carPreviewTable.setItem(count-1,1,item)

#================== Inference Functions ======================

    def startInference(self):
        self.prepareforAnalysis()
        self.startInferenceSignal.emit()
    
    def stopInference(self):
        self.model.stopInference()
        self.enableControls(True)

#=================== Helper Functions =========================

    def prepareforAnalysis(self):
        # set parameters

        # change video display to frames updated by Qlabel
        self.videoSwitcher.setCurrentIndex(1)

        self.enableControls(False)

    def enableControls(self, state=True):
        self.mediaGBox.setEnabled(state)
        self.inferenceGBox.setEnabled(state)
        self.countingGBox.setEnabled(state)
        self.frameSlider.setEnabled(state)
        self.stopInferenceBtn.setEnabled(not state)

    def onProcessDone(self):
        self.enableControls(True)

    @Slot(int)
    def updateMaxFrameNum(self, frame_num):
        self.maxFrameNum.setText(str(frame_num))
        self.frameSlider.setMaximum(frame_num)

    @Slot(np.ndarray, int)
    def updateFrame(self, cv_img, frame_num):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img, self.frameLabel.width(), self.frameLabel.height())
        self.frameLabel.setPixmap(qt_img)
        self.frameSlider.setSliderPosition(frame_num)
        self.frameNum.setText(str(frame_num))
    
    def convert_cv_qt(self, rgb_image, width, height):
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(width, height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)