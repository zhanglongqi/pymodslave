# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'busmonitor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import pyModSlaveQt_rc

class Ui_BusMonitor(object):
    def setupUi(self, BusMonitor):
        if not BusMonitor.objectName():
            BusMonitor.setObjectName(u"BusMonitor")
        BusMonitor.setWindowModality(Qt.NonModal)
        BusMonitor.resize(450, 450)
        BusMonitor.setMinimumSize(QSize(450, 450))
        BusMonitor.setMaximumSize(QSize(450, 450))
        icon = QIcon()
        icon.addFile(u":/img/view-16.png", QSize(), QIcon.Normal, QIcon.Off)
        BusMonitor.setWindowIcon(icon)
        self.actionClear = QAction(BusMonitor)
        self.actionClear.setObjectName(u"actionClear")
        icon1 = QIcon()
        icon1.addFile(u":/img/remove-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClear.setIcon(icon1)
        self.actionClear.setIconVisibleInMenu(True)
        self.actionExit = QAction(BusMonitor)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        icon2.addFile(u":/img/close16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionSave = QAction(BusMonitor)
        self.actionSave.setObjectName(u"actionSave")
        icon3 = QIcon()
        icon3.addFile(u":/img/save-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionStart_Stop = QAction(BusMonitor)
        self.actionStart_Stop.setObjectName(u"actionStart_Stop")
        self.actionStart_Stop.setCheckable(True)
        icon4 = QIcon()
        icon4.addFile(u":/img/run-16.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/img/stop-16.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionStart_Stop.setIcon(icon4)
        self.centralwidget = QWidget(BusMonitor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(450, 400))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblRawData = QLabel(self.centralwidget)
        self.lblRawData.setObjectName(u"lblRawData")
        font = QFont()
        font.setBold(True)
        self.lblRawData.setFont(font)

        self.verticalLayout_2.addWidget(self.lblRawData)

        self.lstRawData = QListView(self.centralwidget)
        self.lstRawData.setObjectName(u"lstRawData")
        self.lstRawData.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(8)
        self.lstRawData.setFont(font1)
        self.lstRawData.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lstRawData.setAlternatingRowColors(True)
        self.lstRawData.setSelectionMode(QAbstractItemView.SingleSelection)
        self.lstRawData.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lstRawData.setSelectionRectVisible(False)

        self.verticalLayout_2.addWidget(self.lstRawData)

        self.lblPDU = QLabel(self.centralwidget)
        self.lblPDU.setObjectName(u"lblPDU")
        self.lblPDU.setFont(font)

        self.verticalLayout_2.addWidget(self.lblPDU)

        self.txtPDU = QPlainTextEdit(self.centralwidget)
        self.txtPDU.setObjectName(u"txtPDU")
        self.txtPDU.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.txtPDU)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        BusMonitor.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(BusMonitor)
        self.toolBar.setObjectName(u"toolBar")
        BusMonitor.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(BusMonitor)

        QMetaObject.connectSlotsByName(BusMonitor)
    # setupUi

    def retranslateUi(self, BusMonitor):
        BusMonitor.setWindowTitle(QCoreApplication.translate("BusMonitor", u"Bus Monitor", None))
        self.actionClear.setText(QCoreApplication.translate("BusMonitor", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.actionClear.setToolTip(QCoreApplication.translate("BusMonitor", u"Clear", None))
#endif // QT_CONFIG(tooltip)
        self.actionExit.setText(QCoreApplication.translate("BusMonitor", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(QCoreApplication.translate("BusMonitor", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave.setText(QCoreApplication.translate("BusMonitor", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("BusMonitor", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.actionStart_Stop.setText(QCoreApplication.translate("BusMonitor", u"Start-Stop", None))
#if QT_CONFIG(tooltip)
        self.actionStart_Stop.setToolTip(QCoreApplication.translate("BusMonitor", u"Start-Stop Monitor", None))
#endif // QT_CONFIG(tooltip)
        self.lblRawData.setText(QCoreApplication.translate("BusMonitor", u"Raw Data", None))
        self.lblPDU.setText(QCoreApplication.translate("BusMonitor", u"PDU", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("BusMonitor", u"toolBar", None))
    # retranslateUi

