#-------------------------------------------------------------------------------
# Name:        ModSlaveAbout
# Purpose:
#
# Author:      ElBar
#
# Created:     17/04/2012
# Copyright:   (c) ElBar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PySide6 import QtGui, QtCore, QtWidgets
from Ui_about import Ui_About

_VERSION = "0.3.6"
_URL = "<a href = " "http://sourceforge.net/projects/pymodslave" ">Sourceforge Project Home Page</a>"


#-------------------------------------------------------------------------------
class ModSlaveAboutWindow(QtWidgets.QDialog, Ui_About):
	""" Class wrapper for about window ui """

	def __init__(self):
		super(ModSlaveAboutWindow, self).__init__()
		self.setupUi(self)
		# self.setupUI()

	def setupUI(self):
		#create window from ui
		self.ui = Ui_About()
		self.ui.setupUi(self)
		self.ui.lblVersion.setText("pyModSlave v{0}".format(_VERSION))
		self.ui.lblURL.setText(_URL)


#-------------------------------------------------------------------------------