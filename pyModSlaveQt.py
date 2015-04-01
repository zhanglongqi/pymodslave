#-------------------------------------------------------------------------------
# Name:        pyModSlaveQt
# Purpose:
#
# Author:      ElBar
#
# Created:     29/02/2012
# Copyright:   (c) ElBar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys
from PyQt4 import QtGui,QtCore
import logging # add logging capability
import ConfigParser # config file parser

from Ui_mainwindow import Ui_MainWindow
from ModSlaveAbout import ModSlaveAboutWindow
from ModSlaveSettingsRTU import ModSlaveSettingsRTUWindow
from ModSlaveSettingsTCP import ModSlaveSettingsTCPWindow
from ModSlaveSettings import ModSlaveSettingsWindow
from ModSlaveMBData import ModSlaveMBDataWindow
from ModSlaveBusMonitor import ModSlaveBusMonitorWindow

#modbus toolkit
import modbus_tk
import ModSlaveSim as simSlave
from modbus_tk.hooks import install_hook
import Utils

#Hooks
SLAVE_HOOKS = ("modbus.Slave.on_exception")

#-------------------------------------------------------------------------------
class ModSlaveMainWindow(QtGui.QMainWindow):
    """ Class wrapper for main window ui """

    def __init__(self):
        super(ModSlaveMainWindow,self).__init__()
        #init
        self.svr = None # Server
        self._svr_args = []
        self.slv = None # Slave
        self._time_interval = 1000 # interval for simulation in msec
        self._params_file_name = 'pyModSlaveQt.ini'
        self._logger = logging.getLogger("modbus_tk")
        self.setupUI()

    def setupUI(self):
        #create window from ui
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        #setup toolbar
        self.ui.mainToolBar.addAction(self.ui.actionSerial_RTU)
        self.ui.mainToolBar.addAction(self.ui.actionTCP)
        self.ui.mainToolBar.addAction(self.ui.actionSettings)
        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addAction(self.ui.actionIO_Data)
        self.ui.mainToolBar.addAction(self.ui.actionBus_Monitor)
        self.ui.mainToolBar.addAction(self.ui.actionReset_Counters)
        self.ui.mainToolBar.addSeparator()
        self.ui.mainToolBar.addAction(self.ui.actionAbout)
        self.ui.mainToolBar.addAction(self.ui.actionExit)
        #setup status bar
        pm = QtGui.QPixmap()
        self.status_ind = QtGui.QLabel(self.ui.centralWidget)
        self.status_ind.setFixedSize(16,16)
        self.status_ind.setPixmap(QtGui.QPixmap(':/img/ballorange-16.png'))
        self.status_text = QtGui.QLabel(self.ui.centralWidget)
        self.status_packet_text = QtGui.QLabel(self.ui.centralWidget)
        self.status_packet_text.setStyleSheet("QLabel {color:blue;}")
        self.status_error_text = QtGui.QLabel(self.ui.centralWidget)
        self.status_error_text.setStyleSheet("QLabel {color:red;}")
        self.ui.statusBar.addWidget(self.status_ind)
        self.ui.statusBar.addWidget(self.status_text, 14)
        self.ui.statusBar.addWidget(self.status_packet_text, 14)
        self.ui.statusBar.addWidget(self.status_error_text, 14)
        #setup dialogs
        self._about_dlg = ModSlaveAboutWindow()
        self._settingsRTU_dlg = ModSlaveSettingsRTUWindow()
        self._settingsTCP_dlg = ModSlaveSettingsTCPWindow()
        self._settings_dlg = ModSlaveSettingsWindow()
        self._bus_monitor_dlg = ModSlaveBusMonitorWindow()
        #setup data windows
        self._mbdata_dlg = ModSlaveMBDataWindow()
        #signals-slots
        self.ui.actionAbout.triggered.connect(self._about_dlg.show)
        self.ui.actionSerial_RTU.triggered.connect(self._settings_RTU_show)
        self.ui.actionTCP.triggered.connect(self._settings_TCP_show)
        self.ui.actionSettings.triggered.connect(self._settings_show)
        self.ui.actionIO_Data.triggered.connect(self._mbdata_show)
        self.ui.actionBus_Monitor.triggered.connect(self._bus_monitor_show)
        self.ui.actionReset_Counters.triggered.connect(self._reset_counters)
        self.ui.btStartStop.clicked.connect(self._start_stop)
        self.ui.cmbModbusMode.currentIndexChanged.connect(self._update_status_bar)
        self.ui.spInterval.valueChanged.connect(self._spInterval_value_changed)
        self.connect(self._bus_monitor_dlg, QtCore.SIGNAL("update_counters"), self._update_counters)
        #show window
        self._update_status_bar()
        self.show()

    def _settings_RTU_show(self):
        """open RTU settings dialog"""
        self._settingsRTU_dlg.exec_()
        self._update_status_bar()

    def _settings_TCP_show(self):
        """open TCP settings dialog"""
        self._settingsTCP_dlg.exec_()
        self._update_status_bar()

    def _settings_show(self):
        """open general settings dialog"""
        self._settings_dlg.exec_()
        self._bus_monitor_dlg.set_max_no_of_bus_monitor_lines(self._settings_dlg.max_no_of_bus_monitor_lines)
        self._update_status_bar()

    def _mbdata_show(self):
        """coils data dialog"""
        self._mbdata_dlg.show()

    def _bus_monitor_show(self):
        """coils data dialog"""
        self._bus_monitor_dlg.svr = self.svr
        self._bus_monitor_dlg.show()

    def _spInterval_value_changed(self,value):
        """sim interval value changed"""
        self._time_interval = value

    def _update_status_bar(self):
        """update status bar"""
        if (self.ui.cmbModbusMode.currentText() == "TCP"):#TCP server
            msg = "TCP : {0}:{1}".format(self._settingsTCP_dlg.tcp_ip,
                                        self._settingsTCP_dlg.tcp_port)
        elif (self.ui.cmbModbusMode.currentText() == "RTU"):#RTU server
            msg = "RTU : {0}, {1}, {2}, {3}, {4}".format(self._settingsRTU_dlg.rtu_port,
                                                    self._settingsRTU_dlg.baud_rate,
                                                    self._settingsRTU_dlg.byte_size,
                                                    self._settingsRTU_dlg.stop_bits,
                                                    self._settingsRTU_dlg.parity)
        self.status_text.setText(msg)
        if (self.svr != None):#server is running
            self.status_ind.setPixmap(QtGui.QPixmap(':/img/ballgreen-16.png'))
        else:#server is stopped
            self.status_ind.setPixmap(QtGui.QPixmap(':/img/ballorange-16.png'))
        self._update_counters()

    def _update_counters(self):
        """update packets - errors counters"""
        self.status_packet_text.setText('Packets : %d' % self._bus_monitor_dlg.packets)
        self.status_error_text.setText('Erros : %d' % self._bus_monitor_dlg.errors)

    def _update_ui(self):
        """update enable-disable status of ui components"""
        if (self.ui.btStartStop.isChecked()):#start
            self.ui.btStartStop.setText("Stop")
            self.ui.cmbModbusMode.setEnabled(False)
            self.ui.sbSlaveID.setEnabled(False)
            self.ui.spInterval.setEnabled(False)
            self.ui.actionSerial_RTU.setEnabled(False)
            self.ui.actionTCP.setEnabled(False)
            self.ui.actionSettings.setEnabled(False)
        else:#stop
            self.ui.btStartStop.setText("Start")
            self.ui.cmbModbusMode.setEnabled(True)
            self.ui.sbSlaveID.setEnabled(True)
            self.ui.spInterval.setEnabled(True)
            self.ui.actionSerial_RTU.setEnabled(True)
            self.ui.actionTCP.setEnabled(True)
            self.ui.actionSettings.setEnabled(True)

    def _start_stop(self):
        """start - stop server and slave"""
        self._reset_counters()
        del self._svr_args[:]#clear params
        svr_hooks = []
        if (self.ui.btStartStop.isChecked()):#start
            if (self.ui.cmbModbusMode.currentText() == "TCP"): # TCP server params
                self._logger.info("Starting TCP server")
                self._svr_args.append("-tcp")
                self._svr_args.append(self._settingsTCP_dlg.tcp_port)
                self._svr_args.append(self._settingsTCP_dlg.tcp_ip)
            elif (self.ui.cmbModbusMode.currentText() == "RTU"): # RTU server params
                self._logger.info("Starting RTU server")
                self._svr_args.append("-rtu")
                self._svr_args.append(self._settingsRTU_dlg.rtu_port - 1) # zero based index
                self._svr_args.append(self._settingsRTU_dlg.baud_rate)
                self._svr_args.append(self._settingsRTU_dlg.byte_size)
                self._svr_args.append(self._settingsRTU_dlg.parity[0])
                self._svr_args.append(self._settingsRTU_dlg.stop_bits)
            if (len(self._svr_args) > 0): # check for valid no of parameters
                self.svr = simSlave.ModServerFactory(self._svr_args)
                if (self.svr == None):#fail to build server
                    self._logger.error("Fail to start server")
                    Utils.errorMessageBox("Fail to start server")
                    self.ui.btStartStop.setChecked(False)
                else:
                    self.svr.start()
                    self.slv = simSlave.ModSlaveSim(self.svr,self.ui.sbSlaveID.value(),
                                                self.ui.spInterval.value()/1000.0,
                                                self._settings_dlg.coils,
                                                self._settings_dlg.inputs,
                                                self._settings_dlg.input_regs,
                                                self._settings_dlg.hold_regs)
                    if (self.slv == None):#fail to build slave
                        self._logger.error("Fail to start slave")
                        Utils.errorMessageBox("Fail to start slave")
                        self.svr.stop()
                        self.svr = None
                        self.ui.btStartStop.setChecked(False)
                    else:
                        self._mbdata_dlg.set_data_models(self.slv.coils_data_model,
                                                         self.slv.dis_inputs_data_model,
                                                         self.slv.input_regs_data_model,
                                                         self.slv.hold_regs_data_model)
                        self.slv.start()
        else:#stop
            self._logger.info("Stop server")
            self.slv.stop()
            self.svr.stop()
            self.slv = None
            self.svr = None
        #update user interface
        self._update_ui()
        self._update_status_bar()

    def _load_params(self):
        self._logger.info("Load params")
        config_tcp_defaut = {'TCP_Port':'502', 'TCP_IP':'127.000.000.001'}
        config_rtu_defaut = {'RTU_Port':'0', 'Baud':'9600', 'DataBits':'8', 'StopBits':'1', 'Parity':'None'}
        config_var_defaut = {'Coils':'0', 'DisInputs':'0', 'InputRegs':'0', 'HoldRegs':'0', 'TimeInterval':'1000', 'MaxNoOfBusMonitorLines':'50'}
        config_default = {}
        config_default.update(config_tcp_defaut)
        config_default.update(config_rtu_defaut)
        config_default.update(config_var_defaut)
        config = ConfigParser.RawConfigParser(config_default)
        if not(config.read(self._params_file_name)):#if file does not exist exit
            self._logger.error("Parameters file does not exist")
            return
        #TCP Settings
        self._settingsTCP_dlg.tcp_port = config.getint('TCP', 'TCP_Port')
        self._settingsTCP_dlg.tcp_ip = config.get('TCP', 'TCP_IP')
        #RTU Settings
        self._settingsRTU_dlg.rtu_port = config.getint('RTU', 'RTU_Port')
        self._settingsRTU_dlg.baud_rate = config.getint('RTU', 'Baud')
        self._settingsRTU_dlg.byte_size = config.getint('RTU', 'DataBits')
        self._settingsRTU_dlg.stop_bits = config.get('RTU', 'StopBits')
        self._settingsRTU_dlg.parity = config.get('RTU', 'Parity')
        #Var Settings
        self._settings_dlg.coils = config.getint('Var', 'Coils')
        self._settings_dlg.inputs = config.getint('Var', 'DisInputs')
        self._settings_dlg.input_regs = config.getint('Var', 'InputRegs')
        self._settings_dlg.hold_regs = config.getint('Var', 'HoldRegs')
        self._time_interval = config.getint('Var', 'TimeInterval')
        self._settings_dlg.max_no_of_bus_monitor_lines = config.getint('Var', 'MaxNoOfBusMonitorLines')
        self._bus_monitor_dlg.set_max_no_of_bus_monitor_lines(self._settings_dlg.max_no_of_bus_monitor_lines)

    def _save_params(self):
        self._logger.info("Save params")
        config = ConfigParser.RawConfigParser()
        #TCP Settings
        config.add_section('TCP')
        config.set('TCP','TCP_Port',self._settingsTCP_dlg.tcp_port)
        config.set('TCP','TCP_IP',self._settingsTCP_dlg.tcp_ip)
        #RTU Settings
        config.add_section('RTU')
        config.set('RTU','RTU_Port',self._settingsRTU_dlg.rtu_port)
        config.set('RTU','Baud',self._settingsRTU_dlg.baud_rate)
        config.set('RTU','DataBits',self._settingsRTU_dlg.byte_size)
        config.set('RTU','StopBits',self._settingsRTU_dlg.stop_bits)
        config.set('RTU','Parity',self._settingsRTU_dlg.parity)
        #Var Settings
        config.add_section('Var')
        config.set('Var','Coils',self._settings_dlg.coils)
        config.set('Var','DisInputs',self._settings_dlg.inputs)
        config.set('Var','InputRegs',self._settings_dlg.input_regs)
        config.set('Var','HoldRegs',self._settings_dlg.hold_regs)
        config.set('Var','TimeInterval',self._time_interval)
        config.set('Var','MaxNoOfBusMonitorLines',self._settings_dlg.max_no_of_bus_monitor_lines)
        #Save Settings
        config_file = open(self._params_file_name, 'wb')
        config.write(config_file)

    def _reset_counters(self):
        self._bus_monitor_dlg.reset_counters()

    def showEvent(self,QShowEvent):
        """set values for controls"""
        self._load_params()
        self.ui.spInterval.setValue(self._time_interval)
        self._update_status_bar()

    def closeEvent(self,QCloseEvent):
        """window is closing"""
        self._save_params()

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def main():

    #logger
    logger = modbus_tk.utils.create_logger("console")
    Utils.set_up_logger_file(logger,'pyModSlaveQt.log')
    #create qt application
    app=QtGui.QApplication(sys.argv)
    #load main window
    window=ModSlaveMainWindow()
    #application loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------