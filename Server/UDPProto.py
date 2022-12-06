import json

from twisted.internet import protocol


class UDPProto(protocol.DatagramProtocol):
    def __init__(self, maintask):
        super().__init__()
        self.maintask = maintask
        self.maintask.UDP = self
        print(self)

    def startProtocol(self):
        pass

    def datagramReceived(self, data, addr):
        try:
            x = data.decode("utf8")
            x = json.loads(x)
            print(x)
            if (x['data']['msg'] == ''):
                self.maintask.cips[x['data']['username']] = addr
                print(addr)
            elif (x['data']['msg'] == "#@players"):
                players = "当前在线玩家：" + ",".join(list(self.maintask.cips.keys()))
                self.transport.write(players.encode("utf8"), addr)
            elif (x['data']['username'] not in self.maintask.cips):
                self.transport.write("已断开连接，请重新连接".encode("utf8"), addr)
            else:
                self.maintask.pushRecvMsg((self, x))
        finally:
            pass
