import socket

#1.买手机
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2.拨通电话
phone.connect(('127.0.0.1',8081))

#3.通信
while True:
    msg = input('请输入：').strip()
    if len(msg) == 0:
        continue

    phone.send(msg.encode('utf-8'))

    data = phone.recv(1024)


    print(data.decode('utf-8'))


#关闭连接必选
phone.close()