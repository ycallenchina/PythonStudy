

import  pymysql.cursors
import tushare as ts

# 加载mysql
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')

cursor = connection.cursor()

sql = "CREATE TABLE Persons3(Id_P int,内容 varchar(255),PRIMARY KEY (`Id_P`))ENGINE=InnoDB DEFAULT CHARSET=utf8;"

cursor.execute(sql)
connection.close()

