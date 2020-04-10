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
# 插入语句:INTO 表名 VALUES (内容)
cursor.execute("INSERT INTO file VALUES ('6', 'qaq', 'pp', 'Be4ij4ing')")

connection.close()