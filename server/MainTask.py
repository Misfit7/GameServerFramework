import FuncMgr
import PlayerMgr
import ProtoFuncs
import TCPProto
import TCPServerThread
import TCPRecvThread
import TCPSendThread

from twisted.internet import reactor
import queue

class MainTask():
    def __init__(self):
        self.clients = {}
        self.pMgr=PlayerMgr.PlayerMgr()
        self.funcMgr=FuncMgr.FuncMgr()
        self.recvQueue=queue.Queue(1000)
        self.sendQueue=queue.Queue(1000)

    def pushRecvMsg(self,msg):
        if  self.recvQueue.full()==False:
            self.recvQueue.put(msg)
        else:
            pass

    def pushSendMsg(self,msg):
        if  self.sendQueue.full()==False:
            self.sendQueue.put(msg)
        else:
            pass

    def getRecvMsg(self):
        if  self.recvQueue.empty()==False:
            return self.recvQueue.get()
        return None

    def getSendMsg(self):
        q=self.sendQueue
        if  q.empty()==False:
            return q.get()
        return None

    def regProtoAll(self):
        self.funcMgr.regProto(1,3,ProtoFuncs.ProtoFuncs.login)
        self.funcMgr.regProto(2,1,ProtoFuncs.ProtoFuncs.msgBroadcast)
        self.funcMgr.regProto(2,2,ProtoFuncs.ProtoFuncs.msgPrivateChat)
        self.funcMgr.regProto(3,1,ProtoFuncs.ProtoFuncs.killLove)

    def start(self,port=9999):
        self.regProtoAll()
        t1=TCPRecvThread.TCPReceiveThread(self)
        t2=TCPSendThread.TCPSendThread(self)
        t1.start()
        t2.start()
        reactor.listenTCP(port,TCPProto.TCPProtoFactory(self))
        reactor.run()

if __name__ == '__main__':
    m=MainTask()
    m.start()
    while True:
        pass
