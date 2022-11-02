import json

from twisted.internet import reactor, protocol

import MainTask


class Echo(protocol.Protocol):
    def connectionMade(self):  # 连接建立
        remote = self.transport.getPeer()  # 获取远端ip
        local = self.transport.getHost()  # 获取本机ip

        print("remote", remote, remote.host)
        print("local", local)
        return super().connectionMade()

    def dataReceived(self, data):
        x = data.decode("utf8")
        x = json.loads(x)
        print(x['bt'], x['lt'], x['data'])
        m.funcMgr.doProto(x['bt'],x['lt'],x)


    def connectionLost(self, reason):
        print('client closed', self.transport.getPeer(), reason)
        return super().connectionLost(reason)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

m=MainTask.MainTask()
m.regProtoAll()
reactor.listenTCP(9999, EchoFactory())
reactor.run()
