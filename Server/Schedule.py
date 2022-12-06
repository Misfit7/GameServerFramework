import threading
import time
from schedule import every, run_pending
from datetime import timedelta
import socket

# clientUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def job1(maintask):
    msg = "今日充值活动已开启"
    # print(msg)
    for cip in maintask.cips:
        # print(cips[cip])
        maintask.UDP.transport.write(msg.encode('utf8'), maintask.cips[cip])


def job2(maintask):
    # 运行任务至某时间
    every().seconds.until(timedelta(seconds=6)).do(job2_1, maintask=maintask)


def job2_1(maintask):
    msg = "您在在线活动中获得金币+10"
    print(msg)
    for cip in maintask.cips:
        # print(cips[cip])
        maintask.pMgr[cip].coin += 10
        maintask.UDP.transport.write(msg.encode('utf8'), maintask.cips[cip])


class Schedule(threading.Thread):
    def __init__(self, maintask):
        threading.Thread.__init__(self)
        self.maintask = maintask

    def run(self):
        every(60).seconds.do(job1, self.maintask)
        every().minutes.at(":00").do(job2, maintask=self.maintask)
        while True:
            run_pending()
            time.sleep(1)
