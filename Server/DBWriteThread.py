#!/usr/bin/python3

import threading
import time


# 自动保存
class SaveThread(threading.Thread):
    def __init__(self, maintask, spanTime=120):
        threading.Thread.__init__(self)
        self.maintask = maintask
        self.spanTime = spanTime

    def run(self):
        while True:
            pMgr = self.maintask.pMgr
            for p in list(pMgr.keys()):
                # print(pMgr[p].uname + ":", pMgr[p].updateStatus)
                if (pMgr[p].updateStatus == 1):
                    pMgr.mq.save(self.maintask, p)
                    pMgr[p].updateStatus = 0
                    print(p + "自动保存成功")
                else:
                    pMgr[p].updateStatus -= 1
                    if (pMgr[p].updateStatus <= -3):
                        for c in list(self.maintask.clients.keys()):
                            if (self.maintask.clients[c] == pMgr[p]):
                                c.connectionLost(None)
            time.sleep(self.spanTime)  # 2分钟执行一次
