import json

import AliPay

class ProtoFuncs():
    @staticmethod
    def login(maintask, me, data):
        if (data['data']['username'] not in list(maintask.pMgr.keys())):
            # 登陆成功
            clients = maintask.clients
            pMgr = maintask.pMgr
            access = pMgr.LoginPlayer(maintask.conn, data)
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
                    "status": 1101
                }
        else:
            msg = {
                "msg": data['data']['username'] + "，对不起，账号已登陆。",
                "status": 1102
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
                "status": 1201
            }
        else:
            msg = {
                "msg": data['data']['username'] + "，注册失败，您注册的账号已存在或输入有误。",
                "status": 1202
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
                "status": 1301
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
                "status": 1302
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
        delta = pMgr[username].atk - pMgr[atkname].df
        pMgr[atkname].hp = pMgr[atkname].hp - delta
        if (pMgr[atkname].hp > 0):
            for name in pMgr:
                if name == atkname:
                    msg = "%s attacked %s once, your hp reduce %s = %s " % (
                        username, 'you', delta, pMgr[atkname].hp)
                    print(msg)
                    me.transport.write(msg.encode('utf8'), maintask.cips[atkname])
                elif name == username:
                    msg = "%s attacked %s once, his hp reduce %s = %s " % (
                        'you', atkname, delta, pMgr[atkname].hp)
                    print(msg)
                    me.transport.write(msg.encode('utf8'), maintask.cips[username])
        elif (pMgr[atkname].hp <= 0):
            for name in pMgr:
                if name == atkname:
                    msg = "%s killed %s, your hp reduce %s = %s " % (
                        username, 'you', delta, pMgr[atkname].hp)
                    print(msg)
                    me.transport.write(msg.encode('utf8'), maintask.cips[atkname])
                elif name == username:
                    msg = "%s killed %s, his hp reduce %s = %s " % (
                        'you', atkname, delta, pMgr[atkname].hp)
                    print(msg)
                    me.transport.write(msg.encode('utf8'), maintask.cips[username])
            pMgr[atkname].hp = pMgr[atkname].maxhp
        pMgr[atkname].updateStatus = 1

    @staticmethod
    def heal(maintask, me, data):
        username = data['data']['username']
        atkname = data['data']['atked']
        pMgr = maintask.pMgr
        pMgr[atkname].hp = pMgr[atkname].hp + pMgr[username].atk
        pMgr[username].mp = pMgr[username].mp - 10
        if (pMgr[atkname].hp > pMgr[atkname].maxhp):
            pMgr[atkname].hp = pMgr[atkname].maxhp
        for name in pMgr:
            if name == atkname:
                msg = "%s healed %s once, your hp add %s = %s" % (
                    username, 'you', pMgr[username].atk, pMgr[atkname].hp)
                print(msg)
                me.transport.write(msg.encode('utf8'), maintask.cips[atkname])
            elif name == username:
                msg = "%s healed %s once, his hp add %s = %s, your mp reduce %s = %s" % (
                    'you', atkname, pMgr[username].atk, pMgr[atkname].hp, 10, pMgr[username].mp)
                print(msg)
                me.transport.write(msg.encode('utf8'), maintask.cips[username])
        pMgr[atkname].updateStatus = 1

    @staticmethod
    def playerStatus(maintask, me, data):
        username = data['data']['username']
        p = maintask.pMgr[username]
        p.skills = p.lv - p.conskills
        msg = "your hp=%s/%s, mp=%s/%s, atk=%s, def=%s, lv=%s, skills=%s, type=%s, money=%s, coin=%s" % (
            p.hp, p.maxhp, p.mp, p.maxmp, p.atk, p.df, p.lv, p.skills, p.utype, p.money, p.coin
        )
        me.transport.write(msg.encode('utf8'), maintask.cips[username])

    @staticmethod
    def playerSkills(maintask, me, data):
        username = data['data']['username']
        p = maintask.pMgr[username]
        if p.skills > 0:
            if data['data']['data'] == '1':
                p.maxhp += 50
                p.skills -= 1
                p.conskills += 1
                msg = "加点成功，最大生命值为%s" % (p.maxhp)
            elif data['data']['data'] == '2':
                p.atk += 5
                p.skills -= 1
                p.conskills += 1
                msg = "加点成功，攻击力为%s" % (p.atk)
            elif data['data']['data'] == '3':
                p.df += 2
                p.skills -= 1
                p.conskills += 1
                msg = "加点成功，防御值为%s" % (p.df)
            else:
                msg = "技能点数不足"
        else:
            msg = "技能点数不足"
        me.transport.write(msg.encode('utf8'), maintask.cips[username])

    @staticmethod
    def playerMove(maintask, me, data):
        username = data['data']['username']
        p = maintask.pMgr[username]
        if data['data']['msg'] == "up":
            p.location["y"] += 1
        elif data['data']['msg'] == "down":
            p.location["y"] -= 1
        elif data['data']['msg'] == "left":
            p.location["x"] -= 1
        elif data['data']['msg'] == "right":
            p.location["x"] += 1
        msg = "你向" + data['data']['msg'] + "移动了，当前位置：" + str(p.location)
        me.transport.write(msg.encode('utf8'), maintask.cips[username])

    @staticmethod
    def charge(maintask, me, data):
        username = data['data']['username']
        out_order_no, url = AliPay.ali_Pay(username, data['data']['money'])
        msg = {
            'msg': url,
            "status": 41001
        }

        maintask.order[out_order_no] = username
        print(msg)
        maintask.pushSendMsg(([me], json.dumps(msg).encode("utf8")))  # 数组

    @staticmethod
    def chargeSuccess(maintask, me, data):
        out_order_no, total_amount = AliPay.pay_result(data['data']['msg'])
        username = maintask.order[out_order_no]
        p = maintask.pMgr[username]
        p.money += total_amount
        msg = username + "恭喜您成功充值" + str(total_amount) + "元余额"
        maintask.UDP.transport.write(msg.encode('utf8'), maintask.cips[username])
        print(msg)