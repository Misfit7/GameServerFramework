import Player
import Mysql


class PlayerMgr(dict):
    def __init__(self):
        super().__init__()
        self.mq = Mysql.GameSql()

    # 登陆
    def LoginPlayer(self, conn, data):
        return self.mq.login(conn, data)

    # 注册
    def RegisterPlayer(self, conn, data):
        return self.mq.register(conn, data)

    # 登出
    def LogoutPlayer(self, maintask, data):
        return self.mq.logout(maintask,data)

    # 玩家对象
    def NewPlayer(self, playername, playerType):
        p = Player.Player(playername, playerType)
        return p

    def SavePlayer(self, maintask, data):
        self.mq.save(maintask,data)
