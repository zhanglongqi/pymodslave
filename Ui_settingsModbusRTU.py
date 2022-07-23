# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsmodbusrtu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import pyModSlaveQt_rc

class Ui_SettingsModbusRTU(object):
    def setupUi(self, SettingsModbusRTU):
        if not SettingsModbusRTU.objectName():
            SettingsModbusRTU.setObjectName(u"SettingsModbusRTU")
        SettingsModbusRTU.resize(240, 240)
        SettingsModbusRTU.setMinimumSize(QSize(180, 180))
        SettingsModbusRTU.setMaximumSize(QSize(240, 240))
        icon = QIcon()
        icon.addFile(u":/img/options-16.png", QSize(), QIcon.Normal, QIcon.Off)
        SettingsModbusRTU.setWindowIcon(icon)
        SettingsModbusRTU.setModal(True)
        self.verticalLayout = QVBoxLayout(SettingsModbusRTU)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblPort = QLabel(SettingsModbusRTU)
        self.lblPort.setObjectName(u"lblPort")
        self.lblPort.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.lblPort, 0, 0, 1, 1)

        self.cmbPort = QComboBox(SettingsModbusRTU)
        self.cmbPort.addItem("")
        self.cmbPort.addItem("")
        self.cmbPort.addItem("")
        self.cmbPort.addItem("")
        self.cmbPort.setObjectName(u"cmbPort")
        self.cmbPort.setEditable(True)

        self.gridLayout.addWidget(self.cmbPort, 0, 1, 1, 1)

        self.cmbBaud = QComboBox(SettingsModbusRTU)
        self.cmbBaud.addItem("")
        self.cmbBaud.addItem("")
        self.cmbBaud.addItem("")
        self.cmbBaud.addItem("")
        self.cmbBaud.addItem("")
        self.cmbBaud.addItem("")
        self.cmbBaud.addItem("")
        self.cmbBaud.addItem("")
        self.cmbBaud.setObjectName(u"cmbBaud")

        self.gridLayout.addWidget(self.cmbBaud, 1, 1, 1, 1)

        self.lblBaud = QLabel(SettingsModbusRTU)
        self.lblBaud.setObjectName(u"lblBaud")

        self.gridLayout.addWidget(self.lblBaud, 1, 0, 1, 1)

        self.lblDataBits = QLabel(SettingsModbusRTU)
        self.lblDataBits.setObjectName(u"lblDataBits")

        self.gridLayout.addWidget(self.lblDataBits, 2, 0, 1, 1)

        self.cmbDataBits = QComboBox(SettingsModbusRTU)
        self.cmbDataBits.addItem("")
        self.cmbDataBits.addItem("")
        self.cmbDataBits.setObjectName(u"cmbDataBits")

        self.gridLayout.addWidget(self.cmbDataBits, 2, 1, 1, 1)

        self.lblStopBits = QLabel(SettingsModbusRTU)
        self.lblStopBits.setObjectName(u"lblStopBits")

        self.gridLayout.addWidget(self.lblStopBits, 3, 0, 1, 1)

        self.cmbStopBits = QComboBox(SettingsModbusRTU)
        self.cmbStopBits.addItem("")
        self.cmbStopBits.addItem("")
        self.cmbStopBits.addItem("")
        self.cmbStopBits.setObjectName(u"cmbStopBits")

        self.gridLayout.addWidget(self.cmbStopBits, 3, 1, 1, 1)

        self.lblParity = QLabel(SettingsModbusRTU)
        self.lblParity.setObjectName(u"lblParity")

        self.gridLayout.addWidget(self.lblParity, 4, 0, 1, 1)

        self.cmbParity = QComboBox(SettingsModbusRTU)
        self.cmbParity.addItem("")
        self.cmbParity.addItem("")
        self.cmbParity.addItem("")
        self.cmbParity.setObjectName(u"cmbParity")

        self.gridLayout.addWidget(self.cmbParity, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(SettingsModbusRTU)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.lblPort.setBuddy(self.cmbPort)
        self.lblBaud.setBuddy(self.cmbBaud)
        self.lblDataBits.setBuddy(self.cmbDataBits)
        self.lblStopBits.setBuddy(self.cmbStopBits)
        self.lblParity.setBuddy(self.cmbParity)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(SettingsModbusRTU)
        self.buttonBox.accepted.connect(SettingsModbusRTU.accept)
        self.buttonBox.rejected.connect(SettingsModbusRTU.reject)

        self.cmbBaud.setCurrentIndex(4)
        self.cmbDataBits.setCurrentIndex(1)
        self.cmbStopBits.setCurrentIndex(0)
        self.cmbParity.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsModbusRTU)
    # setupUi

    def retranslateUi(self, SettingsModbusRTU):
        SettingsModbusRTU.setWindowTitle(QCoreApplication.translate("SettingsModbusRTU", u"Modbus RTU Settings", None))
        self.lblPort.setText(QCoreApplication.translate("SettingsModbusRTU", u"Serial port", None))
        self.cmbPort.setItemText(0, QCoreApplication.translate("SettingsModbusRTU", u"1", None))
        self.cmbPort.setItemText(1, QCoreApplication.translate("SettingsModbusRTU", u"2", None))
        self.cmbPort.setItemText(2, QCoreApplication.translate("SettingsModbusRTU", u"3", None))
        self.cmbPort.setItemText(3, QCoreApplication.translate("SettingsModbusRTU", u"4", None))

        self.cmbBaud.setItemText(0, QCoreApplication.translate("SettingsModbusRTU", u"1200", None))
        self.cmbBaud.setItemText(1, QCoreApplication.translate("SettingsModbusRTU", u"2400", None))
        self.cmbBaud.setItemText(2, QCoreApplication.translate("SettingsModbusRTU", u"4800", None))
        self.cmbBaud.setItemText(3, QCoreApplication.translate("SettingsModbusRTU", u"9600", None))
        self.cmbBaud.setItemText(4, QCoreApplication.translate("SettingsModbusRTU", u"19200", None))
        self.cmbBaud.setItemText(5, QCoreApplication.translate("SettingsModbusRTU", u"38400", None))
        self.cmbBaud.setItemText(6, QCoreApplication.translate("SettingsModbusRTU", u"57600", None))
        self.cmbBaud.setItemText(7, QCoreApplication.translate("SettingsModbusRTU", u"115200", None))

        self.lblBaud.setText(QCoreApplication.translate("SettingsModbusRTU", u"Baud", None))
        self.lblDataBits.setText(QCoreApplication.translate("SettingsModbusRTU", u"Data Bits", None))
        self.cmbDataBits.setItemText(0, QCoreApplication.translate("SettingsModbusRTU", u"7", None))
        self.cmbDataBits.setItemText(1, QCoreApplication.translate("SettingsModbusRTU", u"8", None))

        self.lblStopBits.setText(QCoreApplication.translate("SettingsModbusRTU", u"Stop Bits", None))
        self.cmbStopBits.setItemText(0, QCoreApplication.translate("SettingsModbusRTU", u"1", None))
        self.cmbStopBits.setItemText(1, QCoreApplication.translate("SettingsModbusRTU", u"1.5", None))
        self.cmbStopBits.setItemText(2, QCoreApplication.translate("SettingsModbusRTU", u"2", None))

        self.lblParity.setText(QCoreApplication.translate("SettingsModbusRTU", u"Parity", None))
        self.cmbParity.setItemText(0, QCoreApplication.translate("SettingsModbusRTU", u"None", None))
        self.cmbParity.setItemText(1, QCoreApplication.translate("SettingsModbusRTU", u"Odd", None))
        self.cmbParity.setItemText(2, QCoreApplication.translate("SettingsModbusRTU", u"Even", None))

    # retranslateUi

