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

def 执行sql(x=0):

	if x==1:# 插入语句,内容需要匹配字段数:
		cursor.execute("INSERT INTO persons6 VALUES ('7000', 'qaq')")
	if x==2:# 在指定字段插入内容:
		cursor.execute("INSERT INTO code600118 (Date, close) VALUES ('Wilson', 'Champs-Elysees')")

执行sql(0)
connection.close()