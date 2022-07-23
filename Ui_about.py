# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import pyModSlaveQt_rc

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(400, 80)
        About.setMaximumSize(QSize(400, 80))
        icon = QIcon()
        icon.addFile(u":/img/info16.png", QSize(), QIcon.Normal, QIcon.Off)
        About.setWindowIcon(icon)
        About.setModal(True)
        self.verticalLayout = QVBoxLayout(About)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblVersion = QLabel(About)
        self.lblVersion.setObjectName(u"lblVersion")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lblVersion.setFont(font)
        self.lblVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblVersion)

        self.lblURL = QLabel(About)
        self.lblURL.setObjectName(u"lblURL")
        font1 = QFont()
        font1.setBold(True)
        self.lblURL.setFont(font1)
        self.lblURL.setAlignment(Qt.AlignCenter)
        self.lblURL.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.lblURL)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About", None))
        self.lblVersion.setText(QCoreApplication.translate("About", u"pyModSlave", None))
        self.lblURL.setText(QCoreApplication.translate("About", u"http://", None))
    # retranslateUi

