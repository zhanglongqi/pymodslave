#-------------------------------------------------------------------------------
# Name:        ModSlaveSim
# Purpose:
#
# Author:      elbar
#
# Created:     26/03/2012
# Copyright:   (c) elbar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PyQt4 import QtCore
#repeated timer
import RepeatTimer as rt
import random
#modbus toolkit
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.modbus_rtu as modbus_rtu
#serial communication
import serial
#data model
from ModSlaveMBDataModel import ModSlaveMBDataModel
#add logging capability
import logging

#-------------------------------------------------------------------------------
def ModServerFactory(args):

    logger = logging.getLogger("modbus_tk")

    _modServer = None

    if args[0]=='-tcp':
        logger.info("Build TCP Server - {0}:{1}".format(args[2],args[1]))
        try :
            _modServer = modbus_tcp.TcpServer(int(args[1]), args[2])
        except Exception,msg:
            logger.error("Error while building TCP Server : {0}".format(msg))
    elif args[0]=='-rtu':
        logger.info("Build RTU Server - Port: {0}, Baudrate: {1}, Bytesize: {2}, Parity: {3}, Stopbits : {4}"
                    .format(args[1],args[2],args[3],args[4],args[5]))
        try:
            _modServer = modbus_rtu.RtuServer(serial.Serial(port=int(args[1]),
                                                        baudrate=int(args[2]),
                                                        bytesize=int(args[3]),
                                                        parity=args[4],
                                                        stopbits=float(args[5]),
                                                        xonxoff=0))
        except Exception,msg:
            logger.error("Error while building RTU Server : {0}".format(msg))
    else:
        logger.error("Wrong arguments")

    return _modServer
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
class ModSlaveSim(QtCore.QObject):
    """ Simulate modbus data """

    def __init__(self,modServer,slaveAddress,timeIntervalSim,
                    no_coils = 50, no_dis_inputs = 50,
                    no_input_regs = 50, no_hold_regs = 50):
        super(ModSlaveSim,self).__init__()
        self._modServer = modServer
        self._no_coils = no_coils
        self._no_dis_inputs = no_dis_inputs
        self._no_input_regs = no_input_regs
        self._no_hold_regs = no_hold_regs
        self._logger = logging.getLogger("modbus_tk")
        # data models
        self.coils_data_model = ModSlaveMBDataModel(no_coils)
        self.connect(self.coils_data_model, QtCore.SIGNAL("update_data"), self.set_coils_data)
        self.dis_inputs_data_model = ModSlaveMBDataModel(no_dis_inputs)
        self.connect(self.dis_inputs_data_model, QtCore.SIGNAL("update_data"), self.set_dis_inputs_data)
        self.input_regs_data_model = ModSlaveMBDataModel(no_input_regs)
        self.connect(self.input_regs_data_model, QtCore.SIGNAL("update_data"), self.set_input_regs_data)
        self.hold_regs_data_model = ModSlaveMBDataModel(no_hold_regs)
        self.connect(self.hold_regs_data_model, QtCore.SIGNAL("update_data"), self.set_hold_regs_data)

        try:
            #add slave
            self.slave= modServer.add_slave(slaveAddress)
            #add blocks
            self.slave.add_block('0', cst.COILS , 0, self._no_coils)
            self.slave.add_block('1', cst.DISCRETE_INPUTS, 0, self._no_dis_inputs)
            self.slave.add_block('3', cst.ANALOG_INPUTS , 0, self._no_input_regs)
            self.slave.add_block('4', cst.HOLDING_REGISTERS, 0, self._no_hold_regs)
            #create timer
            self._timer=rt.RepeatTimer(timeIntervalSim,self._simBlockValues,0)
            self._simBlockValues()
        except Exception,msg:
    		self._logger.error("Slave Init Error : {0}".format(msg))

    def start(self):
        self._logger.info("Slave sim started")
        self._timer.start()

    def stop(self):
        self._logger.info("Slave sim stopped")
        self._timer.cancel()

    def _simBlockValues(self):
        #init block values
        block0=[]#coils
        block1=[]#discrete inputs
        block3=[]#input registers
        block4=[]#holding registers
        #coils
        if (self.coils_data_model.sim):
            for i in range(0,self._no_coils):
                block0.append(random.randrange(0,2,1))
            self.set_coils_data(block0)
        #discrete inputs
        if (self.dis_inputs_data_model.sim):
            for i in range(0,self._no_dis_inputs):
                block1.append(random.randrange(0,2,1))
            self.set_dis_inputs_data(block1)
        #input registers
        if (self.input_regs_data_model.sim):
            for i in range(0,self._no_input_regs):
                block3.append(random.randrange(0,65535,1))
            self.set_input_regs_data(block3)
        #holding registers
        if (self.hold_regs_data_model.sim):
            for i in range(0,self._no_hold_regs):
                block4.append(random.randrange(0,65535,1))
            self.set_hold_regs_data(block4)
        #update model data
        self.coils_data_model.update_model(self.get_coils_data())
        self.dis_inputs_data_model.update_model(self.get_dis_inputs_data())
        self.input_regs_data_model.update_model(self.get_input_regs_data())
        self.hold_regs_data_model.update_model(self.get_hold_regs_data())

    def get_coils_data(self):
        return self.slave.get_values('0',0,self._no_coils)

    def set_coils_data(self, data):
        self.slave.set_values('0',0,data)

    def get_dis_inputs_data(self):
        return self.slave.get_values('1',0,self._no_dis_inputs)

    def set_dis_inputs_data(self, data):
        self.slave.set_values('1',0,data)

    def get_input_regs_data(self):
        return self.slave.get_values('3',0,self._no_input_regs)

    def set_input_regs_data(self, data):
        self.slave.set_values('3',0,data)

    def get_hold_regs_data(self):
        return self.slave.get_values('4',0,self._no_hold_regs)

    def set_hold_regs_data(self, data):
        self.slave.set_values('4',0,data)

#-------------------------------------------------------------------------------
