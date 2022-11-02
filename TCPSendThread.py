#!/usr/bin/python3

import threading
import time
import queue
import random
import TCPProto

class TCPSendThread(threading.Thread):
    def __init__(self,maintask):
        threading.Thread.__init__(self)        
        self.maintask=maintask
        
    def run(self):
        while True:            
            xxx=self.maintask.getSendMsg()
            if xxx is not None:
                clients,msg=xxx
                for clt in clients:
                    clt.transport.write(msg)
            time.sleep(0.1)