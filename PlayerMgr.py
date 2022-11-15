import Player
import Mysql

class PlayerMgr(dict):
    def LoginPlayer(self,conn,data):
        cursor=conn.cursor()

    def NewPlayer(self,playername,playerType):
        p=Player.Player(playername,playerType)
        self[playername]=p
        return p

    def LoadPlayer(self,playername):
        pass

    def SavePlayer(self,playername):
        pass

    def SaveAll(self):
        pass

    def LoadAll(self):
        pass