class Player():
    def __init__(self, username, userType):
        self.id = None
        self.uname = username
        self.utype = userType
        self.lv = 1
        if (userType == 1):
            self.warrior()
        elif (userType == 2):
            self.witch()
        elif (userType == 3):
            self.assassin()
        elif (userType == 4):
            self.shooter()
        self.coin = 0
        self.money = 0
        self.updateStatus = None
        self.logStatus = None

    def warrior(self):
        self.hp = 500
        self.mp = 60
        self.atk = 8
        self.df = 6

    def witch(self):
        self.hp = 420
        self.mp = 100
        self.atk = 12
        self.df = 3

    def assassin(self):
        self.hp = 480
        self.mp = 60
        self.atk = 15
        self.df = 3

    def shooter(self):
        self.hp = 450
        self.mp = 65
        self.atk = 10
        self.df = 4
