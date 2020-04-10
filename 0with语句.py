

import  pymysql.cursors
import tushare as ts

# 加载mysql
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
# 填写股票名,和时间

#多用于open 文件语句
#作用等同于 cursor = connection.cursor()并在执行完以下语句后再执行cursor.close()
with connection.cursor() as cursor:
    sql = f"select * from file where 内容='eff'"
    returns=cursor.execute(sql)
    print(returns)
    print(cursor.fetchall())

    sql = f"select * from file where 内容='qaq'"
    returns=cursor.execute(sql)
    print(returns)
    print(cursor.fetchall())

#cursor是光标,好比载体,connection是连接路.关闭连接路更加稳健.
connection.close()