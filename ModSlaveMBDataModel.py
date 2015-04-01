#-------------------------------------------------------------------------------
# Name:        ModSlaveMBDataModel
# Purpose:
#
# Author:      elbar
#
# Created:     29/08/2012
# Copyright:   (c) elbar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PyQt4 import QtGui,QtCore

#-------------------------------------------------------------------------------
class ModSlaveMBDataModel(QtCore.QObject):
    """ Modbus data model """

    def __init__(self, no_of_items = 10, data_type = 0):#data type > 0 : decimal, 1 : hex
        super(ModSlaveMBDataModel,self).__init__()
        self._no_of_items = no_of_items
        self._no_of_model_items = ((no_of_items - 1) // 10 + 1) * 10
        self.model = QtGui.QStandardItemModel((no_of_items - 1) // 10 + 1, 10)
        self.model.setHorizontalHeaderLabels(("0","1","2","3","4","5","6","7","8","9"))
        self.model.setVerticalHeaderLabels(["%02d"%(x*10) for x in range((no_of_items - 1) // 10 + 1)])
        self._data = None
        self._data_type = data_type
        # simulate values
        self.sim = False

    def update_model(self, data):
        self._data = data
        for i in range(self._no_of_model_items):
            row = i //10
            col = i % 10
            idx = self.model.index(row, col, QtCore.QModelIndex())
            if (i >= self._no_of_items):#not used cells
                self.model.setData(idx, "x", QtCore.Qt.DisplayRole)
                self.model.setData(idx, QtGui.QBrush(QtCore.Qt.red), QtCore.Qt.ForegroundRole)
                self.model.setData(idx, QtGui.QBrush(QtCore.Qt.lightGray), QtCore.Qt.BackgroundRole)
                item = self.model.itemFromIndex(idx)
                item.setEditable(False)
            else:
                if (self._data_type == 0):#decimal
                    self.model.setData(idx, self._data[i], QtCore.Qt.DisplayRole)
                    self.model.setData(idx, "Address : {0}".format(i), QtCore.Qt.ToolTipRole)
                else:#hex
                    self.model.setData(idx,"%X"%self._data[i], QtCore.Qt.DisplayRole)
        # emit SIGNAL for updating UI
        self.emit(QtCore.SIGNAL("update_view"))

    def set_data_type(self, dt):
        self._data_type = dt
        self.update_model(self._data)

    def reset_data(self):
        _new_data = []
        for i in range(self._no_of_model_items):
            row = i //10
            col = i % 10
            if (i < self._no_of_items):
                 idx = self.model.index(row, col, QtCore.QModelIndex())
                 self.model.setData(idx, 0, QtCore.Qt.DisplayRole)
                 self.model.setData(idx, "Address : {0}".format(i), QtCore.Qt.ToolTipRole)
                 _new_data.append(0)
        # emit SIGNAL for updating UI
        self.emit(QtCore.SIGNAL("update_view"))
        self.update_data(_new_data)
        self.update_model(_new_data)

    def update_item(self):
        _new_data = []
        for i in range(self._no_of_model_items):
            row = i //10
            col = i % 10
            if (i < self._no_of_items):
                 idx = self.model.index(row, col, QtCore.QModelIndex())
                 value = str((self.model.data(idx, QtCore.Qt.EditRole)).toString())
            if (self._data_type == 0): # decimal
                 _new_data.append(int(value, 10))
            elif(self._data_type == 1): #hex
                _new_data.append(int(value, 16))
        # emit SIGNAL for updating UI
        self.emit(QtCore.SIGNAL("update_view"))
        self.update_data(_new_data)
        self.update_model(_new_data)

    def update_data(self, data):
        # emit SIGNAL for updating modbus data
        self.emit(QtCore.SIGNAL("update_data"), data)

#-------------------------------------------------------------------------------