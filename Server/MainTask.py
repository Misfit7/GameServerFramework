import pymysql
from twisted.internet import reactor
import queue

import BackgroundControl
import FuncMgr
import PlayerMgr
import ProtoFuncs
import TCPProto
import RecvThread
import SendThread
import DBWriteThread
import UDPProto
import Schedule


class MainTask():
    def __init__(self):
        self.waitclients = set()  # 连接上来的用户集合
        self.clients = {}  # 连接并登陆的用户的字典
        self.cips = {}  # 用户名及ip字典
        self.order = {}  # 订单
        self.pMgr = PlayerMgr.PlayerMgr()  # 玩家集合
        self.funcMgr = FuncMgr.FuncMgr()  # 协议处理函数集合
        self.recvQueue = queue.Queue(1000)
        self.sendQueue = queue.Queue(1000)
        self.conn = self.getConn()
        self.schedule = Schedule.Schedule(self)
        self.UDP = None

    # 放入接收消息
    def pushRecvMsg(self, msg):
        if self.recvQueue.full() == False:
            self.recvQueue.put(msg)
        else:
            pass

    # 放入发送消息
    def pushSendMsg(self, msg):
        if self.sendQueue.full() == False:
            self.sendQueue.put(msg)
        else:
            pass

    # 提取接收消息
    def getRecvMsg(self):
        if self.recvQueue.empty() == False:
            return self.recvQueue.get()
        return None

    # 提取发送消息
    def getSendMsg(self):
        q = self.sendQueue
        if q.empty() == False:
            return q.get()
        return None

    # 注册方法
    def regProtoAll(self):
        # 登陆
        self.funcMgr.regProto(1, 1, ProtoFuncs.ProtoFuncs.login)
        # 注册
        self.funcMgr.regProto(1, 2, ProtoFuncs.ProtoFuncs.register)
        # 登出
        self.funcMgr.regProto(1, 3, ProtoFuncs.ProtoFuncs.logout)
        # 广播
        self.funcMgr.regProto(2, 1, ProtoFuncs.ProtoFuncs.msgBroadcast)
        # 私聊
        self.funcMgr.regProto(2, 2, ProtoFuncs.ProtoFuncs.msgPrivateChat)
        # 攻击
        self.funcMgr.regProto(3, 1, ProtoFuncs.ProtoFuncs.attack)
        # 恢复
        self.funcMgr.regProto(3, 2, ProtoFuncs.ProtoFuncs.heal)
        # 个人状态
        self.funcMgr.regProto(3, 3, ProtoFuncs.ProtoFuncs.playerStatus)
        # 加点
        self.funcMgr.regProto(3, 4, ProtoFuncs.ProtoFuncs.playerSkills)
        # 移动
        self.funcMgr.regProto(3, 5, ProtoFuncs.ProtoFuncs.playerMove)
        # 充值链接
        self.funcMgr.regProto(4, 1, ProtoFuncs.ProtoFuncs.charge)
        # 充值成功
        self.funcMgr.regProto(4, 2, ProtoFuncs.ProtoFuncs.chargeSuccess)

    # 数据库连接
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

    # 线程启动
    def start(self, portTCP=9999, portUDP=8090):
        self.regProtoAll()
        # 定时器
        self.schedule.start()
        # 接收消息线程
        t1 = RecvThread.RecvThread(self)
        # 发送消息线程
        t2 = SendThread.SendThread(self)
        # 自动保存线程
        t3 = DBWriteThread.SaveThread(self)
        # 后台管理线程
        t4 = BackgroundControl.Control(self)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        reactor.listenUDP(portUDP, UDPProto.UDPProto(self))
        reactor.listenTCP(portTCP, TCPProto.TCPProtoFactory(self))
        reactor.run()


if __name__ == "__main__":
    m = MainTask()
    m.start()
