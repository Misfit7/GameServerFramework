import json
import pickle

from twisted.internet import protocol


class UDPProto(protocol.DatagramProtocol):
    def __init__(self, maintask):
        super().__init__()
        self.maintask = maintask

    def startProtocol(self):
        pass

    def datagramReceived(self, data, addr):
        x = data.decode("utf8")
        x = json.loads(x)
        print(x)
        try:
            if (x['data']['msg'] == ''):
                self.maintask.cips[x['data']['username']] = addr

            elif (x['data']['msg'] == "#@players"):
                players = "当前在线玩家：" + ",".join(list(self.maintask.cips.keys()))
                self.transport.write(players.encode("utf8"), addr)
            else:
                self.maintask.pushRecvMsg((self, x))
        finally:
            pass