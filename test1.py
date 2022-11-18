from twisted.internet import protocol, reactor

import json

class UDPProto(protocol.DatagramProtocol):
    def startProtocol(self):
        pass

    def datagramReceived(self, data, addr):
        x = data.decode("utf8")
        x = json.loads(x)
        print(x['bt'], x['lt'], x['data'])
        print(addr)
        self.transport.write(x,addr)

reactor.listenUDP(8090, UDPProto())
reactor.run()