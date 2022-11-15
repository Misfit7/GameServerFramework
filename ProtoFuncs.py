class ProtoFuncs():
    @staticmethod
    def login(maintask, me, data):
        clients=maintask.clients
        pMgr=maintask.pMgr
        pMgr.LoginPlayer(maintask.conn,data)
        msg = data['data']['username'] + ", welcome, you are logged."
        p = pMgr.NewPlayer(data['data']['username'], 1)
        clients[me] = p
        print(msg)
        # me.transport.write(msg.encode('utf8'))
        maintask.pushSendMsg(([me],msg.encode('utf8'))) #数组

    @staticmethod
    def msgBroadcast(maintask, me, data):
        clients=maintask.clients
        p = clients[me]
        username = p.uname
        msg = "%s said to all: %s" % (username, data['data']['msg'])
        print(msg)
        # for client in clients:
        #     client.transport.write(msg.encode('utf8'))
        clts=list(clients.values())
        maintask.pushSendMsg((clts,msg.encode('utf8')))

    @staticmethod
    def msgPrivateChat(maintask, me, data):
        clients=maintask.clients
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
        clients=maintask.clients
        username = clients[me].uname
        takedname = data['data']['talked']
        for client in clients:
            if clients[client].uname == takedname:
                clients[client].hp=clients[client].hp+20
                msg = "%s like you, add your hp %s points: %s" % (username, 20, data['data']['msg'])
                print(msg)
                client.transport.write(msg.encode('utf8'))
            elif client == me:
                msg = "%s said to %s qiaoqiao_ly: %s" % ('you', takedname, data['data']['msg'])
                client.transport.write(msg.encode('utf8'))