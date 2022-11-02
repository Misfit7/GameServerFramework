import threading
import time
import queue
import random


class producer(threading.Thread):
    def __init__(self, mainTask, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.mainTask = mainTask

    def producer(self):
        queueLock = self.mainTask.queueLock
        msgQueue = self.mainTask.msgQueue
        xx = ['苹果', '梨子', '鱼']
        queueLock.acquire()  # 获得锁
        if msgQueue.full() == False:
            x1 = random.randint(0, 2)
            msgQueue.put(xx[x1])  # 生产物品
            print("你生产了一个%s." % xx[x1])
        else:
            print("用户还未吃完.")
        queueLock.release()  # 释放锁

    def run(self):
        while True:
            self.producer()
            time.sleep(self.delay)


class consumer(threading.Thread):
    def __init__(self, mainTask, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.mainTask = mainTask

    def consumer(self):
        queueLock = self.mainTask.queueLock
        msgQueue = self.mainTask.msgQueue
        queueLock.acquire()  # 获得锁
        if msgQueue.empty() == False:
            x1 = msgQueue.get()  # 生产物品
            print("你吃了一个%s." % x1)
        else:
            print("生产者生产中.")
        queueLock.release()  # 释放锁

    def run(self):
        while True:
            self.consumer()
            time.sleep(self.delay)


class mainTask():
    def __init__(self):
        self.queueLock = threading.Lock()
        self.msgQueue = queue.Queue(20)

    def startThread(self):
        thread1 = producer(self, "工人1", 2)
        thread2 = producer(self, "工人2", 3)
        thread3 = consumer(self, "节食2", 2)
        thread4 = consumer(self, "吃货3", 1)

        # 开启新线程
        self.threads = [thread1, thread2, thread3, thread4]
        for x in self.threads:
            x.start()
        for x in self.threads:
            x.join()


if __name__ == '__main__':
    m = mainTask()
    m.startThread()
