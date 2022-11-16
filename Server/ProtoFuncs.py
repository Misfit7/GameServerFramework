import json


class ProtoFuncs():
    @staticmethod
    def login(maintask, me, data):
        clients = maintask.clients
        pMgr = maintask.pMgr
        access = pMgr.LoginPlayer(maintask.conn, data)
        # 登陆成功
        if access != 0:
            msg = {
                "msg": data['data']['username'] + " 登陆成功，欢迎您。",
                "status": 1
            }
            # 生成新角色
            pMgr[data['data']['username']] = access
            pMgr[data['data']['username']].logstatus = 1
            # 玩家角色和用户绑定
            clients[me] = pMgr[data['data']['username']]
        else:
            msg = {
                "msg": data['data']['username'] + "，对不起，您的账号或密码错误。",
                "status": 0
            }
        print(msg)
        maintask.pushSendMsg(([me], json.dumps(msg).encode("utf8")))  # 数组

    @staticmethod
    def register(maintask, me, data):
        pMgr = maintask.pMgr
        access = pMgr.RegisterPlayer(maintask.conn, data)
        # 注册成功
        if access == 1:
            msg = {
                "msg": data['data']['username'] + "，注册成功。",
                "status": 0
            }
        else:
            msg = {
                "msg": data['data']['username'] + "，注册失败，您注册的账号已存在或输入有误。",
                "status": 0
            }
        print(msg)
        maintask.pushSendMsg(([me], json.dumps(msg).encode("utf8")))  # 数组

    @staticmethod
    def logout(maintask, me, data):
        clients = maintask.clients
        pMgr = maintask.pMgr
        access = pMgr.LogoutPlayer(maintask, data)
        # 登出成功
        if access != 0:
            msg = {
                "msg": data['data']['username'] + " 退出成功。",
                "status": 1
            }
            # 集合中删除角色
            del pMgr[data['data']['username']]
            # 玩家角色和用户解绑
            clients[me] = None
        else:
            msg = {
                "msg": data['data']['username'] + "，对不起，请稍后再试。",
                "status": 0
            }
        print(msg)
        maintask.pushSendMsg(([me], json.dumps(msg).encode("utf8")))  # 数组

    @staticmethod
    def msgBroadcast(maintask, me, data):
        clients = maintask.clients
        p = clients[me]
        username = p.uname
        msg = "%s said to all: %s" % (username, data['data']['msg'])
        print(msg)
        clts = list(clients.values())
        maintask.pushSendMsg((clts, msg.encode('utf8')))

    @staticmethod
    def msgPrivateChat(maintask, me, data):
        clients = maintask.clients
        username = clients[me].uname
        takedname = data['data']['talked']
        for client in clients:
            if clients[client].uname == takedname:
                msg = "%s said to %s: %s" % (username, takedname, data['data']['msg'])
                print(msg)
                client.transport.write(msg.encode('utf8'))
            elif client == me:
                msg = "%s said to %s qiaoqiao_ly: %s" % ('you', takedname, data['data']['msg'])
                client.transport.write(msg.encode('utf8'))

    @staticmethod
    def killLove(maintask, me, data):
        clients = maintask.clients
        username = clients[me].uname
        takedname = data['data']['talked']
        for client in clients:
            if clients[client].uname == takedname:
                clients[client].hp = clients[client].hp + 20
                msg = "%s like you, add your hp %s points: %s" % (username, 20, data['data']['msg'])
                print(msg)
                client.transport.write(msg.encode('utf8'))
            elif client == me:
                msg = "%s said to %s qiaoqiao_ly: %s" % ('you', takedname, data['data']['msg'])
                client.transport.write(msg.encode('utf8'))
