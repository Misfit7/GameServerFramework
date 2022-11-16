import json
import socket

import Menu

# 1.建立连接
clientConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.连接
clientConn.connect(('127.0.0.1', 9999))

m = Menu.Menu()

# 3.通信

# 输入账号密码
userName = None

msg = {
    "bt": None,
    "lt": None,
    "code": None,
    "data": {
    }
}


def sendAndRecv(msg):
    json_str = json.dumps(msg)
    print(json_str)
    # 发送
    clientConn.send(json_str.encode(encoding='utf-8'))
    # 接收
    data = clientConn.recv(1024)
    data = json.loads(data)
    print(data["msg"])
    return data["status"]


def inputAccount():
    while True:
        global userName
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
    global msg
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
            clientConn.close()
            print("已退出游戏")
            return 3

        else:
            print("选项输入错误")
            continue

        return sendAndRecv(msg)


def secTask():
    global msg
    print(m.funcMenu)
    choice = input("请输入选项：").strip()

    #
    if choice == "1":
        pass

    #
    elif choice == "2":
        pass

    #
    elif choice == "3":
        pass

    #
    elif choice == "4":
        pass

    #
    elif choice == "5":
        msg["bt"] = 1
        msg["lt"] = 3
        msg["username"] = userName
        return sendAndRecv(msg)


if __name__ == '__main__':
    while True:
        status = mainTask()
        if status == 1:
            while True:
                if (secTask() == 1):
                    break
        elif status == 3:
            break
