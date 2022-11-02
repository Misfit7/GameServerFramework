import enum

class TimerType(enum.Enum):
    byNow=1
    byAt=2
    byWeekAt=3

class ATimer():
    def __init__(self,func,seconds,span,timerType,repeatType=1):
        self.func=func
        self.seconds=seconds
        self.timerType=timerType
        self.repeatType=repeatType

class ATimerMgr():
    def __init__(self):
        self.t1={}  #当前时间
        self.t2={}  #时刻

    def addTimer(self,atimer):
        if atimer.timeType=='':
            self.t1[atimer.seconds]=atimer
        else:
            self.t2[atimer.seconds]=atimer

    def doTimer(self):
        for x in self.t1:
            pass
        for x in self.t2:
            pass