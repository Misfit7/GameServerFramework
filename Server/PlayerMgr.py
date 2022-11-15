import Player
import Mysql

class PlayerMgr(dict):
    def __init__(self):
        super().__init__()
        self.mq= Mysql.GameSql()

    # 登陆
    def LoginPlayer(self,conn,data):
        return self.mq.login(conn,data)

    # 注册
    def RegisterPlayer(self,conn,data):
        return self.mq.register(conn,data)

    # 登出
    def LogoutPlayer(self,conn,data):
        pass
        # self.SavePlayer()
        # return self.mq.logout(conn,data)

    # 玩家对象
    def NewPlayer(self,playername,playerType):
        p= Player.Player(playername, playerType)
        return p

    def LoadPlayer(self,playername):
        pass

    def SavePlayer(self,playername):
        pass

    def SaveAll(self):
        pass

    def LoadAll(self):
        pass