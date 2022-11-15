import Player

class PlayerMgr(dict):
    def __init__(self):
        super().__init__()
        playername="zs"
        playertype=1
        p= Player.Player(playername, playertype)
        self[playername]=p

pmgr=PlayerMgr()
print(pmgr["zs"].hp)