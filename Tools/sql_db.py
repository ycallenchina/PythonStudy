import  pymysql
import  pymysql.cursors

#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#port 必须是数字不能为字符串
#db是 数据库名
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
cursor = connection.cursor()

def unpack_SQLfig(n):#解包sql提取的多维数据(递归方法)
    for i in n:
        if isinstance(i, tuple):
            return unpack_SQLfig(i) #为了使递归里面的函数往回传递数据的方法,加return
        else:
            return i

def goto_1list(N):#扁平多维列表或元组为一维列表
    q=[]
    def goto_1list(N):
        for i in N:
            if isinstance(i, list) or isinstance(i, tuple):
                goto_1list(i)
            else:
                q.append(i)
    goto_1list(N)
    return q

def sql材料的用量(表名,材料名):
	cursor.execute(f"select 用量 from {表名} where 材料='{材料名}'")
	return float(unpack_SQLfig(cursor.fetchall()))

def sql表的总用量(表名):
	cursor.execute(f'select sum(用量) from {表名}')
	return float(unpack_SQLfig(cursor.fetchall()))
	
def sql表的材料list(表名):
	cursor.execute(f"select 材料 from {表名}")
	return goto_1list(cursor.fetchall())

