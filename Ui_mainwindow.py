# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Jul 04 16:29:29 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(360, 170)
        MainWindow.setMinimumSize(QtCore.QSize(360, 170))
        MainWindow.setMaximumSize(QtCore.QSize(360, 170))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/Bus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_settings = QtGui.QFrame(self.centralWidget)
        self.frame_settings.setMinimumSize(QtCore.QSize(340, 40))
        self.frame_settings.setMaximumSize(QtCore.QSize(340, 40))
        self.frame_settings.setFrameShape(QtGui.QFrame.Box)
        self.frame_settings.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_settings.setObjectName(_fromUtf8("frame_settings"))
        self.layoutWidget = QtGui.QWidget(self.frame_settings)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 6, 325, 26))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayoutSettings = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayoutSettings.setContentsMargins(0, 0, -1, -1)
        self.gridLayoutSettings.setObjectName(_fromUtf8("gridLayoutSettings"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayoutSettings.addItem(spacerItem, 0, 4, 1, 1)
        self.lblSlaveID = QtGui.QLabel(self.layoutWidget)
        self.lblSlaveID.setObjectName(_fromUtf8("lblSlaveID"))
        self.gridLayoutSettings.addWidget(self.lblSlaveID, 0, 2, 1, 1)
        self.sbSlaveID = QtGui.QSpinBox(self.layoutWidget)
        self.sbSlaveID.setMinimumSize(QtCore.QSize(0, 24))
        self.sbSlaveID.setMinimum(1)
        self.sbSlaveID.setMaximum(255)
        self.sbSlaveID.setObjectName(_fromUtf8("sbSlaveID"))
        self.gridLayoutSettings.addWidget(self.sbSlaveID, 0, 3, 1, 1)
        self.cmbModbusMode = QtGui.QComboBox(self.layoutWidget)
        self.cmbModbusMode.setMinimumSize(QtCore.QSize(0, 24))
        self.cmbModbusMode.setObjectName(_fromUtf8("cmbModbusMode"))
        self.cmbModbusMode.addItem(_fromUtf8(""))
        self.cmbModbusMode.addItem(_fromUtf8(""))
        self.gridLayoutSettings.addWidget(self.cmbModbusMode, 0, 1, 1, 1)
        self.lblModbusMode = QtGui.QLabel(self.layoutWidget)
        self.lblModbusMode.setObjectName(_fromUtf8("lblModbusMode"))
        self.gridLayoutSettings.addWidget(self.lblModbusMode, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_settings)
        self.frame_commands = QtGui.QFrame(self.centralWidget)
        self.frame_commands.setMinimumSize(QtCore.QSize(340, 40))
        self.frame_commands.setMaximumSize(QtCore.QSize(340, 40))
        self.frame_commands.setFrameShape(QtGui.QFrame.Box)
        self.frame_commands.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_commands.setObjectName(_fromUtf8("frame_commands"))
        self.layoutWidget1 = QtGui.QWidget(self.frame_commands)
        self.layoutWidget1.setGeometry(QtCore.QRect(5, 6, 326, 26))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayoutCmds = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayoutCmds.setMargin(0)
        self.gridLayoutCmds.setObjectName(_fromUtf8("gridLayoutCmds"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayoutCmds.addItem(spacerItem1, 0, 3, 1, 1)
        self.btStartStop = QtGui.QPushButton(self.layoutWidget1)
        self.btStartStop.setMinimumSize(QtCore.QSize(0, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/run-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/stop-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btStartStop.setIcon(icon1)
        self.btStartStop.setIconSize(QtCore.QSize(16, 16))
        self.btStartStop.setCheckable(True)
        self.btStartStop.setObjectName(_fromUtf8("btStartStop"))
        self.gridLayoutCmds.addWidget(self.btStartStop, 0, 0, 1, 1)
        self.spInterval = QtGui.QSpinBox(self.layoutWidget1)
        self.spInterval.setMinimumSize(QtCore.QSize(0, 24))
        self.spInterval.setMinimum(1000)
        self.spInterval.setMaximum(10000)
        self.spInterval.setSingleStep(500)
        self.spInterval.setProperty("value", 5000)
        self.spInterval.setObjectName(_fromUtf8("spInterval"))
        self.gridLayoutCmds.addWidget(self.spInterval, 0, 2, 1, 1)
        self.lblSimCycle = QtGui.QLabel(self.layoutWidget1)
        self.lblSimCycle.setObjectName(_fromUtf8("lblSimCycle"))
        self.gridLayoutCmds.addWidget(self.lblSimCycle, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_commands)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menuBar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuData = QtGui.QMenu(self.menuBar)
        self.menuData.setObjectName(_fromUtf8("menuData"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/close16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSerial_RTU = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/edit-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSerial_RTU.setIcon(icon3)
        self.actionSerial_RTU.setIconVisibleInMenu(True)
        self.actionSerial_RTU.setObjectName(_fromUtf8("actionSerial_RTU"))
        self.actionTCP = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/network-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTCP.setIcon(icon4)
        self.actionTCP.setIconVisibleInMenu(True)
        self.actionTCP.setObjectName(_fromUtf8("actionTCP"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/info16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSettings = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/options-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon6)
        self.actionSettings.setIconVisibleInMenu(True)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionCoils = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/DO.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCoils.setIcon(icon7)
        self.actionCoils.setObjectName(_fromUtf8("actionCoils"))
        self.actionDigital_Inputs = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/DI.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDigital_Inputs.setIcon(icon8)
        self.actionDigital_Inputs.setObjectName(_fromUtf8("actionDigital_Inputs"))
        self.actionHolding_Registers = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/AO.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHolding_Registers.setIcon(icon9)
        self.actionHolding_Registers.setObjectName(_fromUtf8("actionHolding_Registers"))
        self.actionAnalog_Inputs = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/AI.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnalog_Inputs.setIcon(icon10)
        self.actionAnalog_Inputs.setObjectName(_fromUtf8("actionAnalog_Inputs"))
        self.actionIO_Data = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/IO.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIO_Data.setIcon(icon11)
        self.actionIO_Data.setObjectName(_fromUtf8("actionIO_Data"))
        self.actionBus_Monitor = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/view-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBus_Monitor.setIcon(icon12)
        self.actionBus_Monitor.setObjectName(_fromUtf8("actionBus_Monitor"))
        self.actionReset_Counters = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/trash-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_Counters.setIcon(icon13)
        self.actionReset_Counters.setObjectName(_fromUtf8("actionReset_Counters"))
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionSerial_RTU)
        self.menuOptions.addAction(self.actionTCP)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)
        self.menuData.addAction(self.actionIO_Data)
        self.menuData.addAction(self.actionBus_Monitor)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionReset_Counters)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuData.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.lblSlaveID.setBuddy(self.sbSlaveID)
        self.lblModbusMode.setBuddy(self.cmbModbusMode)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Modbus Slave", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSlaveID.setText(QtGui.QApplication.translate("MainWindow", "Slave ID", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbModbusMode.setItemText(0, QtGui.QApplication.translate("MainWindow", "RTU", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbModbusMode.setItemText(1, QtGui.QApplication.translate("MainWindow", "TCP", None, QtGui.QApplication.UnicodeUTF8))
        self.lblModbusMode.setText(QtGui.QApplication.translate("MainWindow", "Modbus Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.btStartStop.setToolTip(QtGui.QApplication.translate("MainWindow", "Start-Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.btStartStop.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSimCycle.setText(QtGui.QApplication.translate("MainWindow", "Simulate Every (msec)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData.setTitle(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSerial_RTU.setText(QtGui.QApplication.translate("MainWindow", "Modbus RTU...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTCP.setText(QtGui.QApplication.translate("MainWindow", "Modbus TCP...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCoils.setText(QtGui.QApplication.translate("MainWindow", "Coils", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDigital_Inputs.setText(QtGui.QApplication.translate("MainWindow", "Digital Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHolding_Registers.setText(QtGui.QApplication.translate("MainWindow", "Holding Registers", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalog_Inputs.setText(QtGui.QApplication.translate("MainWindow", "Analog Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIO_Data.setText(QtGui.QApplication.translate("MainWindow", "IO Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBus_Monitor.setText(QtGui.QApplication.translate("MainWindow", "Bus Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset_Counters.setText(QtGui.QApplication.translate("MainWindow", "Reset Counters", None, QtGui.QApplication.UnicodeUTF8))

import pyModSlaveQt_rc
