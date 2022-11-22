import threading
import time
import schedule
import socket

clientUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def job1(cips):
    msg = "今日充值活动已开启"
    print(msg)
    for cip in cips:
        # print(cips[cip])
        clientUDP.sendto(msg.encode('utf8'), cips[cip])

# @repeat(every(6).seconds)
# def job2():
#     end = datetime.now()
#     time = int((end - start).seconds/60)
#     print("您已在线",time,"分钟，金币+10")

# @repeat(every(6).seconds)
# def job2():
#     end = datetime.now()
#     time = int((end - start).seconds/60)
#     print("您已在线",time,"分钟，金币+10")


class Schedule(threading.Thread):
    def __init__(self, maintask):
        threading.Thread.__init__(self)
        self.maintask = maintask

    def run(self):
        schedule.every(15).seconds.do(job1, self.maintask.cips)
        while True:
            schedule.run_pending()
            time.sleep(1)
