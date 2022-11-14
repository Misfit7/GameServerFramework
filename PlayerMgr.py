import Player
class PlayerMgr(dict):

    def NewPlayer(self,playername,playerType):
        p=Player.Player(playername,1)
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