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

#查看返回数据fetch
# 如果select本身取的时候只有一条数据时：
# cursor.fetchone()：将只返回一条结果，返回单个元组如('id','title')。
# cursor.fetchall() :也将返回所有结果，返回二维元组，如(('id','title'),),
# cursor.fetchmany(3)获取前三行数据，元组包含元组

sql = f'select * from 材料库'
cursor.execute(sql)
# print("记录数量： " + str(cout))
#
# print(cursor.fetchmany(100))  #获取前三行数据，元组包含元组
print(cursor.fetchall())  #取下一行!!!
# print(cursor.fetchall())  #取剩下所有行!!
#
print('空了吗?')
for row in cursor.fetchall():
    print('剩余',row)#因为fetchall已经取完,所以现在的fetchall为空


def 返回sql的字段名():
	line=cursor.description#为二维元组

connection.close()