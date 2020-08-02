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

	if x==1:#删除表
		cursor.execute("DROP TABLE 材料库")
	if x==2:#清空表
		cursor.execute("TRUNCATE TABLE file2")
	if x==3:#删除数据库
		cursor.execute("DROP DATABASE 数据库名称")
	if x==4:#删除内容行
		cursor.execute("delete from persons6 where 内容='qaq'")
	if x==5:#删除多行内容
		cursor.execute("delete from code600118 where Date in('7000')")
	if x==6:#更新内容
		cursor.execute("UPDATE code600118 SET volume = '88888' WHERE Date = '2019-11-15'")
		#UPDATE 表名 SET 字段名 = 'Fred' WHERE 字段名(所在行) = 'Wilson'(的那一行) 
	return 

执行sql(6)

connection.close()

