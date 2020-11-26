
import pandas as pd
import numpy as np
import sys
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
# def 读取菜名创建sql配方表并写入内容(data):
	#读取excel内容,并用sheet名创建表名,第一行名创建keys,最后插入内容

sql表名='andyou9月明细'
导出路径='E:/PythonStudy_Git/调用资料/导出测试.xlsx'

#导出df内容
cursor.execute(f"select * from {sql表名}")
df=pd.DataFrame(cursor.fetchall())
#导出df字段名
cursor.execute(f'SHOW COLUMNS FROM {sql表名}')#返回的是字段资料:((字段1,类型,作用)(字段2,类型,作用))
sql_column=cursor.fetchall()
keys=[i[0] for i in sql_column]
df.columns=tuple(keys)


# print(df)
df.to_excel(导出路径,'Sheet1',index=False)
connection.close()

