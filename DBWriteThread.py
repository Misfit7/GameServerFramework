#!/usr/bin/python3

import datetime
import pickle
import threading
import time
import queue
import random
import TCPProto

class TCPRecvThread(threading.Thread):
    def __init__(self,maintask,spanTime=12000):
        threading.Thread.__init__(self)
        self.maintask=maintask
        self.spanTime=spanTime

    def run(self):
        s1="insert into player(pname) values(%s)"
        s2="insert into playercontent(id, playercontent) values(%s, %s)"

        while (True):
            conn=self.maintask.getConn()
            cursor = conn.cursor()
            for pItem in self.maintask.pMgr:
                p=pItem.value()
                ps=pickle.dumps(p)
                try:
                    cursor.execute(s1,p.uname)
                    p.id=int(cursor.lastrowid)  #
                    cursor.execute(s2,(p.id,ps))  #
                    conn.commit()
                except Exception as ex:
                    conn.rollback()

            time.sleep(self.spanTime)   #两分钟存一次