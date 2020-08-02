import  pymysql.cursors

#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#port 必须是数字不能为字符串
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
cursor = connection.cursor()

# 执行SQL语句创建新表
sql = "CREATE TABLE Persons3(Id_P varchar(255),内容 varchar(255))ENGINE=MyISAM DEFAULT CHARSET=utf8;"
cursor.execute(sql)

connection.close()