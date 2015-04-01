# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'busmonitor.ui'
#
# Created: Tue Jul 23 13:23:43 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BusMonitor(object):
    def setupUi(self, BusMonitor):
        BusMonitor.setObjectName(_fromUtf8("BusMonitor"))
        BusMonitor.setWindowModality(QtCore.Qt.NonModal)
        BusMonitor.resize(450, 450)
        BusMonitor.setMinimumSize(QtCore.QSize(450, 450))
        BusMonitor.setMaximumSize(QtCore.QSize(450, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/view-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BusMonitor.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(BusMonitor)
        self.centralwidget.setMinimumSize(QtCore.QSize(450, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lblRawData = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblRawData.setFont(font)
        self.lblRawData.setObjectName(_fromUtf8("lblRawData"))
        self.verticalLayout_2.addWidget(self.lblRawData)
        self.lstRawData = QtGui.QListView(self.centralwidget)
        self.lstRawData.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lstRawData.setFont(font)
        self.lstRawData.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lstRawData.setAlternatingRowColors(True)
        self.lstRawData.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lstRawData.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.lstRawData.setSelectionRectVisible(False)
        self.lstRawData.setObjectName(_fromUtf8("lstRawData"))
        self.verticalLayout_2.addWidget(self.lstRawData)
        self.lblPDU = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPDU.setFont(font)
        self.lblPDU.setObjectName(_fromUtf8("lblPDU"))
        self.verticalLayout_2.addWidget(self.lblPDU)
        self.txtPDU = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtPDU.setReadOnly(True)
        self.txtPDU.setObjectName(_fromUtf8("txtPDU"))
        self.verticalLayout_2.addWidget(self.txtPDU)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        BusMonitor.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(BusMonitor)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        BusMonitor.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClear = QtGui.QAction(BusMonitor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/remove-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon1)
        self.actionClear.setIconVisibleInMenu(True)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionExit = QtGui.QAction(BusMonitor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/close16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave = QtGui.QAction(BusMonitor)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/save-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionStart_Stop = QtGui.QAction(BusMonitor)
        self.actionStart_Stop.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/run-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/stop-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionStart_Stop.setIcon(icon4)
        self.actionStart_Stop.setObjectName(_fromUtf8("actionStart_Stop"))

        self.retranslateUi(BusMonitor)
        QtCore.QMetaObject.connectSlotsByName(BusMonitor)

    def retranslateUi(self, BusMonitor):
        BusMonitor.setWindowTitle(QtGui.QApplication.translate("BusMonitor", "Bus Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRawData.setText(QtGui.QApplication.translate("BusMonitor", "Raw Data", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPDU.setText(QtGui.QApplication.translate("BusMonitor", "PDU", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("BusMonitor", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("BusMonitor", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setToolTip(QtGui.QApplication.translate("BusMonitor", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("BusMonitor", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setToolTip(QtGui.QApplication.translate("BusMonitor", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("BusMonitor", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setToolTip(QtGui.QApplication.translate("BusMonitor", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_Stop.setText(QtGui.QApplication.translate("BusMonitor", "Start-Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_Stop.setToolTip(QtGui.QApplication.translate("BusMonitor", "Start-Stop Monitor", None, QtGui.QApplication.UnicodeUTF8))

import pyModSlaveQt_rc
