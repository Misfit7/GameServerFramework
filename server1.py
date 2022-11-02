import socketserver

class MyResquestHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)#如果是tcp协议，self.request相当于conn
        print(self.client_address)

        while True:
            try:
                msg = self.request.recv(1024)
                if len(msg) == 0:
                    break
                self.request.send(msg.upper())
            except Exception:
                break

        self.request.close()


s = socketserver.ThreadingTCPServer(('127.0.0.1',8081),MyResquestHandle)
s.serve_forever()