# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsmodbustcp.ui'
#
# Created: Mon Apr 29 12:28:19 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsModbusTCP(object):
    def setupUi(self, SettingsModbusTCP):
        SettingsModbusTCP.setObjectName(_fromUtf8("SettingsModbusTCP"))
        SettingsModbusTCP.resize(180, 90)
        SettingsModbusTCP.setMinimumSize(QtCore.QSize(180, 90))
        SettingsModbusTCP.setMaximumSize(QtCore.QSize(180, 90))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/network-16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsModbusTCP.setWindowIcon(icon)
        SettingsModbusTCP.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(SettingsModbusTCP)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leTCPPort = QtGui.QLineEdit(SettingsModbusTCP)
        self.leTCPPort.setObjectName(_fromUtf8("leTCPPort"))
        self.gridLayout.addWidget(self.leTCPPort, 1, 1, 1, 1)
        self.lblTCPPort = QtGui.QLabel(SettingsModbusTCP)
        self.lblTCPPort.setObjectName(_fromUtf8("lblTCPPort"))
        self.gridLayout.addWidget(self.lblTCPPort, 1, 0, 1, 1)
        self.lblIP = QtGui.QLabel(SettingsModbusTCP)
        self.lblIP.setObjectName(_fromUtf8("lblIP"))
        self.gridLayout.addWidget(self.lblIP, 0, 0, 1, 1)
        self.leIP = QtGui.QLineEdit(SettingsModbusTCP)
        self.leIP.setObjectName(_fromUtf8("leIP"))
        self.gridLayout.addWidget(self.leIP, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsModbusTCP)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.lblTCPPort.setBuddy(self.leTCPPort)

        self.retranslateUi(SettingsModbusTCP)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsModbusTCP.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsModbusTCP.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsModbusTCP)

    def retranslateUi(self, SettingsModbusTCP):
        SettingsModbusTCP.setWindowTitle(QtGui.QApplication.translate("SettingsModbusTCP", "Modbus TCP Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.leTCPPort.setText(QtGui.QApplication.translate("SettingsModbusTCP", "502", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTCPPort.setText(QtGui.QApplication.translate("SettingsModbusTCP", "TCP Port", None, QtGui.QApplication.UnicodeUTF8))
        self.lblIP.setText(QtGui.QApplication.translate("SettingsModbusTCP", "IP", None, QtGui.QApplication.UnicodeUTF8))
        self.leIP.setInputMask(QtGui.QApplication.translate("SettingsModbusTCP", "999.999.999.999;_", None, QtGui.QApplication.UnicodeUTF8))

import pyModSlaveQt_rc
