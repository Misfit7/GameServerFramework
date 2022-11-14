import pymysql
from twisted.internet import reactor
import queue

import FuncMgr
import PlayerMgr
import ProtoFuncs
import TCPProto
import TCPRecvThread
import TCPSendThread

class MainTask():
    def __init__(self):
        self.clients={} #连接上来的用户的集合
        self.pMgr=PlayerMgr.PlayerMgr() #玩家集合
        self.funcMgr=FuncMgr.FuncMgr() #协议处理函数集合
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

    def getConn(self):
            conn_obj = pymysql.connect(
                host='gz-cdb-bhtlu6g1.sql.tencentcdb.com',  # MySQL服务端的IP地址
                port=56807,  # MySQL默认PORT地址(端口号)
                user='root',  # 用户名
                password='xxxrrr123456',  # 密码,也可以简写为passwd
                database='game',  # 库名称,也可以简写为db
                charset='utf8'  # 字符编码
            )
            return conn_obj

    def start(self,port=9999):
        self.regProtoAll()
        t1=TCPRecvThread.TCPRecvThread(self)
        t2=TCPSendThread.TCPSendThread(self)
        t1.start()
        t2.start()
        reactor.listenTCP(port,TCPProto.TCPProtoFactory(self))
        reactor.run()

if __name__=="__main__":
    m=MainTask()
    m.start()
    while True:
        pass