import socket

import json

clientUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2.连接
clientUDP.connect(('127.0.0.1', 8090))

msg = {"data": {}}
if __name__ == '__main__':
    while True:
        say = input("要说的话：")
        msg["bt"] = 2
        msg["lt"] = 1
        msg["data"]["username"] = 123
        msg["data"]["msg"] = say
        clientUDP.sendto(json.dumps(msg).encode('utf8'), ('127.0.0.1', 8090))

        data, server_add = clientUDP.recvfrom(1024)
        print('\n' + data.decode('utf8'))