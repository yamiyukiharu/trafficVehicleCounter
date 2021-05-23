
from typing import Tuple
from PySide2.QtCore import QPoint, QUrl, Signal, Slot
from PySide2.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QWidget
from PySide2.QtGui import QImage, QPixmap, Qt, QIcon
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
        self.maskFile = ''
        self.carPreviewTable.setHorizontalHeaderLabels(['Preview', 'ID'])
        self.truckPreviewTable.setHorizontalHeaderLabels(['Preview', 'ID'])
        self.frameView.ui.histogram.hide()
        self.frameView.ui.roiBtn.hide()
        self.frameView.ui.menuBtn.hide()
        self.frameView.view.setMouseEnabled(False,False)
        self.imgMask = None
        
        self.visualizeMarkerStart = QPoint(200,200)
        self.visualizeMarkerEnd = QPoint(500,500)
        self.visualizeMarker = pg.LineROI(self.visualizeMarkerStart, self.visualizeMarkerEnd, 50)
        self.finishLine = pg.RectROI((200,200), (200,200), rotatable=True, resizable=True)

        self.setupSignalSlots()
        # development
        
        self.setVideo(os.getcwd() + '/data/video/VehicleTest.mp4')
        self.setCacheData(os.getcwd() + '/data/video/VehicleTest.h5')

    def setupSignalSlots(self):
        self.loadVideoBtn.clicked.connect(self.openVideoFile)

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
        self.drawMaskBtn.clicked.connect(self.drawMask)
        self.resetMaskBtn.clicked.connect(self.resetMask)
        self.setMaskFileBtn.clicked.connect(self.openMaskFile)
        self.saveMaskBtn.clicked.connect(self.saveMask)

        self.yFilterVectorSpn.valueChanged.connect(self.updateVectorDirectionLabel)
        self.countMethodCmb.currentIndexChanged.connect(self.countingMethodSwitcher.setCurrentIndex)
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

    def openMaskFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Mask File", '', "hdf (*.h5)")
        if file_path != '':
            self.model.setMaskFile(file_path)
            self.maskFile = file_path
            self.maskFileLbl.setText(self.maskFile)
            self.imgMask = self.model.getMask()
            self.maskPreview = cv2.bitwise_and(self.frameView.image, self.frameView.image, mask=self.imgMask)

    def saveMask(self):
        if self.imgMask is None:
            QMessageBox.warning(self, 'Error', 'Mask not drawn yet!')
            return
        if self.maskFile == '':
            file_path, _ = QFileDialog().getSaveFileName()
            if file_path != '':        
                self.maskFile = file_path
                self.maskFileLbl.setText(self.maskFile)    
        self.model.saveMask(self.maskFile, self.imgMask)

#======================= Setting Data sources ========================

    def setVideo(self, file_path):
        self.inputVideoFile = file_path
        self.inputVideoFileLabel.setText(file_path)
        self.model.setInputVideoPath(self.inputVideoFile)

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

    def updateVectorDirectionLabel(self):
        if self.yFilterVectorSpn.value() > 0:
            self.vectorDirectionLbl.setText('DOWN')
        else:
            self.vectorDirectionLbl.setText('UP')

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

#================== Masking Functions ======================

    def resetMask(self):
        if self.frameView.image is None:
            QMessageBox.warning(self, 'Error', 'No image to mask!')
            return
        self.maskPreview = self.frameView.image.copy()
        cv2.imshow('Mask', self.maskPreview)
        self.imgMask = np.ones(self.frameView.image.shape[:2], dtype = np.uint8)

    def drawMask(self):
        if self.imgMask is None:
            self.resetMask()
        self.drawing = False
        cv2.namedWindow('Mask')
        cv2.setMouseCallback('Mask', self.maskMouse)
        cv2.imshow('Mask', self.maskPreview)    

    def maskMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            cv2.circle(self.maskPreview, (x,y), self.maskStokeSpn.value(), [0,0,0], -1)
            cv2.circle(self.imgMask, (x,y), self.maskStokeSpn.value(), 0, -1)

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                cv2.circle(self.maskPreview, (x, y), self.maskStokeSpn.value(), [0,0,0], -1)
                cv2.circle(self.imgMask, (x, y), self.maskStokeSpn.value(), 0, -1)

        elif event == cv2.EVENT_LBUTTONUP:
            if self.drawing == True:
                self.drawing = False
                cv2.circle(self.maskPreview, (x, y), self.maskStokeSpn.value(), [0,0,0], -1)
                cv2.circle(self.imgMask, (x, y), self.maskStokeSpn.value(), 0, -1)
        cv2.imshow('Mask', self.maskPreview)
        

#=================== Helper Functions =========================

    def prepareforAnalysis(self):
        # set parameters
        self.model.setParams(
            {
                'mask'          : self.imgMask,
                'count_method'  : self.countMethodCmb.currentIndex(),
                'iou_thresh'    : self.iouThreshSpn.value(),
                'score_thresh'  : self.scoreThreshSpn.value(),
                'cos_dist'      : self.cosineDistSpn.value(),
                'x_vect'        : self.xFilterVectorSpn.value(),
                'y_vect'        : self.yFilterVectorSpn.value(),
                'filt_width'    : self.widthFilterVectorSpn.value(),
                'filt_dist'     : self.distFilterSpn.value(),
                'filt_frames'   : self.skipFrameFilterSpn.value(),
                'finish_frames' : self.finishLineFramesSpn.value(),
                'finish_line'   : self.getFinishLineBounds(),
            }
        )

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
        self.frameView.view.setXRange(0, cv_img.shape[1])
        self.frameView.view.setYRange(0, cv_img.shape[0])
        self.frameView.setImage(cv_img)
        self.frameNum.setText(str(frame_num))
    
    def convert_cv_qt(self, rgb_image, width, height):
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(width, height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)