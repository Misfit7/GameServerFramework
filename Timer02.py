import datetime
import threading
import time
import schedule

class Timer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.mgr={}
        self.mgr[1]=[self.printHello,self.printSay]
        self.mgr[5]=[self.printWorld]
        self.count=0

    def printHello(self):
        print("Hello")

    def printSay(self):
        print("???")

    def printWorld(self):
        print("world")

    def doMgr(self):
        for key in self.mgr:
            if self.count%key==0:
                for func in self.mgr[key]:
                    func()

    def run(self):
        flag=False
        while True:
            self.count=self.count+1
            # self.doMgr()
            dt=datetime.datetime.now()
            if dt.minute==36 and flag==False:
                print('现在是36')
                flag=True
            time.sleep(1)

if __name__ == '__main__':
    xx=Timer()
    xx.start()