from twisted.internet import protocol

class UDPProto(protocol.DatagramProtocol):
    def startProtocol(self):
        pass

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data.decode('utf8'), addr))
        self.transport.write(data, addr)

# class UDPProtoFactory(protocol.Factory):
#     def __init__(self,maintask):
#         super().__init__()
#
#     def buildProtocol(self, addr):
#         return UDPProto(self)
