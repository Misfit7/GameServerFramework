import json
import socket
import os

import Menu

# 1.建立连接
clientConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.连接
clientConn.connect(('127.0.0.1', 9999))

m=Menu.Menu()

# 3.通信

def inputAccount():
    while True:
        userName = input('请输入账号：')
        userPassword = input('请输入密码：')
        if len(userName)>
        msg = {
            "bt": 1,
            "lt": 3,
            "code": 0,
            "data": {
                "username": userName,
                "password": userPassword
            }
        }
        return json.dumps(msg)

while True:
    print(m.mainMenu)
    choice = input('请输入选项：').strip()

    # 登陆
    if choice == "1":
        json_str = inputAccount()
    # 发送
    clientConn.send(json_str.encode(encoding='utf-8'))

    # 注册
    if choice == "2":
        json_str = inputAccount()
    # 发送
    clientConn.send(json_str.encode(encoding='utf-8'))

    # 接收
    data = clientConn.recv(1024)
    print(data.decode('utf-8'))

    if choice == "5":
        # 关闭连接
        clientConn.close()

