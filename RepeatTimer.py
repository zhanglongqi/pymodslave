#-------------------------------------------------------------------------------
# Name:        RepeatTimer
# Purpose:
#
# Author:      elbar
#
# Created:     26/03/2012
# Copyright:   (c) elbar 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import threading

#add logging capability
import logging

#-------------------------------------------------------------------------------
class RepeatTimer(threading.Thread):

    def __init__(self, interval, function, iterations=0, args=[], kwargs={}):
        threading.Thread.__init__(self)
        self._logger = logging.getLogger("modbus_tk")
        self.interval = interval
        self.function = function
        self.iterations = iterations
        self.args = args
        self.kwargs = kwargs
        self.finished = threading.Event()

    def run(self):
        count = 0
        self._logger.info("Start timer")
        while not self.finished.is_set() and (self.iterations <= 0 or count < self.iterations):
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
                count += 1
        self._logger.info("Stop timer")

    def cancel(self):
        self.finished.set()

#-------------------------------------------------------------------------------
