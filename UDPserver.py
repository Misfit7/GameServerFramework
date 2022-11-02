# import socketserver
#
# # 自定义类来实现通信循环
# class MyUDPHander(socketserver.BaseRequestHandler):
#     def handle(self):
#         data,sock = self.request
#         sock.sendto(data.upper(),self.client_address)
#
# if __name__ == '__main__':
#     server = socketserver.ThreadingUDPServer(('127.0.0.1', 8080), MyUDPHander)
#     server.serve_forever()  # 链接循环