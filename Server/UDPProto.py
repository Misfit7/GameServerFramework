import json

from twisted.internet import protocol

class UDPProto(protocol.DatagramProtocol):
    def __init__(self,maintask):
        super().__init__()
        self.maintask=maintask

    def startProtocol(self):
        pass

    def datagramReceived(self, data, addr):
        x = data.decode("utf8")
        x = json.loads(x)
        print(x)
        if (x['data']['msg']==''):
            self.maintask.cips[x['data']['username']]=addr
        else:
            self.maintask.pushRecvMsg((self,x))
