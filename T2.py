# import threading
# import time
# import queue
# import random
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, name, delay,isWorker):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.delay = delay
#         self.isWorker=isWorker
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
#             if  self.isWorker:
#                 self.producer()
#             else:
#                 self.consumer()
#             time.sleep(self.delay)
#
#
# queueLock=threading.Lock()
# msgQueue=queue.Queue(20)
# # 创建新线程
# thread1 = myThread("工人1", 1,True)
# thread2 = myThread("节食2", 2,False)
# thread3 = myThread("吃货3", 1,False)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread3.start()
# thread1.join()
# thread2.join()
# thread3.join()
# print ("退出主线程")