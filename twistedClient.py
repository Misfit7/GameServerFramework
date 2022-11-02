# from twisted.internet import reactor
# from twisted.internet import protocol
#
#
# class EchoClient(protocol.Protocol):
#     def connectionMade(self):
#         # 只要链接一建立，就会自动调用此方法
#         print("client send data to server")
#         msg = "hello world"
#         self.transport.write(msg.encode('utf-8'))
#
#     def dataReceived(self, data):
#         # 只要有数据收到，就会调用该方法，这个都是自动的
#         print("Server said", data)
#         self.transport.loseConnection()
#         # 这里收到数据后，打印数据，然后就关闭链接了,调用这个方法loseConnection，reactor会自动调用connectionLost方法
#
#     def connectionLost(self, reason):
#         print("Connection lost")
#
#
# class EehoFactory(protocol.ClientFactory):
#     protocol = EchoClient
#
#     # 相当于handle
#
#     def clientConnectionFailed(self, connector, reason):
#         # 如果连不上就会调用该方法，也是reactor中自动调用的
#         print("Connection failed - goodbye")
#         reactor.stop()
#
#     def clientConnectionLost(self, connector, reason):
#         # 如果连的过程中断开了，就会自动执行该方法，也是reactor方法自动调用的
#         print("Connection lost - goodbye")
#         reactor.stop()
#
#
# def client():
#     f = EehoFactory()
#     # 创建一个客户端的基类
#     reactor.connectTCP("localhost", 9000, f)
#     # 直接连接
#
#
# client()
