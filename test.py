from socket import *

client = socket(AF_INET,SOCK_DGRAM)

if __name__ == '__main__':
    data = "你好"
    client.sendto(data.encode('utf8'),('127.0.0.1',8090))
    data,server_add = client.recvfrom(1024)
    print(data.decode('utf8'),server_add)
    while True:
        pass