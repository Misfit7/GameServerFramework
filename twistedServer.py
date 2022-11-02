from twisted.internet import protocol
from twisted.internet import reactor

clients = {}

class Echo(protocol.Protocol):
    def connectionMade(self):
        clients[self] = ''

    def dataReceived(self, data):
        # 只要twisted一收到数据就会调用此方法dataReceived，收到数据后干什么，他就不知道了
        # 这里写的意思就是收到后在发回去给客户端
        msg = data.decode()
        msg = "you send a msg:" + msg
        # self.transport.write(msg.encode('utf-8'))
        msg2 = "someeone said to all:" + data.decode()

        for client in clients:
            if client == self:
                client.transport.write(msg.encode('utf-8'))
            else:
                client.transport.write(msg2.encode('utf-8'))


def server():
    factory = protocol.ServerFactory()
    # 服务器工厂，和客户端建立连接后定义的某些方法，比如发送数据或者文件
    # 除了这些，还有一些默认的方法，可以理解为定义一个基础的工厂类，比如
    # soceketserver方法中的setup方法，和finsh方法

    factory.protocol = Echo
    # 相当于socketserver中的handle，必须要写，每个客户端过来都会建立一个
    # 实例，然后就调用Echo这个方法

    reactor.listenTCP(9999, factory)
    # 相当于一个触发器，监听9999端口，把我们定义的基础类放在这里，和socketserver中一样

    reactor.run()


server()
