#!/usr/bin/python3

import pickle
import threading
import time,datetime

# 自动保存
class TCPSaveThread(threading.Thread):
    def __init__(self,maintask,spanTime=12000):
        threading.Thread.__init__(self)        
        self.maintask=maintask
        self.spanTime=spanTime
    
    def run(self):
        #dtOld=dtNow=datetime.datetime.now()
        s1="insert into player(pname) values(%s)"
        s2="insert into playercontent(id, playercontent) values(%s, %s)"

        while True:
            conn= self.maintask.getConn()
            cursor = conn.cursor()
            for pItem in self.maintask.pMgr:
                p=pItem.value()
                ps=pickle.dumps(p)
                try:    
                    cursor.execute(s1,p.uname)
                    p.id=cursor.lastrowid
                    d_tuple=(p.id, ps)#pymysql.Binary(ps)
                    cursor.execute(s2,d_tuple)
                    conn.commit()
                except  Exception as ex:
                    conn.rollback()  

            time.sleep(self.spanTime) #2分钟存一次