import pymysql
import PlayerMgr
import pickle

class GameSql():
    def login(self,conn):
        cursor = conn.cursor()  # 括号内不写参数,数据是元组套元组




        pMgr=PlayerMgr.PlayerMgr()
        p=pMgr.NewPlayer("李华旸",None)
        s1="insert into player(pname) values(%s)"
        s2="insert into playercontent(id, playercontent) values(%s, %s)"
        
        try:    
            cursor.execute(s1,p.uname)
            p.id=cursor.lastrowid
            ps=pickle.dumps(p)
            d_tuple=(p.id, ps)#pymysql.Binary(ps)
            cursor.execute(s2,d_tuple)
            conn.commit()
        except  Exception as ex:
            conn.rollback()
        
        sql1 = 'select * from playerContent;'  # SQL语句会被高亮显示
        # 执行SQL语句
        affect_rows = cursor.execute(sql1)
        print(affect_rows)  # 执行SQL语句之后受影响的行数
        # 获取数据
        # res = cursor.fetchall()  # 获取所有数据
        res = cursor.fetchone()  # 获取一条数据
        
        px=res[1] #获得player的二进制
        p=pickle.loads(px)
        print(p)
        # res = cursor.fetchmany(2)  # 获取指定个数数据
        # cursor.scroll(1, 'relative')  # 相对于当前位置往后移动一个单位
        # res = cursor.fetchall()  # 获取所有数据
        # cursor.scroll(1, 'absolute')  # 相对于起始位置往后移动一个单位
        res1 = cursor.fetchall()  # 获取所有数据
        print(res, res1)

        conn.close()