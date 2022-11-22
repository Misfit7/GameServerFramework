import json

from twisted.internet import protocol


class TCPProto(protocol.Protocol):
    def __init__(self, factory):
        super().__init__()
        self.factory = factory
        self.maintask = self.factory.maintask

    def connectionMade(self):  # 连接建立
        remote = self.transport.getPeer()  # 获取远端ip
        local = self.transport.getHost()  # 获取本机ip

        print("remote", remote, remote.host)
        print("local", local)
        self.maintask.waitclients.add(self)
        return super().connectionMade()

    def dataReceived(self, data):
        x = data.decode("utf8")
        x = json.loads(x)
        print(x['bt'], x['lt'], x['data'])
        self.maintask.pushRecvMsg((self, x))

    def connectionLost(self, reason):
        print('client closed', self.transport.getPeer(), reason)
        try:
            self.maintask.pMgr[self.maintask.clients[self].uname].updateStatus=0
            self.maintask.pMgr.mq.save(self.maintask,self.maintask.clients[self].uname)
            del self.maintask.pMgr[self.maintask.clients[self].uname]
        finally:
            try:
                del self.maintask.cips[self.maintask.clients[self].uname]
            finally:
                try:
                    self.maintask.waitclients.remove(self)
                finally:
                    try:
                        del self.maintask.clients[self]
                    finally:
                        return super().connectionLost(reason)


class TCPProtoFactory(protocol.Factory):
    def __init__(self, maintask):
        super().__init__()
        self.maintask = maintask

    def buildProtocol(self, addr):
        return TCPProto(self)
