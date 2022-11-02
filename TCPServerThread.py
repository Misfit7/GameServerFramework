#!/usr/bin/python3

import threading
import time
import queue
import random
import TCPProto
from twisted.internet import protocol, reactor
class TCPServerThread(threading.Thread):
    def __init__(self,maintask,port=9999):
        threading.Thread.__init__(self)        
        self.maintask=maintask
        self.port=port
        self.ListenTcp()
    def ListenTcp(self):
        self.maintask.regProtoAll()
        reactor.listenTCP(self.port, TCPProto.TCPProtoFactory(self.maintask))
    def run(self):
        reactor.run()


