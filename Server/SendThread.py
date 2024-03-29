#!/usr/bin/python3

import threading
import time

class SendThread(threading.Thread):
    def __init__(self,maintask):
        threading.Thread.__init__(self)        
        self.maintask=maintask
        
    def run(self):
        while True:            
            xxx=self.maintask.getSendMsg()
            if xxx is not None:
                if ("UDP" in xxx):
                    me,cips,msg,type=xxx
                    for cip in cips:
                        me.transport.write(msg,cip)
                else:
                    clients,msg=xxx
                    for clt in clients:
                        clt.transport.write(msg)
            time.sleep(0.1)