# import threading
# import time
# import queue
# import random
#
# exitFlag = 0
#
# class producer (threading.Thread):
#     def __init__(self, name, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.delay = delay
#
#     def producer(self):
#         xx=['苹果','梨子','鱼']
#         queueLock.acquire() #获得锁
#         if msgQueue.full()==False:
#             x1=random.randint(0,2)
#             msgQueue.put(xx[x1])    #生产物品
#             print("你生产了一个%s."%xx[x1])
#         else:
#             print("用户还未吃完.")
#         queueLock.release() #释放锁
#
#     def run(self):
#         while True:
#             self.producer()
#             time.sleep(self.delay)
#
# class consumer (threading.Thread):
#     def __init__(self, name, delay):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.delay = delay
#
#     def consumer(self):
#         queueLock.acquire() #获得锁
#         if msgQueue.empty()==False:
#             x1=msgQueue.get()    #生产物品
#             print("你吃了一个%s."%x1)
#         else:
#             print("生产者生产中.")
#         queueLock.release() #释放锁
#
#     def run(self):
#         while True:
#             self.consumer()
#             time.sleep(self.delay)
#
#
# queueLock=threading.Lock()
# msgQueue=queue.Queue(20)
# # 创建新线程
#
# thread1 = producer("工人1", 2)
# thread2 = producer("工人2", 3)
# thread3 = consumer("节食2", 2)
# thread4 = consumer("吃货3", 1)
#
# # 开启新线程
# x1=[thread1,thread2,thread3,thread4]
# for x in x1:
#     x.start()
# for x in x1:
#     x.join()
# print ("退出主线程")