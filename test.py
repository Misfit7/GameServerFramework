import json
import socket

clientUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == '__main__':
    msg = {"data": {}}
    msg["data"]["username"] = "userName"
    msg["data"]["msg"] = ''
    clientUDP.sendto(json.dumps(msg).encode('utf8'),('127.0.0.1',8090))
    while True:
        data, server_add = clientUDP.recvfrom(1024)
        data = data.decode('utf8')
        print('\n' + data)
