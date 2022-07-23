#-------------------------------------------------------------------------------
# Name:        ModSlaveSettings
# Purpose:
#
# Author:      ElBar
#
# Created:     17/04/2012
# Copyright:   (c) ElBar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PySide6 import QtGui,QtCore, QtWidgets
from Ui_settings import Ui_Settings

#add logging capability
import logging

#-------------------------------------------------------------------------------
class ModSlaveSettingsWindow(QtWidgets.QDialog):
    """ Class wrapper for general settings ui """

    def __init__(self):
        super(ModSlaveSettingsWindow,self).__init__()
        #init values
        self.coils = 50
        self.inputs = 50
        self.input_regs = 50
        self.hold_regs = 50
        self.max_no_of_bus_monitor_lines = 50
        self._logger = logging.getLogger("modbus_tk")
        self.setupUI()

    def setupUI(self):
        #create window from ui
        self.ui=Ui_Settings()
        self.ui.setupUi(self)
        #set init values
        self._set_values()
        #signals-slots
        self.accepted.connect(self._OK_pressed)
        self.rejected.connect(self._cancel_pressed)

    def _set_values(self):
        """set param values to ui"""
        self._logger.info("Set param values to UI")
        self.ui.sbNoOfCoils.setValue(self.coils)
        self.ui.sbNoOfDigInputs.setValue(self.inputs)
        self.ui.sbNoOfInputRegs.setValue(self.input_regs)
        self.ui.sbNoOfHoldingRegs.setValue(self.hold_regs)
        self.ui.sbMaxNoOfBusMonitorLines.setValue(self.max_no_of_bus_monitor_lines)

    def _get_values(self):
        """get param values from ui"""
        self._logger.info("Get param values from UI")
        self.coils = self.ui.sbNoOfCoils.value()
        self.inputs = self.ui.sbNoOfDigInputs.value()
        self.input_regs = self.ui.sbNoOfInputRegs.value()
        self.hold_regs = self.ui.sbNoOfHoldingRegs.value()
        self.max_no_of_bus_monitor_lines = self.ui.sbMaxNoOfBusMonitorLines.value()

    def _OK_pressed(self):
        """new values are accepted"""
        self._get_values()

    def _cancel_pressed(self):
        """new values are rejected"""
        self._set_values()

    def showEvent(self,QShowEvent):
        """set values for controls"""
        self._set_values()

#-------------------------------------------------------------------------------