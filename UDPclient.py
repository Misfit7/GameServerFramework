from socket import *

client = socket(AF_INET,SOCK_DGRAM)

while True:
    client.sendto(b'hello',('127.0.0.1',8080))
    data,server_add = client.recvfrom(1024)
    print(data)