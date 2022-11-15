class FuncMgr(dict):
    def __init__(self):
        super()

    def regProto(self,bt,lt,func):
        t=(bt<<16)+lt
        self[t]=func

    def doProto(self,maintask,me,data):
        bt=data['bt']
        lt=data['lt']
        t=(bt<<16)+lt
        if t in self:
            self[t](maintask,me,data)