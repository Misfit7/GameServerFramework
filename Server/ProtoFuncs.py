import json


class ProtoFuncs():
    @staticmethod
    def login(maintask, me, data):
        if (data['data']['username'] not in list(maintask.pMgr.keys())):
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
                maintask.waitclients.remove(me)
                clients[me] = pMgr[data['data']['username']]
            else:
                msg = {
                    "msg": data['data']['username'] + "，对不起，您的账号或密码错误。",
                    "status": 0
                }
        else:
            msg = {
                "msg": data['data']['username'] + "，对不起，账号已登陆。",
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
            del clients[me]
            del maintask.cips[data['data']['username']]
            maintask.waitclients.add(me)
        else:
            msg = {
                "msg": data['data']['username'] + "，对不起，请稍后再试。",
                "status": 0
            }
        print(msg)
        maintask.pushSendMsg(([me], json.dumps(msg).encode("utf8")))  # 数组

    @staticmethod
    def msgBroadcast(maintask, me, data):
        username = data['data']['username']
        msg = "%s 广播: %s" % (username, data['data']['msg'])
        print(msg)
        cips = list(maintask.cips.values())
        maintask.pushSendMsg((me, cips, msg.encode('utf8'), "UDP"))

    @staticmethod
    def msgPrivateChat(maintask, me, data):
        username = data['data']['username']
        takedname = data['data']['talked']
        for name in maintask.cips:
            if name == takedname:
                msg = "%s said to %s 悄悄话: %s" % (username, 'you', data['data']['msg'])
                print(msg)
                me.transport.write(msg.encode('utf8'), maintask.cips[takedname])
            elif name == username:
                msg = "%s said to %s 悄悄话: %s" % ('you', takedname, data['data']['msg'])
                print(msg)
                me.transport.write(msg.encode('utf8'), maintask.cips[username])

    @staticmethod
    def attack(maintask, me, data):
        username = data['data']['username']
        atkname = data['data']['atked']
        pMgr = maintask.pMgr
        pMgr[atkname].hp = pMgr[atkname].hp - pMgr[username].atk
        for name in pMgr:
            if name == atkname:
                msg = "%s attacked %s once, your hp reduce %s = %s " % (
                    username, 'you', pMgr[username].atk, pMgr[atkname].hp)
                print(msg)
                me.transport.write(msg.encode('utf8'), maintask.cips[atkname])
            elif name == username:
                msg = "%s attacked %s once, his hp reduce %s = %s " % (
                    'you', atkname, pMgr[username].atk, pMgr[atkname].hp)
                print(msg)
                me.transport.write(msg.encode('utf8'), maintask.cips[username])
