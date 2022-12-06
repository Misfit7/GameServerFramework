import json
import os
import pickle
import socket
import _thread
import time
from pynput.keyboard import Key, Listener, Controller

import Menu

clientUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# clientUDP.connect(('127.0.0.1', 8090))
# UDP = ('127.0.0.1', 8090)
UDP = ('119.91.27.246', 8090)

clientTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientTCP.connect(('127.0.0.1', 9999))
clientTCP.connect(('119.91.27.246', 9999))

m = Menu.Menu()

# 3.通信

# 输入账号密码
userName = None
status = 0


# 发送
def TCPSendMsg(msg):
    json_str = json.dumps(msg)
    print(json_str)
    clientTCP.send(json_str.encode(encoding='utf-8'))


# 接收UDP消息
def UDPRecvMsg():
    while True:
        data, server_add = clientUDP.recvfrom(1024)
        data = data.decode('utf8')
        print('\n' + data)
        if (data == "已断开连接，请重新连接"):
            os._exit(0)


# 接收TCP数据
def TCPRecvData():
    data = clientTCP.recv(1024)
    try:
        data = json.loads(data)
        print(data["msg"])
        return data["status"]
    finally:
        pass


def inputAccount():
    while True:
        global userName
        msg = {"data": {}}
        userName = input("请输入账号（字母数字）：")
        if not (0 < len(userName.encode("utf8")) <= 24 and userName.isalnum()):
            print("账号输入错误，请重新输入")
            continue
        while True:
            userPassword = input("请输入密码（字母数字8-16位）：")
            if 8 <= len(userPassword.encode("utf8")) <= 16 and userPassword.isalnum():
                msg["data"]["username"] = userName
                msg["data"]["password"] = userPassword
                return msg
            else:
                print("密码输入错误，请重新输入")


def mainTask():
    print(m.mainMenu)
    while True:
        choice = input("请输入选项：").strip()

        # 登陆
        if choice == "1":
            msg = inputAccount()
            msg["bt"] = 1
            msg["lt"] = 1

        # 注册
        elif choice == "2":
            msg = inputAccount()
            # 发送
            while True:
                usertype = input("职业选择：1、战士 2、法师 3、刺客 4、射手\n").strip()
                if (usertype not in ("1", "2", "3", "4")):
                    print("输入错误")
                    continue
                msg["bt"] = 1
                msg["lt"] = 2
                msg["data"]["usertype"] = int(usertype)
                break

        # 退出游戏
        elif choice == "3":
            # 关闭连接
            clientTCP.close()
            print("已退出游戏")
            return 3

        else:
            print("选项输入错误")
            continue
        TCPSendMsg(msg)
        return TCPRecvData()


def secTask():
    print(m.funcMenu)
    msg = {"data": {}}
    choice = input("请输入选项：").strip()

    # 广播
    if choice == "1":
        say = input("要说的话：")
        msg["bt"] = 2
        msg["lt"] = 1
        msg["data"]["username"] = userName
        msg["data"]["msg"] = say
        clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)

    # 私聊
    elif choice == "2":
        msg["data"]["msg"] = "#@players"
        clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)
        msg["data"]["msg"] = None
        while True:
            talked = input("要私聊的用户名：")
            if (talked == userName):
                print("对象不能为自己")
                continue
            say = input("要说的话：")
            msg["bt"] = 2
            msg["lt"] = 2
            msg["data"]["username"] = userName
            msg["data"]["talked"] = talked
            msg["data"]["msg"] = say
            clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)
            break

    # 充值
    elif choice == "3":
        msg["bt"] = 4
        msg["lt"] = 1
        money = input("要充值的金额：")
        msg["data"]["username"] = userName
        msg["data"]["money"] = money
        TCPSendMsg(msg)
        TCPRecvData()

    # 动作
    elif choice == "4":
        thirdMenu()

    # 退出角色
    elif choice == "5":
        msg["bt"] = 1
        msg["lt"] = 3
        msg["data"]["username"] = userName
        TCPSendMsg(msg)
        rec = TCPRecvData()
        return rec


def thirdMenu():
    while True:
        msg = {"data": {}}
        print(m.actMenu)
        choice = input("请输入选项：").strip()
        msg["data"]["msg"] = "#@players"
        clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)
        msg["data"]["msg"] = None

        # 攻击
        if (choice == '1'):
            while True:
                atkname = input("请输入攻击对象：")
                if (atkname == userName):
                    print("对象不能为自己")
                    continue
                msg["bt"] = 3
                msg["lt"] = 1
                msg["data"]["username"] = userName
                msg["data"]["atked"] = atkname
                clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)
                break

        # 恢复
        elif (choice == '2'):
            while True:
                atkname = input("请输入治疗对象：")
                msg["bt"] = 3
                msg["lt"] = 2
                msg["data"]["username"] = userName
                msg["data"]["atked"] = atkname
                clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)
                break

        # 状态
        elif (choice == '3'):
            msg["bt"] = 3
            msg["lt"] = 3
            msg["data"]["username"] = userName
            clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)

        # 加点
        elif (choice == '4'):
            msg["bt"] = 3
            msg["lt"] = 4
            msg["data"]["username"] = userName
            msg["data"]["data"] = input("加点方向 1、生命 2、攻击 3、防御：")
            clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)

        # 返回
        elif (choice == '5'):
            break


def on_press(key):
    msg = {"data": {}}
    msg["bt"] = 3
    msg["lt"] = 5
    msg["data"]["username"] = userName
    if key == Key.up:
        msg["data"]["msg"] = "up"
    elif key == Key.down:
        msg["data"]["msg"] = "down"
    elif key == Key.left:
        msg["data"]["msg"] = "left"
    elif key == Key.right:
        msg["data"]["msg"] = "right"
    elif str(key) == "'t'":
        return False
    clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)


def Move():
    with Listener(on_press=on_press) as listener:
        listener.join()


def newThread():
    try:
        _thread.start_new_thread(UDPRecvMsg, ())
    except:
        print("Error: 无法启动线程")


if __name__ == '__main__':
    flag = 0
    while True:
        status = mainTask()
        if status == 1:
            msg = {"data": {}}
            msg["data"]["username"] = userName
            msg["data"]["msg"] = ''
            clientUDP.sendto(json.dumps(msg).encode('utf8'), UDP)
            if (flag == 0):
                newThread()
                flag = 1
            while status == 1:
                Move()
                ret = secTask()
                if (ret == 1301):
                    break
        elif status == 3:
            break
