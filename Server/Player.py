class Player():
    def __init__(self, username, userType):
        self.id = None
        self.uname = username
        self.lv = 1
        if (userType == 1):
            self.warrior()
            self.utype = "warrior"
        elif (userType == 2):
            self.witch()
            self.utype = "witch"
        elif (userType == 3):
            self.assassin()
            self.utype = "assassin"
        elif (userType == 4):
            self.shooter()
            self.utype = "shooter"
        self.coin = 0
        self.updateStatus = 0

    def warrior(self):
        self.maxhp = self.hp = 500
        self.maxmp = self.mp = 60
        self.atk = 8
        self.df = 6

    def witch(self):
        self.maxhp =self.hp = 420
        self.maxmp =self.mp = 100
        self.atk = 12
        self.df = 3

    def assassin(self):
        self.maxhp =self.hp = 480
        self.maxmp =self.mp = 60
        self.atk = 15
        self.df = 3

    def shooter(self):
        self.maxhp =self.hp = 450
        self.maxmp =self.mp = 65
        self.atk = 10
        self.df = 4
