import pymysql
import PlayerMgr

import pickle
# 链接服务端
conn_obj = pymysql.connect(
    host='127.0.0.1',  # MySQL服务端的IP地址
    port=3306,  # MySQL默认PORT地址(端口号)
    user='root',  # 用户名
    password='Biewanwohao123.',  # 密码,也可以简写为passwd
    database='game',  # 库名称,也可以简写为db
    charset='utf8'  # 字符编码
)
# 产生获取命令的游标对象
cursor = conn_obj.cursor()  # 括号内不写参数,数据是元组套元组
# cursor = conn_obj.cursor(
#     cursor=pymysql.cursors.DictCursor
# )  # 括号内写参数,数据会处理成字典形式
# sql1 = 'show tables;'

pMgr=PlayerMgr.PlayerMgr()
p=pMgr.NewPlayer("张三", 1)
s1="insert into player(pname) values(%s)"
s2="insert into playercontent(id, playercontent) values(%s, %s)"

try:    
    cursor.execute(s1,p.uname)
    p.id=int(cursor.lastrowid)  #
    ps=pickle.dumps(p)
    cursor.execute(s2,(p.id,ps))  #
    conn_obj.commit()
except Exception as ex:
    conn_obj.rollback()

sql1 = 'select * from playerContent;'  # SQL语句会被高亮显示
# 执行SQL语句
affect_rows = cursor.execute(sql1)
print(affect_rows)  # 执行SQL语句之后受影响的行数
# 获取数据
# res = cursor.fetchall()  # 获取所有数据
res = cursor.fetchone()  # 获取一条数据
px=res[1]
p=pickle.loads(px)
print(p)
# res = cursor.fetchmany(2)  # 获取指定个数数据
# cursor.scroll(1, 'relative')  # 相对于当前位置往后移动一个单位
# res = cursor.fetchall()  # 获取所有数据
# cursor.scroll(1, 'absolute')  # 相对于起始位置往后移动一个单位
res1 = cursor.fetchall()  # 获取所有数据
print(res, res1)
cursor.close()
conn_obj.close()