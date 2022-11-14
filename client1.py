import json
import socket

# 1.买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.拨通电话
phone.connect(('127.0.0.1', 9999))

# 3.通信
while True:
    msg = input('请输入：').strip()
    if len(msg) == 0:
        continue

    if msg == "1":
        msg = {
            "bt": 1,
            "lt": 3,
            "code": 0,
            "data": {
                "username": "zhangsan",
                "password": "123"
            }
        }
        json_str = json.dumps(msg)

    phone.send(json_str.encode(encoding='utf-8'))

    data = phone.recv(1024)

    print(data.decode('utf-8'))

# 关闭连接必选
phone.close()
