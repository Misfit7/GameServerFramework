import socketserver

# 自定义类来实现通信循环
class MyUDPHander(socketserver.BaseRequestHandler):
    def handle(self):
        data,sock = self.request
        print(data.decode('utf8'),self.client_address)
        sock.sendto(data.upper(),self.client_address)

if __name__ == '__main__':
    server = socketserver.ThreadingUDPServer(('127.0.0.1', 8090), MyUDPHander)
    server.serve_forever()  # 链接循环