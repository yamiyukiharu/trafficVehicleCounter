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

from pyqtgraph import ImageView


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1033, 820)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.videoSwitcher = QGroupBox(Form)
        self.videoSwitcher.setObjectName(u"videoSwitcher")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoSwitcher.sizePolicy().hasHeightForWidth())
        self.videoSwitcher.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.videoSwitcher)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 5)
        self.frameView = ImageView(self.videoSwitcher)
        self.frameView.setObjectName(u"frameView")
        sizePolicy.setHeightForWidth(self.frameView.sizePolicy().hasHeightForWidth())
        self.frameView.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.frameView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, 0)
        self.stopProcessBtn = QPushButton(self.videoSwitcher)
        self.stopProcessBtn.setObjectName(u"stopProcessBtn")
        self.stopProcessBtn.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stopProcessBtn.sizePolicy().hasHeightForWidth())
        self.stopProcessBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.stopProcessBtn)

        self.frameSlider = QSlider(self.videoSwitcher)
        self.frameSlider.setObjectName(u"frameSlider")
        self.frameSlider.setEnabled(True)
        self.frameSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.frameSlider)

        self.frameNum = QLabel(self.videoSwitcher)
        self.frameNum.setObjectName(u"frameNum")

        self.horizontalLayout_5.addWidget(self.frameNum)

        self.label_13 = QLabel(self.videoSwitcher)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.maxFrameNum = QLabel(self.videoSwitcher)
        self.maxFrameNum.setObjectName(u"maxFrameNum")

        self.horizontalLayout_5.addWidget(self.maxFrameNum)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.videoSwitcher)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.mediaGBox = QGroupBox(Form)
        self.mediaGBox.setObjectName(u"mediaGBox")
        self.gridLayout_2 = QGridLayout(self.mediaGBox)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.mediaGBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.mediaGBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.inputVideoFileLabel = QLineEdit(self.mediaGBox)
        self.inputVideoFileLabel.setObjectName(u"inputVideoFileLabel")

        self.horizontalLayout_9.addWidget(self.inputVideoFileLabel)

        self.loadVideoBtn = QToolButton(self.mediaGBox)
        self.loadVideoBtn.setObjectName(u"loadVideoBtn")

        self.horizontalLayout_9.addWidget(self.loadVideoBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cacheDataLabel = QLineEdit(self.mediaGBox)
        self.cacheDataLabel.setObjectName(u"cacheDataLabel")

        self.horizontalLayout_10.addWidget(self.cacheDataLabel)

        self.loadCacheBtn = QToolButton(self.mediaGBox)
        self.loadCacheBtn.setObjectName(u"loadCacheBtn")

        self.horizontalLayout_10.addWidget(self.loadCacheBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.mediaGBox)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.saveMaskBtn = QPushButton(self.groupBox)
        self.saveMaskBtn.setObjectName(u"saveMaskBtn")

        self.gridLayout_5.addWidget(self.saveMaskBtn, 3, 2, 1, 1)

        self.resetMaskBtn = QPushButton(self.groupBox)
        self.resetMaskBtn.setObjectName(u"resetMaskBtn")

        self.gridLayout_5.addWidget(self.resetMaskBtn, 3, 0, 1, 1)

        self.drawMaskBtn = QPushButton(self.groupBox)
        self.drawMaskBtn.setObjectName(u"drawMaskBtn")

        self.gridLayout_5.addWidget(self.drawMaskBtn, 3, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 1, 0, 1, 1)

        self.maskStokeSpn = QSpinBox(self.groupBox)
        self.maskStokeSpn.setObjectName(u"maskStokeSpn")
        self.maskStokeSpn.setMaximum(200)
        self.maskStokeSpn.setValue(50)

        self.gridLayout_5.addWidget(self.maskStokeSpn, 1, 1, 1, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.maskFileLbl = QLineEdit(self.groupBox)
        self.maskFileLbl.setObjectName(u"maskFileLbl")
        self.maskFileLbl.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.maskFileLbl)

        self.setMaskFileBtn = QToolButton(self.groupBox)
        self.setMaskFileBtn.setObjectName(u"setMaskFileBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.setMaskFileBtn.sizePolicy().hasHeightForWidth())
        self.setMaskFileBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.setMaskFileBtn)


        self.gridLayout_5.addLayout(self.horizontalLayout_8, 2, 1, 1, 2)


        self.verticalLayout_9.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.inferenceGBox = QGroupBox(Form)
        self.inferenceGBox.setObjectName(u"inferenceGBox")
        self.inferenceGBox.setEnabled(True)
        self.formLayout = QFormLayout(self.inferenceGBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setContentsMargins(8, 8, 8, 8)
        self.modelLabel = QLabel(self.inferenceGBox)
        self.modelLabel.setObjectName(u"modelLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.modelLabel)

        self.modelComboBox = QComboBox(self.inferenceGBox)
        self.modelComboBox.addItem("")
        self.modelComboBox.setObjectName(u"modelComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.modelComboBox)

        self.iOUThresholdLabel_2 = QLabel(self.inferenceGBox)
        self.iOUThresholdLabel_2.setObjectName(u"iOUThresholdLabel_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.iOUThresholdLabel_2)

        self.cosineDistSpn = QDoubleSpinBox(self.inferenceGBox)
        self.cosineDistSpn.setObjectName(u"cosineDistSpn")
        self.cosineDistSpn.setDecimals(1)
        self.cosineDistSpn.setValue(0.400000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cosineDistSpn)

        self.iOUThresholdLabel = QLabel(self.inferenceGBox)
        self.iOUThresholdLabel.setObjectName(u"iOUThresholdLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.iOUThresholdLabel)

        self.iouThreshSpn = QDoubleSpinBox(self.inferenceGBox)
        self.iouThreshSpn.setObjectName(u"iouThreshSpn")
        self.iouThreshSpn.setDecimals(2)
        self.iouThreshSpn.setValue(0.450000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.iouThreshSpn)

        self.confidenceThresholdLabel = QLabel(self.inferenceGBox)
        self.confidenceThresholdLabel.setObjectName(u"confidenceThresholdLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.confidenceThresholdLabel)

        self.scoreThreshSpn = QDoubleSpinBox(self.inferenceGBox)
        self.scoreThreshSpn.setObjectName(u"scoreThreshSpn")
        self.scoreThreshSpn.setDecimals(1)
        self.scoreThreshSpn.setValue(0.700000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.scoreThreshSpn)

        self.label_7 = QLabel(self.inferenceGBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.outputFileLabel = QLineEdit(self.inferenceGBox)
        self.outputFileLabel.setObjectName(u"outputFileLabel")
        self.outputFileLabel.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.outputFileLabel)

        self.setOutputFileBtn = QToolButton(self.inferenceGBox)
        self.setOutputFileBtn.setObjectName(u"setOutputFileBtn")
        sizePolicy2.setHeightForWidth(self.setOutputFileBtn.sizePolicy().hasHeightForWidth())
        self.setOutputFileBtn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.setOutputFileBtn)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.startInferenceBtn = QPushButton(self.inferenceGBox)
        self.startInferenceBtn.setObjectName(u"startInferenceBtn")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.startInferenceBtn)


        self.horizontalLayout_2.addWidget(self.inferenceGBox)

        self.countingGBox = QGroupBox(Form)
        self.countingGBox.setObjectName(u"countingGBox")
        self.verticalLayout_8 = QVBoxLayout(self.countingGBox)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_16 = QLabel(self.countingGBox)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_7.addWidget(self.label_16)

        self.countMethodCmb = QComboBox(self.countingGBox)
        self.countMethodCmb.addItem("")
        self.countMethodCmb.addItem("")
        self.countMethodCmb.setObjectName(u"countMethodCmb")

        self.horizontalLayout_7.addWidget(self.countMethodCmb)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.countingMethodSwitcher = QStackedWidget(self.countingGBox)
        self.countingMethodSwitcher.setObjectName(u"countingMethodSwitcher")
        self.vectorPage = QWidget()
        self.vectorPage.setObjectName(u"vectorPage")
        self.gridLayout_3 = QGridLayout(self.vectorPage)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.widthFilterVectorSpn = QSpinBox(self.vectorPage)
        self.widthFilterVectorSpn.setObjectName(u"widthFilterVectorSpn")
        self.widthFilterVectorSpn.setMaximum(1000)
        self.widthFilterVectorSpn.setValue(192)

        self.gridLayout_3.addWidget(self.widthFilterVectorSpn, 2, 2, 1, 1)

        self.xFilterVectorSpn = QDoubleSpinBox(self.vectorPage)
        self.xFilterVectorSpn.setObjectName(u"xFilterVectorSpn")
        self.xFilterVectorSpn.setDecimals(0)
        self.xFilterVectorSpn.setMinimum(-1000.000000000000000)
        self.xFilterVectorSpn.setMaximum(1000.000000000000000)
        self.xFilterVectorSpn.setValue(-258.000000000000000)

        self.gridLayout_3.addWidget(self.xFilterVectorSpn, 0, 2, 1, 1)

        self.label_12 = QLabel(self.vectorPage)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)

        self.label_5 = QLabel(self.vectorPage)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_14 = QLabel(self.vectorPage)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_11 = QLabel(self.vectorPage)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_6 = QLabel(self.vectorPage)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)

        self.distFilterSpn = QSpinBox(self.vectorPage)
        self.distFilterSpn.setObjectName(u"distFilterSpn")
        self.distFilterSpn.setMaximum(1000)
        self.distFilterSpn.setValue(440)

        self.gridLayout_3.addWidget(self.distFilterSpn, 3, 2, 1, 1)

        self.skipFrameFilterSpn = QSpinBox(self.vectorPage)
        self.skipFrameFilterSpn.setObjectName(u"skipFrameFilterSpn")
        self.skipFrameFilterSpn.setValue(10)

        self.gridLayout_3.addWidget(self.skipFrameFilterSpn, 4, 2, 1, 1)

        self.label_4 = QLabel(self.vectorPage)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.visualizeChk = QCheckBox(self.vectorPage)
        self.visualizeChk.setObjectName(u"visualizeChk")

        self.gridLayout_3.addWidget(self.visualizeChk, 5, 0, 1, 1)

        self.yFilterVectorSpn = QDoubleSpinBox(self.vectorPage)
        self.yFilterVectorSpn.setObjectName(u"yFilterVectorSpn")
        self.yFilterVectorSpn.setEnabled(False)
        self.yFilterVectorSpn.setDecimals(0)
        self.yFilterVectorSpn.setMinimum(-1000.000000000000000)
        self.yFilterVectorSpn.setMaximum(1000.000000000000000)
        self.yFilterVectorSpn.setValue(357.000000000000000)

        self.gridLayout_3.addWidget(self.yFilterVectorSpn, 1, 2, 1, 1)

        self.vectorDirectionLbl = QLabel(self.vectorPage)
        self.vectorDirectionLbl.setObjectName(u"vectorDirectionLbl")
        self.vectorDirectionLbl.setStyleSheet(u"color: rgb(252, 1, 7);")

        self.gridLayout_3.addWidget(self.vectorDirectionLbl, 1, 0, 1, 1, Qt.AlignHCenter)

        self.countingMethodSwitcher.addWidget(self.vectorPage)
        self.finishLinePage = QWidget()
        self.finishLinePage.setObjectName(u"finishLinePage")
        self.gridLayout_4 = QGridLayout(self.finishLinePage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.finishLineFramesSpn = QSpinBox(self.finishLinePage)
        self.finishLineFramesSpn.setObjectName(u"finishLineFramesSpn")
        self.finishLineFramesSpn.setMaximum(200)
        self.finishLineFramesSpn.setValue(5)

        self.gridLayout_4.addWidget(self.finishLineFramesSpn, 0, 1, 1, 1)

        self.finishLineChk = QCheckBox(self.finishLinePage)
        self.finishLineChk.setObjectName(u"finishLineChk")

        self.gridLayout_4.addWidget(self.finishLineChk, 1, 0, 1, 1)

        self.label_18 = QLabel(self.finishLinePage)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.countingMethodSwitcher.addWidget(self.finishLinePage)

        self.verticalLayout_8.addWidget(self.countingMethodSwitcher)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.countAnalyzeBtn = QPushButton(self.countingGBox)
        self.countAnalyzeBtn.setObjectName(u"countAnalyzeBtn")

        self.horizontalLayout_6.addWidget(self.countAnalyzeBtn)

        self.countBtn = QPushButton(self.countingGBox)
        self.countBtn.setObjectName(u"countBtn")

        self.horizontalLayout_6.addWidget(self.countBtn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addWidget(self.countingGBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.carCount = QLCDNumber(self.widget_2)
        self.carCount.setObjectName(u"carCount")
        self.carCount.setLineWidth(0)
        self.carCount.setDigitCount(3)
        self.carCount.setSegmentStyle(QLCDNumber.Flat)
        self.carCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.carCount, 1, 1, 1, 1)

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
        self.truckCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.truckCount, 1, 0, 1, 1)

        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_15, 0, 2, 1, 1, Qt.AlignHCenter)

        self.busCount = QLCDNumber(self.widget_2)
        self.busCount.setObjectName(u"busCount")
        self.busCount.setLineWidth(0)
        self.busCount.setDigitCount(3)
        self.busCount.setSegmentStyle(QLCDNumber.Flat)
        self.busCount.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.busCount, 1, 2, 1, 1)


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
        self.truckPreviewTable.horizontalHeader().setVisible(True)
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
        self.busPreviewTab = QWidget()
        self.busPreviewTab.setObjectName(u"busPreviewTab")
        self.verticalLayout_7 = QVBoxLayout(self.busPreviewTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.busPreviewTable = QTableWidget(self.busPreviewTab)
        if (self.busPreviewTable.columnCount() < 2):
            self.busPreviewTable.setColumnCount(2)
        if (self.busPreviewTable.rowCount() < 30):
            self.busPreviewTable.setRowCount(30)
        self.busPreviewTable.setObjectName(u"busPreviewTable")
        self.busPreviewTable.setShowGrid(True)
        self.busPreviewTable.setGridStyle(Qt.SolidLine)
        self.busPreviewTable.setRowCount(30)
        self.busPreviewTable.setColumnCount(2)
        self.busPreviewTable.horizontalHeader().setMinimumSectionSize(110)
        self.busPreviewTable.horizontalHeader().setDefaultSectionSize(110)
        self.busPreviewTable.verticalHeader().setMinimumSectionSize(110)
        self.busPreviewTable.verticalHeader().setDefaultSectionSize(110)

        self.verticalLayout_7.addWidget(self.busPreviewTable)

        self.previewTabWidget.addTab(self.busPreviewTab, "")

        self.verticalLayout.addWidget(self.previewTabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)
        self.visualizeChk.toggled.connect(self.xFilterVectorSpn.setEnabled)
        self.visualizeChk.toggled.connect(self.widthFilterVectorSpn.setEnabled)
        self.visualizeChk.toggled.connect(self.distFilterSpn.setEnabled)
        self.visualizeChk.toggled.connect(self.yFilterVectorSpn.setEnabled)

        self.countMethodCmb.setCurrentIndex(1)
        self.countingMethodSwitcher.setCurrentIndex(1)
        self.previewTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Traffic Vehicle Counter", None))
        self.videoSwitcher.setTitle(QCoreApplication.translate("Form", u"Video", None))
        self.stopProcessBtn.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.frameNum.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"/", None))
        self.maxFrameNum.setText(QCoreApplication.translate("Form", u"N", None))
        self.mediaGBox.setTitle(QCoreApplication.translate("Form", u"Media", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Input Video:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Cache Data:", None))
        self.loadVideoBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.loadCacheBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Masking", None))
        self.saveMaskBtn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.resetMaskBtn.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.drawMaskBtn.setText(QCoreApplication.translate("Form", u"Draw", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Mask File:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Stroke Size:", None))
        self.setMaskFileBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.inferenceGBox.setTitle(QCoreApplication.translate("Form", u"Inference", None))
        self.modelLabel.setText(QCoreApplication.translate("Form", u"Model: ", None))
        self.modelComboBox.setItemText(0, QCoreApplication.translate("Form", u"YoloV4", None))

        self.iOUThresholdLabel_2.setText(QCoreApplication.translate("Form", u"Cosine Distance:", None))
        self.iOUThresholdLabel.setText(QCoreApplication.translate("Form", u"IOU Threshold:", None))
        self.confidenceThresholdLabel.setText(QCoreApplication.translate("Form", u"Score Threshold", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Output File:", None))
        self.setOutputFileBtn.setText(QCoreApplication.translate("Form", u"...", None))
        self.startInferenceBtn.setText(QCoreApplication.translate("Form", u"START", None))
        self.countingGBox.setTitle(QCoreApplication.translate("Form", u"Counting", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Method:", None))
        self.countMethodCmb.setItemText(0, QCoreApplication.translate("Form", u"Vector", None))
        self.countMethodCmb.setItemText(1, QCoreApplication.translate("Form", u"Finish Line", None))

        self.countMethodCmb.setCurrentText(QCoreApplication.translate("Form", u"Finish Line", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Y:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Travel Distance (pixels)", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Filter Vector Width", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"X:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Max Skipped Frames", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Filter Vector (pixels)", None))
        self.visualizeChk.setText(QCoreApplication.translate("Form", u"Show Vector", None))
        self.vectorDirectionLbl.setText(QCoreApplication.translate("Form", u"DOWN", None))
        self.finishLineChk.setText(QCoreApplication.translate("Form", u"Show Finish Line", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"frames to count:", None))
        self.countAnalyzeBtn.setText(QCoreApplication.translate("Form", u"Count + Analyze", None))
        self.countBtn.setText(QCoreApplication.translate("Form", u"Quick Count", None))
        self.label.setText(QCoreApplication.translate("Form", u"Trucks", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Cars", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Bus", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Detections", None))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.truckPreviewTab), QCoreApplication.translate("Form", u"Trucks", None))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.carPreviewTab), QCoreApplication.translate("Form", u"Cars", None))
        self.previewTabWidget.setTabText(self.previewTabWidget.indexOf(self.busPreviewTab), QCoreApplication.translate("Form", u"Bus", None))
    # retranslateUi

