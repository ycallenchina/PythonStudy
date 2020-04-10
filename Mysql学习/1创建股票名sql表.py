
import  pymysql.cursors
#载入mysql数据库
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
cursor = connection.cursor()
# 表名=code股票名
symbol='000987'
code_symbol='code'+symbol
sql =f"CREATE TABLE {code_symbol}(Date varchar(255),close varchar(255),p_change varchar(255),volume varchar(255),PRIMARY KEY (`Date`)) DEFAULT CHARSET=utf8;"

# 执行sql语句
cout=cursor.execute(sql)

connection.close()