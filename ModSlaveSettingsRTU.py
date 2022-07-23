#-------------------------------------------------------------------------------
# Name:        ModSlaveSettingsRTU
# Purpose:
#
# Author:      ElBar
#
# Created:     17/04/2012
# Copyright:   (c) ElBar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PySide6 import QtWidgets
from Ui_settingsModbusRTU import Ui_SettingsModbusRTU

import Utils

#add logging capability
import logging


#-------------------------------------------------------------------------------
class ModSlaveSettingsRTUWindow(QtWidgets.QDialog):
	""" Class wrapper for RTU settings ui """

	def __init__(self):
		super(ModSlaveSettingsRTUWindow, self).__init__()
		#init value
		self.rtu_port = 1
		self.baud_rate = 9600
		self.byte_size = 8
		self.parity = 'None'
		self.stop_bits = '1'
		self._logger = logging.getLogger("modbus_tk")
		self.setupUI()

	def setupUI(self):
		#create window from ui
		self.ui = Ui_SettingsModbusRTU()
		self.ui.setupUi(self)
		#set init values
		self._set_values()
		#signals-slots
		self.accepted.connect(self._OK_pressed)
		self.rejected.connect(self._cancel_pressed)

	def _set_values(self):
		"""set param values to ui"""
		self._logger.info("Set param values to UI")
		self.ui.cmbPort.setEditText(str(self.rtu_port))
		self.ui.cmbBaud.setCurrentIndex(self.ui.cmbBaud.findText(str(self.baud_rate)))
		self.ui.cmbDataBits.setCurrentIndex(self.ui.cmbDataBits.findText(str(self.byte_size)))
		self.ui.cmbParity.setCurrentIndex(self.ui.cmbParity.findText(self.parity))
		self.ui.cmbStopBits.setCurrentIndex(self.ui.cmbStopBits.findText(str(self.stop_bits)))

	def _get_values(self):
		"""get param values from ui"""
		self._logger.info("Get param values from UI")
		self.rtu_port = int(self.ui.cmbPort.currentText())
		self.baud_rate = self.ui.cmbBaud.currentText()
		self.byte_size = self.ui.cmbDataBits.currentText()
		self.parity = self.ui.cmbParity.currentText()
		self.stop_bits = self.ui.cmbStopBits.currentText()

	def _OK_pressed(self):
		"""new values are accepted"""
		port = str(self.ui.cmbPort.currentText())
		if (port.isdigit() and int(port) >= 1 and int(port) <= 16):  #port must be an integer
			self._get_values()
		else:
			self.rtu_port = 1
			self._set_values()
			self._get_values()
			self._logger.error("Port must be an integer between 1 and 16")
			Utils.errorMessageBox("Port must be an integer between 1 and 16")

	def _cancel_pressed(self):
		"""new values are rejected"""
		self._set_values()

	def showEvent(self, QShowEvent):
		"""set values for controls"""
		self._set_values()


#-------------------------------------------------------------------------------