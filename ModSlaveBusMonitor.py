#-------------------------------------------------------------------------------
# Name:        ModSlaveBusMonitor
# Purpose:
#
# Author:      elbar
#
# Created:     04/07/2013
# Copyright:   (c) elbar 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PySide6 import QtGui,QtCore, QtWidgets
from Ui_busmonitor import Ui_BusMonitor
import datetime as dt
import Utils

#add logging capability
import logging
#modbus toolkit
import modbus_tk
from modbus_tk.hooks import install_hook

#Hooks
SLAVE_HOOKS = ("modbus.Slave.on_exception")
SERVER_TCP_HOOKS = ("modbus_tcp.TcpServer.after_recv", "modbus_tcp.TcpServer.before_send")
SERVER_RTU_HOOKS = ("modbus_rtu.RtuServer.after_read", "modbus_rtu.RtuServer.before_write")

#-------------------------------------------------------------------------------
class ModSlaveBusMonitorWindow(QtWidgets.QMainWindow):
    """ Class wrapper for modbus data """

    def __init__(self):
        super(ModSlaveBusMonitorWindow,self).__init__()
        self._logger = logging.getLogger("modbus_tk")
        self._model = QtCore.QStringListModel()
        self._string_list = []
        self._max_no_of_bus_monitor_lines = 50
        self.packets = 0
        self.errors = 0
        self.svr = None
        #setu UI
        self.setupUI()
        self.ui.lstRawData.setModel(self._model)
        self.running = False
        #install hooks
        install_hook(SERVER_RTU_HOOKS[0], self._req_rtu_data)
        install_hook(SERVER_RTU_HOOKS[1], self._resp_rtu_data)
        install_hook(SERVER_TCP_HOOKS[0], self._req_tcp_data)
        install_hook(SERVER_TCP_HOOKS[1], self._resp_tcp_data)
        install_hook(SLAVE_HOOKS, self._error_data)

    def setupUI(self):
        #create window from ui
        self.ui=Ui_BusMonitor()
        self.ui.setupUi(self)
        #setup toolbar
        self.ui.toolBar.addAction(self.ui.actionStart_Stop)
        self.ui.toolBar.addAction(self.ui.actionSave)
        self.ui.toolBar.addAction(self.ui.actionClear)
        self.ui.toolBar.addAction(self.ui.actionExit)
        #signals-slots
        self.ui.actionStart_Stop.triggered.connect(self._start_stop)
        self.ui.actionSave.triggered.connect(self._save)
        self.ui.actionClear.triggered.connect(self._clear)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.lstRawData.activated.connect(self._selected_row)
        self.ui.lstRawData.clicked.connect(self._selected_row)

    def set_max_no_of_bus_monitor_lines(self, no):
        self._max_no_of_bus_monitor_lines = no

    def _add_line(self, line):
        if (self.ui.actionStart_Stop.isChecked()):
            if (self._string_list.count() >= self._max_no_of_bus_monitor_lines):
                self._string_list.removeAt(0)
            self._string_list.append(QtCore.QString(line))
        self._model.setStringList(self._string_list)

    def _start_stop(self):
        self.running = self.ui.actionStart_Stop.isChecked()

    def _save(self):
        file_name = QtGui.QFileDialog.getSaveFileName(self, QtCore.QString('Save File As...'),
                            QtCore.QDir.homePath(),
                            'Text (*.txt)', 'Text (*.txt)', QtGui.QFileDialog.DontConfirmOverwrite)
        try:
            f = open(QtCore.QDir.toNativeSeparators(file_name), 'w')
            f.writelines(['%s\n' % str(line) for line in self._string_list])
            f.close()
        except:
            Utils.errorMessageBox('Error! Cannot Save Data')

    def _clear(self):
        self._string_list.clear()
        self._model.setStringList(self._string_list)
        self.ui.txtPDU.clear()

    def _req_rtu_data(self, data):
        self.packets += 1
        self.emit(QtCore.SIGNAL("update_counters"))
        if (self.running):
            req = str(data[1]).encode('hex')
            self._add_line("[RTU]>Rx > %s : %s" % (dt.datetime.now().strftime('%H:%M:%S'), self._format_data(req.upper())))

    def _resp_rtu_data(self, data):
        if (self.running):
            resp = str(data[1]).encode('hex')
            self._add_line("[RTU]>Tx > %s : %s" % (dt.datetime.now().strftime('%H:%M:%S'),  self._format_data(resp.upper())))

    def _req_tcp_data(self, data):
        self.packets += 1
        self.emit(QtCore.SIGNAL("update_counters"))
        if (self.running):
            req = str(data[2]).encode('hex')
            self._add_line("[TCP]>Rx > %s : %s" % (dt.datetime.now().strftime('%H:%M:%S'), self._format_data(req.upper())))

    def _resp_tcp_data(self, data):
        if (self.running):
            resp = str(data[2]).encode('hex')
            self._add_line("[TCP]>Tx > %s : %s" % (dt.datetime.now().strftime('%H:%M:%S'),  self._format_data(resp.upper())))

    def _error_data(self, data):
        self.errors += 1
        self.emit(QtCore.SIGNAL("update_counters"))
        if (self.running):
            slave = data[1]
            msg = data[2]
            self._add_line("Sys > %s : Slave %s - %s" % (dt.datetime.now().strftime('%H:%M:%S'), slave, msg))

    def _format_data(self, data):
        fmt_data = ''
        for i in xrange(0, len(data), 2):
            fmt_data += (data[i:i+2] + ' ')
        return fmt_data

    def reset_counters(self):
        self.packets = 0
        self.errors = 0
        self.emit(QtCore.SIGNAL("update_counters"))

    def _selected_row(self, sel):
        data = QtCore.QVariant.toPyObject(sel.data())
        if ('Sys' in data):
            self._parse_Sys_Msg(str(data))
        elif ('Tx' in data):
            self._parse_Tx_Msg(str(data))
        elif ('Rx' in data):
            self._parse_Rx_Msg(str(data))
        else:
            self.ui.txtPDU.setPlainText('Error! Cannot parse Message')

    def _parse_Tx_Msg(self, data):
        self.ui.txtPDU.setPlainText('Type : Tx Message')
        msg = data.split('>')
        try :
            pdu = msg[2].split(' : ')
            self.ui.txtPDU.appendPlainText('TimeStamp : %s' % pdu[0].strip())
            mb_data = pdu[1].replace(' ', '')
            if ('RTU' in data):
                self._parse_Tx_pdu(mb_data[:-4])
                self.ui.txtPDU.appendPlainText('CRC : %s' % mb_data[-4:])
            elif ('TCP' in data):
                self.ui.txtPDU.appendPlainText('Transaction ID  : %s' % mb_data[0:4])
                self.ui.txtPDU.appendPlainText('Protocol ID  : %s' % mb_data[4:8])
                self.ui.txtPDU.appendPlainText('Length  : %s' % mb_data[8:12])
                self._parse_Tx_pdu(mb_data[12:])
            else :
                self.ui.txtPDU.appendPlainText('Error! Cannot parse Message')
        except :
            self.ui.txtPDU.appendPlainText('Error! Cannot parse Message')

    def _parse_Tx_pdu(self, pdu):
        try :
            self.ui.txtPDU.appendPlainText('Slave ID : %s' % pdu[:2])
            fc = int(pdu[2:4], 16)
            if (fc > 128): #Modbus error
                self.ui.txtPDU.appendPlainText('Function Code [80 + SlaveID] : %s' % pdu[2:4])
                self.ui.txtPDU.appendPlainText('Exception Code : %s' % pdu[4:6])
            elif (fc <= 4): # Read
                self.ui.txtPDU.appendPlainText('Function Code : %s' % pdu[2:4])
                self.ui.txtPDU.appendPlainText('Byte Count : %s' % pdu[4:6])
                self.ui.txtPDU.appendPlainText('Register Values : %s' % pdu[6:])
            elif (fc <= 4): # Read
                self.ui.txtPDU.appendPlainText('Function Code : %s' % pdu[2:4])
                self.ui.txtPDU.appendPlainText('Byte Count : %s' % pdu[4:6])
                self.ui.txtPDU.appendPlainText('Register Values : %s' % pdu[6:])
            elif (fc >= 5 and fc <= 6): # Write
                self.ui.txtPDU.appendPlainText('Function Code : %s' % pdu[2:4])
                self.ui.txtPDU.appendPlainText('Byte Count : %s' % pdu[4:6])
                self.ui.txtPDU.appendPlainText('Starting Address : %s' % pdu[6:8])
                self.ui.txtPDU.appendPlainText('Output Value : %s' % pdu[8:])
            elif (fc >= 15 and fc <= 16): # Write Multiple
                self.ui.txtPDU.appendPlainText('Function Code : %s' % pdu[2:4])
                self.ui.txtPDU.appendPlainText('Byte Count : %s' % pdu[4:6])
                self.ui.txtPDU.appendPlainText('Starting Address : %s' % pdu[6:8])
                self.ui.txtPDU.appendPlainText('Quantity of Registers : %s' % pdu[8:])
        except :
            self.ui.txtPDU.appendPlainText('Error! Cannot parse PDU')

    def _parse_Rx_Msg(self, data):
        self.ui.txtPDU.setPlainText('Type : Rx Message')
        msg = data.split('>')
        try :
            pdu = msg[2].split(' : ')
            self.ui.txtPDU.appendPlainText('TimeStamp : %s' % pdu[0].strip())
            mb_data = pdu[1].replace(' ', '')
            if ('RTU' in data):
                self._parse_Rx_pdu(mb_data[:-4])
                self.ui.txtPDU.appendPlainText('CRC : %s' % mb_data[-4:])
            elif ('TCP' in data):
                self.ui.txtPDU.appendPlainText('Transaction ID  : %s' % mb_data[0:4])
                self.ui.txtPDU.appendPlainText('Protocol ID  : %s' % mb_data[4:8])
                self.ui.txtPDU.appendPlainText('Length  : %s' % mb_data[8:12])
                self._parse_Rx_pdu(mb_data[12:])
            else :
                self.ui.txtPDU.appendPlainText('Error! Cannot parse Message')
        except :
            self.ui.txtPDU.appendPlainText('Error! Cannot parse Message')

    def _parse_Rx_pdu(self, pdu):
        try :
            self.ui.txtPDU.appendPlainText('Slave ID : %s' % pdu[:2])
            self.ui.txtPDU.appendPlainText('Function Code : %s' % pdu[2:4])
            self.ui.txtPDU.appendPlainText('Starting Address : %s' % pdu[4:8])
            fc = int(pdu[2:4], 16)
            if (fc <= 4): # Read
                self.ui.txtPDU.appendPlainText('Quantity of Registers : %s' % pdu[8:12])
            elif (fc >= 5 and fc <= 6): # Write
                self.ui.txtPDU.appendPlainText('Output Value : %s' % pdu[8:12])
            elif (fc >= 15 and fc <= 16): # Write Multiple
                self.ui.txtPDU.appendPlainText('Quantity of Registers : %s' % pdu[8:12])
                self.ui.txtPDU.appendPlainText('Byte Count : %s' % pdu[12:14])
                self.ui.txtPDU.appendPlainText('Output Values : %s' % pdu[14:])
        except :
            self.ui.txtPDU.appendPlainText('Error! Cannot parse PDU')

    def _parse_Sys_Msg(self, data):
        self.ui.txtPDU.setPlainText('Type : System Message')
        msg = data.split('>')
        pdu = msg[1].split(' : ')
        self.ui.txtPDU.appendPlainText('TimeStamp : %s' % pdu[0].strip())
        self.ui.txtPDU.appendPlainText('Message : %s' % pdu[1].strip())

    def showEvent(self,QShowEvent):
        pass

    def closeEvent(self,QCloseEvent):
        self.ui.actionStart_Stop.setChecked(False)

#-------------------------------------------------------------------------------