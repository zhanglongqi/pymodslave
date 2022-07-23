# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QToolBar, QVBoxLayout, QWidget)
import pyModSlaveQt_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(384, 222)
        MainWindow.setMinimumSize(QSize(360, 170))
        icon = QIcon()
        icon.addFile(u":/img/Bus.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/img/close16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionSerial_RTU = QAction(MainWindow)
        self.actionSerial_RTU.setObjectName(u"actionSerial_RTU")
        icon2 = QIcon()
        icon2.addFile(u":/img/edit-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSerial_RTU.setIcon(icon2)
        self.actionSerial_RTU.setIconVisibleInMenu(True)
        self.actionTCP = QAction(MainWindow)
        self.actionTCP.setObjectName(u"actionTCP")
        icon3 = QIcon()
        icon3.addFile(u":/img/network-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTCP.setIcon(icon3)
        self.actionTCP.setIconVisibleInMenu(True)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon4 = QIcon()
        icon4.addFile(u":/img/info16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        icon5 = QIcon()
        icon5.addFile(u":/img/options-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon5)
        self.actionSettings.setIconVisibleInMenu(True)
        self.actionCoils = QAction(MainWindow)
        self.actionCoils.setObjectName(u"actionCoils")
        icon6 = QIcon()
        icon6.addFile(u":/img/DO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCoils.setIcon(icon6)
        self.actionDigital_Inputs = QAction(MainWindow)
        self.actionDigital_Inputs.setObjectName(u"actionDigital_Inputs")
        icon7 = QIcon()
        icon7.addFile(u":/img/DI.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDigital_Inputs.setIcon(icon7)
        self.actionHolding_Registers = QAction(MainWindow)
        self.actionHolding_Registers.setObjectName(u"actionHolding_Registers")
        icon8 = QIcon()
        icon8.addFile(u":/img/AO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHolding_Registers.setIcon(icon8)
        self.actionAnalog_Inputs = QAction(MainWindow)
        self.actionAnalog_Inputs.setObjectName(u"actionAnalog_Inputs")
        icon9 = QIcon()
        icon9.addFile(u":/img/AI.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAnalog_Inputs.setIcon(icon9)
        self.actionIO_Data = QAction(MainWindow)
        self.actionIO_Data.setObjectName(u"actionIO_Data")
        icon10 = QIcon()
        icon10.addFile(u":/img/IO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionIO_Data.setIcon(icon10)
        self.actionBus_Monitor = QAction(MainWindow)
        self.actionBus_Monitor.setObjectName(u"actionBus_Monitor")
        icon11 = QIcon()
        icon11.addFile(u":/img/view-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBus_Monitor.setIcon(icon11)
        self.actionReset_Counters = QAction(MainWindow)
        self.actionReset_Counters.setObjectName(u"actionReset_Counters")
        icon12 = QIcon()
        icon12.addFile(u":/img/trash-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReset_Counters.setIcon(icon12)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_settings = QFrame(self.centralWidget)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setMinimumSize(QSize(340, 40))
        self.frame_settings.setMaximumSize(QSize(340, 40))
        self.frame_settings.setFrameShape(QFrame.Box)
        self.frame_settings.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame_settings)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblModbusMode = QLabel(self.frame_settings)
        self.lblModbusMode.setObjectName(u"lblModbusMode")
        self.lblModbusMode.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.lblModbusMode)

        self.cmbModbusMode = QComboBox(self.frame_settings)
        self.cmbModbusMode.addItem("")
        self.cmbModbusMode.addItem("")
        self.cmbModbusMode.setObjectName(u"cmbModbusMode")
        self.cmbModbusMode.setMinimumSize(QSize(0, 24))

        self.horizontalLayout.addWidget(self.cmbModbusMode)

        self.lblSlaveID = QLabel(self.frame_settings)
        self.lblSlaveID.setObjectName(u"lblSlaveID")

        self.horizontalLayout.addWidget(self.lblSlaveID)

        self.sbSlaveID = QSpinBox(self.frame_settings)
        self.sbSlaveID.setObjectName(u"sbSlaveID")
        self.sbSlaveID.setMinimumSize(QSize(0, 24))
        self.sbSlaveID.setMinimum(1)
        self.sbSlaveID.setMaximum(255)

        self.horizontalLayout.addWidget(self.sbSlaveID)

        self.horizontalSpacer_1 = QSpacerItem(31, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_1)


        self.verticalLayout.addWidget(self.frame_settings)

        self.frame_commands = QFrame(self.centralWidget)
        self.frame_commands.setObjectName(u"frame_commands")
        self.frame_commands.setMinimumSize(QSize(340, 40))
        self.frame_commands.setMaximumSize(QSize(340, 40))
        self.frame_commands.setFrameShape(QFrame.Box)
        self.frame_commands.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_commands)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btStartStop = QPushButton(self.frame_commands)
        self.btStartStop.setObjectName(u"btStartStop")
        self.btStartStop.setMinimumSize(QSize(0, 24))
        icon13 = QIcon()
        icon13.addFile(u":/img/run-16.png", QSize(), QIcon.Normal, QIcon.Off)
        icon13.addFile(u":/img/stop-16.png", QSize(), QIcon.Normal, QIcon.On)
        self.btStartStop.setIcon(icon13)
        self.btStartStop.setIconSize(QSize(16, 16))
        self.btStartStop.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btStartStop)

        self.lblSimCycle = QLabel(self.frame_commands)
        self.lblSimCycle.setObjectName(u"lblSimCycle")

        self.horizontalLayout_2.addWidget(self.lblSimCycle)

        self.spInterval = QSpinBox(self.frame_commands)
        self.spInterval.setObjectName(u"spInterval")
        self.spInterval.setMinimumSize(QSize(0, 24))
        self.spInterval.setMinimum(1000)
        self.spInterval.setMaximum(10000)
        self.spInterval.setSingleStep(500)
        self.spInterval.setValue(5000)

        self.horizontalLayout_2.addWidget(self.spInterval)

        self.horizontalSpacer_2 = QSpacerItem(26, 9, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_commands)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 384, 24))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOptions = QMenu(self.menuBar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuData = QMenu(self.menuBar)
        self.menuData.setObjectName(u"menuData")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
#if QT_CONFIG(shortcut)
        self.lblModbusMode.setBuddy(self.cmbModbusMode)
        self.lblSlaveID.setBuddy(self.sbSlaveID)
#endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuData.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
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

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Modbus Slave", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSerial_RTU.setText(QCoreApplication.translate("MainWindow", u"Modbus RTU...", None))
        self.actionTCP.setText(QCoreApplication.translate("MainWindow", u"Modbus TCP...", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings...", None))
        self.actionCoils.setText(QCoreApplication.translate("MainWindow", u"Coils", None))
        self.actionDigital_Inputs.setText(QCoreApplication.translate("MainWindow", u"Digital Inputs", None))
        self.actionHolding_Registers.setText(QCoreApplication.translate("MainWindow", u"Holding Registers", None))
        self.actionAnalog_Inputs.setText(QCoreApplication.translate("MainWindow", u"Analog Inputs", None))
        self.actionIO_Data.setText(QCoreApplication.translate("MainWindow", u"IO Data", None))
        self.actionBus_Monitor.setText(QCoreApplication.translate("MainWindow", u"Bus Monitor", None))
        self.actionReset_Counters.setText(QCoreApplication.translate("MainWindow", u"Reset Counters", None))
        self.lblModbusMode.setText(QCoreApplication.translate("MainWindow", u"Modbus Mode", None))
        self.cmbModbusMode.setItemText(0, QCoreApplication.translate("MainWindow", u"RTU", None))
        self.cmbModbusMode.setItemText(1, QCoreApplication.translate("MainWindow", u"TCP", None))

        self.lblSlaveID.setText(QCoreApplication.translate("MainWindow", u"Slave ID", None))
#if QT_CONFIG(tooltip)
        self.btStartStop.setToolTip(QCoreApplication.translate("MainWindow", u"Start-Stop", None))
#endif // QT_CONFIG(tooltip)
        self.btStartStop.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lblSimCycle.setText(QCoreApplication.translate("MainWindow", u"Simulate Every (msec)", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuData.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
    # retranslateUi

