# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtMultimediaWidgets import QVideoWidget
from pyqtgraph import ImageView


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1103, 813)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.videoSwitcher = QTabWidget(Form)
        self.videoSwitcher.setObjectName(u"videoSwitcher")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoSwitcher.sizePolicy().hasHeightForWidth())
        self.videoSwitcher.setSizePolicy(sizePolicy)
        self.videoPlaybackPage = QWidget()
        self.videoPlaybackPage.setObjectName(u"videoPlaybackPage")
        sizePolicy.setHeightForWidth(self.videoPlaybackPage.sizePolicy().hasHeightForWidth())
        self.videoPlaybackPage.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.videoPlaybackPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.videoFrame = QVideoWidget(self.videoPlaybackPage)
        self.videoFrame.setObjectName(u"videoFrame")
        sizePolicy.setHeightForWidth(self.videoFrame.sizePolicy().hasHeightForWidth())
        self.videoFrame.setSizePolicy(sizePolicy)
        self.videoFrame.setMinimumSize(QSize(800, 450))
        self.videoFrame.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.videoFrame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, 0)
        self.playBtn = QPushButton(self.videoPlaybackPage)
        self.playBtn.setObjectName(u"playBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.playBtn.sizePolicy().hasHeightForWidth())
        self.playBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.playBtn)

        self.videoSlider = QSlider(self.videoPlaybackPage)
        self.videoSlider.setObjectName(u"videoSlider")
        self.videoSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.videoSlider)

        self.videoTime = QLabel(self.videoPlaybackPage)
        self.videoTime.setObjectName(u"videoTime")

        self.horizontalLayout_3.addWidget(self.videoTime)

        self.label_8 = QLabel(self.videoPlaybackPage)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.videoMaxTime = QLabel(self.videoPlaybackPage)
        self.videoMaxTime.setObjectName(u"videoMaxTime")

        self.horizontalLayout_3.addWidget(self.videoMaxTime)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.videoSwitcher.addTab(self.videoPlaybackPage, "")
        self.analysisPage = QWidget()
        self.analysisPage.setObjectName(u"analysisPage")
        sizePolicy.setHeightForWidth(self.analysisPage.sizePolicy().hasHeightForWidth())
        self.analysisPage.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.analysisPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frameView = ImageView(self.analysisPage)
        self.frameView.setObjectName(u"frameView")
        sizePolicy.setHeightForWidth(self.frameView.sizePolicy().hasHeightForWidth())
        self.frameView.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.frameView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, 0)
        self.stopInferenceBtn = QPushButton(self.analysisPage)
        self.stopInferenceBtn.setObjectName(u"stopInferenceBtn")
        self.stopInferenceBtn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.stopInferenceBtn.sizePolicy().hasHeightForWidth())
        self.stopInferenceBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.stopInferenceBtn)

        self.frameSlider = QSlider(self.analysisPage)
        self.frameSlider.setObjectName(u"frameSlider")
        self.frameSlider.setEnabled(True)
        self.frameSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.frameSlider)

        self.frameNum = QLabel(self.analysisPage)
        self.frameNum.setObjectName(u"frameNum")

        self.horizontalLayout_5.addWidget(self.frameNum)

        self.label_13 = QLabel(self.analysisPage)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.maxFrameNum = QLabel(self.analysisPage)
        self.maxFrameNum.setObjectName(u"maxFrameNum")

        self.horizontalLayout_5.addWidget(self.maxFrameNum)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.videoSwitcher.addTab(self.analysisPage, "")

        self.verticalLayout_2.addWidget(self.videoSwitcher)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.mediaGBox = QGroupBox(Form)
        self.mediaGBox.setObjectName(u"mediaGBox")
        self.gridLayout_2 = QGridLayout(self.mediaGBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.loadVideoBtn = QToolButton(self.mediaGBox)
        self.loadVideoBtn.setObjectName(u"loadVideoBtn")

        self.gridLayout_2.addWidget(self.loadVideoBtn, 1, 1, 1, 1)

        self.loadCacheBtn = QToolButton(self.mediaGBox)
        self.loadCacheBtn.setObjectName(u"loadCacheBtn")

        self.gridLayout_2.addWidget(self.loadCacheBtn, 3, 1, 1, 1)

        self.inputVideoFileLabel = QLineEdit(self.mediaGBox)
        self.inputVideoFileLabel.setObjectName(u"inputVideoFileLabel")

        self.gridLayout_2.addWidget(self.inputVideoFileLabel, 0, 1, 1, 1)

        self.label_9 = QLabel(self.mediaGBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.cacheDataLabel = QLineEdit(self.mediaGBox)
        self.cacheDataLabel.setObjectName(u"cacheDataLabel")

        self.gridLayout_2.addWidget(self.cacheDataLabel, 2, 1, 1, 1)

        self.label_10 = QLabel(self.mediaGBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.mediaGBox)

        self.inferenceGBox = QGroupBox(Form)
        self.inferenceGBox.setObjectName(u"inferenceGBox")
        self.inferenceGBox.setEnabled(True)
        self.formLayout = QFormLayout(self.inferenceGBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.modelLabel = QLabel(self.inferenceGBox)
        self.modelLabel.setObjectName(u"modelLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.modelLabel)

        self.modelComboBox = QComboBox(self.inferenceGBox)
        self.modelComboBox.addItem("")
        self.modelComboBox.setObjectName(u"modelComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.modelComboBox)

        self.iOUThresholdLabel = QLabel(self.inferenceGBox)
        self.iOUThresholdLabel.setObjectName(u"iOUThresholdLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.iOUThresholdLabel)

        self.confidenceThresholdLabel = QLabel(self.inferenceGBox)
        self.confidenceThresholdLabel.setObjectName(u"confidenceThresholdLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.confidenceThresholdLabel)

        self.confidenceThresholdDoubleSpinBox = QDoubleSpinBox(self.inferenceGBox)
        self.confidenceThresholdDoubleSpinBox.setObjectName(u"confidenceThresholdDoubleSpinBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.confidenceThresholdDoubleSpinBox)

        self.label_7 = QLabel(self.inferenceGBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.outputFileLabel = QLineEdit(self.inferenceGBox)
        self.outputFileLabel.setObjectName(u"outputFileLabel")
        self.outputFileLabel.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.outputFileLabel)

        self.setOutputFileBtn = QToolButton(self.inferenceGBox)
        self.setOutputFileBtn.setObjectName(u"setOutputFileBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.setOutputFileBtn.sizePolicy().hasHeightForWidth())
        self.setOutputFileBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.setOutputFileBtn)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.iOUThresholdDoubleSpinBox = QDoubleSpinBox(self.inferenceGBox)
        self.iOUThresholdDoubleSpinBox.setObjectName(u"iOUThresholdDoubleSpinBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.iOUThresholdDoubleSpinBox)

        self.startInferenceBtn = QPushButton(self.inferenceGBox)
        self.startInferenceBtn.setObjectName(u"startInferenceBtn")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.startInferenceBtn)


        self.horizontalLayout_2.addWidget(self.inferenceGBox)

        self.countingGBox = QGroupBox(Form)
        self.countingGBox.setObjectName(u"countingGBox")
        self.gridLayout_4 = QGridLayout(self.countingGBox)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(self.countingGBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 1, 3, 1, 1)

        self.label_11 = QLabel(self.countingGBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 1, 1, 1, 1)

        self.label_4 = QLabel(self.countingGBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.xFilterVectorSpn = QDoubleSpinBox(self.countingGBox)
        self.xFilterVectorSpn.setObjectName(u"xFilterVectorSpn")
        self.xFilterVectorSpn.setDecimals(0)
        self.xFilterVectorSpn.setMinimum(-1000.000000000000000)
        self.xFilterVectorSpn.setMaximum(1000.000000000000000)
        self.xFilterVectorSpn.setValue(-5.000000000000000)

        self.gridLayout_4.addWidget(self.xFilterVectorSpn, 1, 2, 1, 1)

        self.yFilterVectorSpn = QDoubleSpinBox(self.countingGBox)
        self.yFilterVectorSpn.setObjectName(u"yFilterVectorSpn")
        self.yFilterVectorSpn.setDecimals(0)
        self.yFilterVectorSpn.setMinimum(-1000.000000000000000)
        self.yFilterVectorSpn.setMaximum(1000.000000000000000)
        self.yFilterVectorSpn.setValue(-5.000000000000000)

        self.gridLayout_4.addWidget(self.yFilterVectorSpn, 1, 4, 1, 1)

        self.label_5 = QLabel(self.countingGBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.countingGBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.distFilterSpn = QSpinBox(self.countingGBox)
        self.distFilterSpn.setObjectName(u"distFilterSpn")
        self.distFilterSpn.setMaximum(1000)

        self.gridLayout_4.addWidget(self.distFilterSpn, 2, 2, 1, 1)

        self.skipFrameFilterSpn = QSpinBox(self.countingGBox)
        self.skipFrameFilterSpn.setObjectName(u"skipFrameFilterSpn")

        self.gridLayout_4.addWidget(self.skipFrameFilterSpn, 3, 2, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.countBtn = QPushButton(self.countingGBox)
        self.countBtn.setObjectName(u"countBtn")

        self.horizontalLayout_6.addWidget(self.countBtn)

        self.visualizeBtn = QPushButton(self.countingGBox)
        self.visualizeBtn.setObjectName(u"visualizeBtn")

        self.horizontalLayout_6.addWidget(self.visualizeBtn)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 4, 0, 1, 5)


        self.horizontalLayout_2.addWidget(self.countingGBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.truckCount = QLCDNumber(self.widget_2)
        self.truckCount.setObjectName(u"truckCount")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.truckCount.sizePolicy().hasHeightForWidth())
        self.truckCount.setSizePolicy(sizePolicy4)
        self.truckCount.setLineWidth(0)
        self.truckCount.setDigitCount(3)
        self.truckCount.setSegmentStyle(QLCDNumber.Flat)
        self.truckCount.setProperty("intValue", 5)

        self.gridLayout.addWidget(self.truckCount, 1, 0, 1, 1)

        self.carCount = QLCDNumber(self.widget_2)
        self.carCount.setObjectName(u"carCount")
        self.carCount.setLineWidth(0)
        self.carCount.setDigitCount(3)
        self.carCount.setSegmentStyle(QLCDNumber.Flat)
        self.carCount.setProperty("intValue", 5)

        self.gridLayout.addWidget(self.carCount, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.previewTabWidget = QTabWidget(Form)
        self.previewTabWidget.setObjectName(u"previewTabWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.previewTabWidget.sizePolicy().hasHeightForWidth())
        self.previewTabWidget.setSizePolicy(sizePolicy5)
        self.previewTabWidget.setMinimumSize(QSize(220, 0))
        self.truckPreviewTab = QWidget()
        self.truckPreviewTab.setObjectName(u"truckPreviewTab")
        self.verticalLayout_5 = QVBoxLayout(self.truckPreviewTab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.truckPreviewTable = QTableWidget(self.truckPreviewTab)
        if (self.truckPreviewTable.columnCount() < 2):
            self.truckPreviewTable.setColumnCount(2)
        if (self.truckPreviewTable.rowCount() < 30):
            self.truckPreviewTable.setRowCount(30)
        self.truckPreviewTable.setObjectName(u"truckPreviewTable")
        self.truckPreviewTable.setRowCount(30)
        self.truckPreviewTable.setColumnCount(2)
        self.truckPreviewTable.horizontalHeader().setVisible(False)
        self.truckPreviewTable.horizontalHeader().setMinimumSectionSize(110)
        self.truckPreviewTable.horizontalHeader().setDefaultSectionSize(110)
        self.truckPreviewTable.verticalHeader().setMinimumSectionSize(110)
        self.truckPreviewTable.verticalHeader().setDefaultSectionSize(110)

        self.verticalLayout_5.addWidget(self.truckPreviewTable)

        self.previewTabWidget.addTab(self.truckPreviewTab, "")
        self.carPreviewTab = QWidget()
        self.carPreviewTab.setObjectName(u"carPreviewTab")
        self.verticalLayout_6 = QVBoxLayout(self.carPreviewTab)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.carPreviewTable = QTableWidget(self.carPreviewTab)
        if (self.carPreviewTable.columnCount() < 2):
            self.carPreviewTable.setColumnCount(2)
        if (self.carPreviewTable.rowCount() < 30):
            self.carPreviewTable.setRowCount(30)
        self.carPreviewTable.setObjectName(u"carPreviewTable")
        self.carPreviewTable.setShowGrid(True)
        self.carPreviewTable.setGridStyle(Qt.SolidLine)
        self.carPreviewTable.setRowCount(30)
        self.carPreviewTable.setColumnCount(2)
        self.carPreviewTable.horizontalHeader().setMinimumSectionSize(110)
        self.carPreviewTable.horizontalHeader().setDefaultSectionSize(110)
        self.carPreviewTable.verticalHeader().setMinimumSectionSize(110)
        self.carPreviewTable.verticalHeader().setDefaultSectionSize(110)

        self.verticalLayout_6.addWidget(self.carPreviewTable)

        self.previewTabWidget.addTab(self.carPreviewTab, "")

        self.verticalLayout.addWidget(self.previewTabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.videoSwitcher.setCurrentIndex(1)
        self.previewTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.playBtn.setText(QCoreApplication.translate("Form", u"Play / Pause", None))
        self.videoTime.setText(QCoreApplication.translate("Form", u"00:00", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"/", None))
        self.videoMaxTime.setText(QCoreApplication.translate("Form", u"00:00", None))
        self.videoSwitcher.setTabText(self.videoSwitcher.indexOf(self.videoPlaybackPage), QCoreApplication.translate("Form", u"Playback", None))
        self.stopInferenceBtn.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.frameNum.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"/", None))
        self.maxFrameNum.setText(QCoreApplication.translate("Form", u"N", None))
        self.videoSwitcher.setTabText(self.videoSwitcher.indexOf(self.analysisPage), QCoreApplication.translate("Form", u"Analysis", None))
        self.mediaGBox.setTitle(QCoreApplication.translate("Form", u"Media", None))
        self.loadVideoBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.loadCacheBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Input Video:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Cache Data:", None))
        self.inferenceGBox.setTitle(QCoreApplication.translate("Form", u"Inference", None))
        self.modelLabel.setText(QCoreApplication.translate("Form", u"Model: ", None))
        self.modelComboBox.setItemText(0, QCoreApplication.translate("Form", u"YoloV4", None))

        self.iOUThresholdLabel.setText(QCoreApplication.translate("Form", u"IOU Threshold:", None))
        self.confidenceThresholdLabel.setText(QCoreApplication.translate("Form", u"Score Threshold", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Output File:", None))
        self.setOutputFileBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.startInferenceBtn.setText(QCoreApplication.translate("Form", u"START", None))
        self.countingGBox.setTitle(QCoreApplication.translate("Form", u"Counting", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Y:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"X:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Filter Vector (pixels)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Travel Distance (pixels)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Max Skipped Frames", None))
        self.countBtn.setText(QCoreApplication.translate("Form", u"Count Offline", None))
        self.visualizeBtn.setText(QCoreApplication.translate("Form", u"Visualize", None))
        self.label.setText(QCoreApplication.translate("Form", u"Trucks", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Cars", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Detections", None))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.truckPreviewTab), QCoreApplication.translate("Form", u"Trucks", None))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.carPreviewTab), QCoreApplication.translate("Form", u"Cars", None))
    # retranslateUi

