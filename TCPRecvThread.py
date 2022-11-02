#!/usr/bin/python3

import threading
import time
import queue
import random
import TCPProto

class TCPRecvThread(threading.Thread):
    def __init__(self,maintask):
        threading.Thread.__init__(self)        
        self.maintask=maintask
        
    def run(self):
        while True:
            xx=self.maintask.getRecvMsg()
            if xx is not None:
                self.maintask.funcMgr.doProto(self.maintask,*xx)
            else:
                time.sleep(0.1)