# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mbdata.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import pyModSlaveQt_rc

class Ui_MBData(object):
    def setupUi(self, MBData):
        if not MBData.objectName():
            MBData.setObjectName(u"MBData")
        MBData.resize(500, 420)
        MBData.setMinimumSize(QSize(500, 420))
        MBData.setMaximumSize(QSize(500, 420))
        icon = QIcon()
        icon.addFile(u":/img/Bus.png", QSize(), QIcon.Normal, QIcon.Off)
        MBData.setWindowIcon(icon)
        self.centralwidget = QWidget(MBData)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabIOs = QTabWidget(self.centralwidget)
        self.tabIOs.setObjectName(u"tabIOs")
        self.tabIOs.setGeometry(QRect(10, 11, 481, 401))
        self.tabCoils = QWidget()
        self.tabCoils.setObjectName(u"tabCoils")
        self.verticalLayoutWidget = QWidget(self.tabCoils)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(6, 5, 452, 364))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbResetDO = QPushButton(self.verticalLayoutWidget)
        self.pbResetDO.setObjectName(u"pbResetDO")
        self.pbResetDO.setMinimumSize(QSize(48, 0))
        self.pbResetDO.setMaximumSize(QSize(48, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/img/refresh-16.png", QSize(), QIcon.Normal, QIcon.On)
        self.pbResetDO.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pbResetDO)

        self.chkSimCoils = QCheckBox(self.verticalLayoutWidget)
        self.chkSimCoils.setObjectName(u"chkSimCoils")

        self.horizontalLayout.addWidget(self.chkSimCoils)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tvCoilsData = QTableView(self.verticalLayoutWidget)
        self.tvCoilsData.setObjectName(u"tvCoilsData")
        self.tvCoilsData.setMinimumSize(QSize(450, 330))

        self.verticalLayout.addWidget(self.tvCoilsData)

        icon2 = QIcon()
        icon2.addFile(u":/img/DO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabIOs.addTab(self.tabCoils, icon2, "")
        self.tabDiscreteInputs = QWidget()
        self.tabDiscreteInputs.setObjectName(u"tabDiscreteInputs")
        self.verticalLayoutWidget_2 = QWidget(self.tabDiscreteInputs)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(6, 5, 452, 364))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pbResetDI = QPushButton(self.verticalLayoutWidget_2)
        self.pbResetDI.setObjectName(u"pbResetDI")
        self.pbResetDI.setMinimumSize(QSize(48, 0))
        self.pbResetDI.setMaximumSize(QSize(48, 16777215))
        self.pbResetDI.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pbResetDI)

        self.chkSimDisInputs = QCheckBox(self.verticalLayoutWidget_2)
        self.chkSimDisInputs.setObjectName(u"chkSimDisInputs")

        self.horizontalLayout_2.addWidget(self.chkSimDisInputs)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tvDiscreteInputsData = QTableView(self.verticalLayoutWidget_2)
        self.tvDiscreteInputsData.setObjectName(u"tvDiscreteInputsData")
        self.tvDiscreteInputsData.setEnabled(True)
        self.tvDiscreteInputsData.setMinimumSize(QSize(450, 330))
        self.tvDiscreteInputsData.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.tvDiscreteInputsData)

        icon3 = QIcon()
        icon3.addFile(u":/img/DI.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabIOs.addTab(self.tabDiscreteInputs, icon3, "")
        self.tabHoldingRegisters = QWidget()
        self.tabHoldingRegisters.setObjectName(u"tabHoldingRegisters")
        self.verticalLayoutWidget_3 = QWidget(self.tabHoldingRegisters)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(6, 5, 452, 364))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pbResetAO = QPushButton(self.verticalLayoutWidget_3)
        self.pbResetAO.setObjectName(u"pbResetAO")
        self.pbResetAO.setMinimumSize(QSize(48, 0))
        self.pbResetAO.setMaximumSize(QSize(48, 16777215))
        self.pbResetAO.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pbResetAO)

        self.chkSimHoldRegs = QCheckBox(self.verticalLayoutWidget_3)
        self.chkSimHoldRegs.setObjectName(u"chkSimHoldRegs")

        self.horizontalLayout_3.addWidget(self.chkSimHoldRegs)

        self.cmbHoldRegsType = QComboBox(self.verticalLayoutWidget_3)
        self.cmbHoldRegsType.addItem("")
        self.cmbHoldRegsType.addItem("")
        self.cmbHoldRegsType.setObjectName(u"cmbHoldRegsType")
        self.cmbHoldRegsType.setMaxVisibleItems(2)

        self.horizontalLayout_3.addWidget(self.cmbHoldRegsType)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tvHoldingRegistersData = QTableView(self.verticalLayoutWidget_3)
        self.tvHoldingRegistersData.setObjectName(u"tvHoldingRegistersData")
        self.tvHoldingRegistersData.setMinimumSize(QSize(450, 330))

        self.verticalLayout_3.addWidget(self.tvHoldingRegistersData)

        icon4 = QIcon()
        icon4.addFile(u":/img/AO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabIOs.addTab(self.tabHoldingRegisters, icon4, "")
        self.tabInputRegisters = QWidget()
        self.tabInputRegisters.setObjectName(u"tabInputRegisters")
        self.verticalLayoutWidget_4 = QWidget(self.tabInputRegisters)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(6, 5, 452, 364))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pbResetAI = QPushButton(self.verticalLayoutWidget_4)
        self.pbResetAI.setObjectName(u"pbResetAI")
        self.pbResetAI.setMinimumSize(QSize(48, 0))
        self.pbResetAI.setMaximumSize(QSize(48, 16777215))
        self.pbResetAI.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.pbResetAI)

        self.chkSimInputRegs = QCheckBox(self.verticalLayoutWidget_4)
        self.chkSimInputRegs.setObjectName(u"chkSimInputRegs")

        self.horizontalLayout_4.addWidget(self.chkSimInputRegs)

        self.cmbInputRegsType = QComboBox(self.verticalLayoutWidget_4)
        self.cmbInputRegsType.addItem("")
        self.cmbInputRegsType.addItem("")
        self.cmbInputRegsType.setObjectName(u"cmbInputRegsType")
        self.cmbInputRegsType.setMaxVisibleItems(2)

        self.horizontalLayout_4.addWidget(self.cmbInputRegsType)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.tvInputRegistersData = QTableView(self.verticalLayoutWidget_4)
        self.tvInputRegistersData.setObjectName(u"tvInputRegistersData")
        self.tvInputRegistersData.setMinimumSize(QSize(450, 330))

        self.verticalLayout_4.addWidget(self.tvInputRegistersData)

        icon5 = QIcon()
        icon5.addFile(u":/img/AI.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabIOs.addTab(self.tabInputRegisters, icon5, "")
        MBData.setCentralWidget(self.centralwidget)

        self.retranslateUi(MBData)

        self.tabIOs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MBData)
    # setupUi

    def retranslateUi(self, MBData):
        MBData.setWindowTitle(QCoreApplication.translate("MBData", u"Data", None))
#if QT_CONFIG(tooltip)
        self.pbResetDO.setToolTip(QCoreApplication.translate("MBData", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.pbResetDO.setText("")
        self.chkSimCoils.setText(QCoreApplication.translate("MBData", u"Sim", None))
        self.tabIOs.setTabText(self.tabIOs.indexOf(self.tabCoils), QCoreApplication.translate("MBData", u"Coils", None))
#if QT_CONFIG(tooltip)
        self.pbResetDI.setToolTip(QCoreApplication.translate("MBData", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.pbResetDI.setText("")
        self.chkSimDisInputs.setText(QCoreApplication.translate("MBData", u"Sim", None))
        self.tabIOs.setTabText(self.tabIOs.indexOf(self.tabDiscreteInputs), QCoreApplication.translate("MBData", u"Discrete Inputs", None))
#if QT_CONFIG(tooltip)
        self.pbResetAO.setToolTip(QCoreApplication.translate("MBData", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.pbResetAO.setText("")
        self.chkSimHoldRegs.setText(QCoreApplication.translate("MBData", u"Sim", None))
        self.cmbHoldRegsType.setItemText(0, QCoreApplication.translate("MBData", u"Decimal", None))
        self.cmbHoldRegsType.setItemText(1, QCoreApplication.translate("MBData", u"Hex", None))

        self.tabIOs.setTabText(self.tabIOs.indexOf(self.tabHoldingRegisters), QCoreApplication.translate("MBData", u"Holding Registers", None))
#if QT_CONFIG(tooltip)
        self.pbResetAI.setToolTip(QCoreApplication.translate("MBData", u"Reset", None))
#endif // QT_CONFIG(tooltip)
        self.pbResetAI.setText("")
        self.chkSimInputRegs.setText(QCoreApplication.translate("MBData", u"Sim", None))
        self.cmbInputRegsType.setItemText(0, QCoreApplication.translate("MBData", u"Decimal", None))
        self.cmbInputRegsType.setItemText(1, QCoreApplication.translate("MBData", u"Hex", None))

        self.tabIOs.setTabText(self.tabIOs.indexOf(self.tabInputRegisters), QCoreApplication.translate("MBData", u"Input Registers", None))
    # retranslateUi

