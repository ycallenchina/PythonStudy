
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

表名="E:/PythonStudy_Git/调用资料/csi汇总.xlsx"
#创建表
df=pd.read_excel(表名,sheet_name = None)#读取excel表格


for i in df:#读取表名i,并创建
	df[i]=df[i].where(df[i].notnull(),'')#去dataframe里的空值nan,替换为''
	
	PF_name=i
	Csql_columns=''
	for c in df[i].columns:#读取列名,并创建
		Csql_columns+=c+' varchar(255),'
	sql = f"CREATE TABLE {PF_name}({Csql_columns[:-1]})ENGINE=MyISAM DEFAULT CHARSET=utf8;"	
	print(sql)
	cursor.execute(sql)#执行sql
	
	#内容插入
	for index,row in df[i].iterrows():#读取行row,并插入内容
		sql2=f"INSERT INTO {PF_name} VALUES "+str(tuple(row))
		print(sql2)
		cursor.execute(sql2)#执行sql

connection.close()

