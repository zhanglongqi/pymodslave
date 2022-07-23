# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsmodbustcp.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import pyModSlaveQt_rc

class Ui_SettingsModbusTCP(object):
    def setupUi(self, SettingsModbusTCP):
        if not SettingsModbusTCP.objectName():
            SettingsModbusTCP.setObjectName(u"SettingsModbusTCP")
        SettingsModbusTCP.resize(180, 90)
        SettingsModbusTCP.setMinimumSize(QSize(180, 90))
        SettingsModbusTCP.setMaximumSize(QSize(180, 90))
        icon = QIcon()
        icon.addFile(u":/img/network-16.png", QSize(), QIcon.Normal, QIcon.Off)
        SettingsModbusTCP.setWindowIcon(icon)
        SettingsModbusTCP.setModal(True)
        self.verticalLayout = QVBoxLayout(SettingsModbusTCP)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.leTCPPort = QLineEdit(SettingsModbusTCP)
        self.leTCPPort.setObjectName(u"leTCPPort")

        self.gridLayout.addWidget(self.leTCPPort, 1, 1, 1, 1)

        self.lblTCPPort = QLabel(SettingsModbusTCP)
        self.lblTCPPort.setObjectName(u"lblTCPPort")

        self.gridLayout.addWidget(self.lblTCPPort, 1, 0, 1, 1)

        self.lblIP = QLabel(SettingsModbusTCP)
        self.lblIP.setObjectName(u"lblIP")

        self.gridLayout.addWidget(self.lblIP, 0, 0, 1, 1)

        self.leIP = QLineEdit(SettingsModbusTCP)
        self.leIP.setObjectName(u"leIP")

        self.gridLayout.addWidget(self.leIP, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(SettingsModbusTCP)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.lblTCPPort.setBuddy(self.leTCPPort)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(SettingsModbusTCP)
        self.buttonBox.accepted.connect(SettingsModbusTCP.accept)
        self.buttonBox.rejected.connect(SettingsModbusTCP.reject)

        QMetaObject.connectSlotsByName(SettingsModbusTCP)
    # setupUi

    def retranslateUi(self, SettingsModbusTCP):
        SettingsModbusTCP.setWindowTitle(QCoreApplication.translate("SettingsModbusTCP", u"Modbus TCP Settings", None))
        self.leTCPPort.setText(QCoreApplication.translate("SettingsModbusTCP", u"502", None))
        self.lblTCPPort.setText(QCoreApplication.translate("SettingsModbusTCP", u"TCP Port", None))
        self.lblIP.setText(QCoreApplication.translate("SettingsModbusTCP", u"IP", None))
        self.leIP.setInputMask(QCoreApplication.translate("SettingsModbusTCP", u"999.999.999.999;_", None))
    # retranslateUi

