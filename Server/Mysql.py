import PlayerMgr
import pickle


class GameSql():
    def login(self, conn, data):
        cursor = conn.cursor()  # 括号内不写参数,数据是元组套元组

        username = data["data"]["username"]
        password = data["data"]["password"]

        s1 = "select * from player where pname=%s and ppassword=%s"
        s2 = "select * from playercontent where id=%s"
        s3 = "update player set logtime=SYSDATE() where id=%s"

        try:
            p_tuple = (username, password)
            cursor.execute(s1, p_tuple)
            row1 = cursor.fetchone()
            if (row1 != None):
                cursor.execute(s2, row1[0])
                row2 = cursor.fetchone()
                cursor.execute(s3, row1[0])
                conn.commit()
                return pickle.loads(row2[1])
            else:
                return 0
        except  Exception as ex:
            print(ex)
            return 0

    def register(self, conn, data):
        cursor = conn.cursor()  # 括号内不写参数,数据是元组套元组

        pMgr = PlayerMgr.PlayerMgr()
        username = data["data"]["username"]
        password = data["data"]["password"]
        usertype = data["data"]["usertype"]
        p = pMgr.NewPlayer(username, usertype)
        s1 = "insert into player(pname,ppassword,logtime) values(%s, %s, null)"
        s2 = "insert into playercontent(id, playercontent) values(%s, %s)"

        try:
            p_tuple = (p.uname, password)
            cursor.execute(s1, p_tuple)
            p.id = cursor.lastrowid
            ps = pickle.dumps(p)
            p_tuple = (p.id, ps)
            cursor.execute(s2, p_tuple)
            conn.commit()
            return 1
        except  Exception as ex:
            print(ex)
            conn.rollback()
            return 0
