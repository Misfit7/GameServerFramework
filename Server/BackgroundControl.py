#!/usr/bin/python3

import threading

# 后台管理
class Control(threading.Thread):
    def __init__(self, maintask):
        threading.Thread.__init__(self)
        self.maintask = maintask

    def run(self):
        while True:
            if input() == "show player":
                print(self.maintask.pMgr.keys())
                player = input("修改的玩家：")
                if player not in self.maintask.pMgr:
                    continue
                choice = input("1、等级 2、金币 3、余额：")
                number = int(input("修改的数值："))
                if choice == "1":
                    self.maintask.pMgr[player].lv = number
                elif choice == "2":
                    self.maintask.pMgr[player].coin = number
                elif choice == "3":
                    self.maintask.pMgr[player].money = number
                else:
                    pass
