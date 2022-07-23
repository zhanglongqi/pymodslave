# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import pyModSlaveQt_rc

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(240, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMinimumSize(QSize(240, 200))
        Settings.setMaximumSize(QSize(240, 200))
        icon = QIcon()
        icon.addFile(u":/img/options-16.png", QSize(), QIcon.Normal, QIcon.Off)
        Settings.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sbNoOfCoils = QSpinBox(Settings)
        self.sbNoOfCoils.setObjectName(u"sbNoOfCoils")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sbNoOfCoils.sizePolicy().hasHeightForWidth())
        self.sbNoOfCoils.setSizePolicy(sizePolicy1)
        self.sbNoOfCoils.setMinimumSize(QSize(50, 0))
        self.sbNoOfCoils.setMaximumSize(QSize(75, 16777215))
        self.sbNoOfCoils.setMinimum(1)
        self.sbNoOfCoils.setMaximum(500)
        self.sbNoOfCoils.setSingleStep(10)
        self.sbNoOfCoils.setValue(50)

        self.gridLayout.addWidget(self.sbNoOfCoils, 0, 2, 1, 1)

        self.lblNoOfInputRegs = QLabel(Settings)
        self.lblNoOfInputRegs.setObjectName(u"lblNoOfInputRegs")

        self.gridLayout.addWidget(self.lblNoOfInputRegs, 2, 1, 1, 1)

        self.sbNoOfInputRegs = QSpinBox(Settings)
        self.sbNoOfInputRegs.setObjectName(u"sbNoOfInputRegs")
        sizePolicy1.setHeightForWidth(self.sbNoOfInputRegs.sizePolicy().hasHeightForWidth())
        self.sbNoOfInputRegs.setSizePolicy(sizePolicy1)
        self.sbNoOfInputRegs.setMinimumSize(QSize(50, 0))
        self.sbNoOfInputRegs.setMaximumSize(QSize(75, 16777215))
        self.sbNoOfInputRegs.setMinimum(1)
        self.sbNoOfInputRegs.setMaximum(500)
        self.sbNoOfInputRegs.setSingleStep(10)
        self.sbNoOfInputRegs.setValue(50)

        self.gridLayout.addWidget(self.sbNoOfInputRegs, 2, 2, 1, 1)

        self.lblCoils = QLabel(Settings)
        self.lblCoils.setObjectName(u"lblCoils")
        sizePolicy1.setHeightForWidth(self.lblCoils.sizePolicy().hasHeightForWidth())
        self.lblCoils.setSizePolicy(sizePolicy1)
        self.lblCoils.setMinimumSize(QSize(132, 0))
        self.lblCoils.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.lblCoils, 0, 1, 1, 1)

        self.sbNoOfDigInputs = QSpinBox(Settings)
        self.sbNoOfDigInputs.setObjectName(u"sbNoOfDigInputs")
        sizePolicy1.setHeightForWidth(self.sbNoOfDigInputs.sizePolicy().hasHeightForWidth())
        self.sbNoOfDigInputs.setSizePolicy(sizePolicy1)
        self.sbNoOfDigInputs.setMinimumSize(QSize(50, 0))
        self.sbNoOfDigInputs.setMaximumSize(QSize(75, 16777215))
        self.sbNoOfDigInputs.setMinimum(1)
        self.sbNoOfDigInputs.setMaximum(500)
        self.sbNoOfDigInputs.setSingleStep(10)
        self.sbNoOfDigInputs.setValue(50)

        self.gridLayout.addWidget(self.sbNoOfDigInputs, 1, 2, 1, 1)

        self.lblNoOfHoldingRegs = QLabel(Settings)
        self.lblNoOfHoldingRegs.setObjectName(u"lblNoOfHoldingRegs")

        self.gridLayout.addWidget(self.lblNoOfHoldingRegs, 3, 1, 1, 1)

        self.lblNoOfDigInputs = QLabel(Settings)
        self.lblNoOfDigInputs.setObjectName(u"lblNoOfDigInputs")

        self.gridLayout.addWidget(self.lblNoOfDigInputs, 1, 1, 1, 1)

        self.sbNoOfHoldingRegs = QSpinBox(Settings)
        self.sbNoOfHoldingRegs.setObjectName(u"sbNoOfHoldingRegs")
        sizePolicy1.setHeightForWidth(self.sbNoOfHoldingRegs.sizePolicy().hasHeightForWidth())
        self.sbNoOfHoldingRegs.setSizePolicy(sizePolicy1)
        self.sbNoOfHoldingRegs.setMinimumSize(QSize(50, 0))
        self.sbNoOfHoldingRegs.setMaximumSize(QSize(75, 16777215))
        self.sbNoOfHoldingRegs.setMinimum(1)
        self.sbNoOfHoldingRegs.setMaximum(500)
        self.sbNoOfHoldingRegs.setSingleStep(10)
        self.sbNoOfHoldingRegs.setValue(50)

        self.gridLayout.addWidget(self.sbNoOfHoldingRegs, 3, 2, 1, 1)

        self.lblMaxNoOfBusMonitorLines = QLabel(Settings)
        self.lblMaxNoOfBusMonitorLines.setObjectName(u"lblMaxNoOfBusMonitorLines")

        self.gridLayout.addWidget(self.lblMaxNoOfBusMonitorLines, 4, 1, 1, 1)

        self.sbMaxNoOfBusMonitorLines = QSpinBox(Settings)
        self.sbMaxNoOfBusMonitorLines.setObjectName(u"sbMaxNoOfBusMonitorLines")
        self.sbMaxNoOfBusMonitorLines.setMaximum(100)
        self.sbMaxNoOfBusMonitorLines.setValue(50)

        self.gridLayout.addWidget(self.sbMaxNoOfBusMonitorLines, 4, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Settings)
        self.buttonBox.accepted.connect(Settings.accept)
        self.buttonBox.rejected.connect(Settings.reject)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.lblNoOfInputRegs.setText(QCoreApplication.translate("Settings", u"No Of Input Registers", None))
        self.lblCoils.setText(QCoreApplication.translate("Settings", u"No Of Coils", None))
        self.lblNoOfHoldingRegs.setText(QCoreApplication.translate("Settings", u"No Of Holding Registers", None))
        self.lblNoOfDigInputs.setText(QCoreApplication.translate("Settings", u"No Of Digital Inputs", None))
        self.lblMaxNoOfBusMonitorLines.setText(QCoreApplication.translate("Settings", u"Max No of Bus Monitor Lines", None))
    # retranslateUi

