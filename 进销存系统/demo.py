
import pandas as pd
import numpy as np
import sys
import  pymysql
import  pymysql.cursors

#链接sql
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
cursor = connection.cursor()

def 读取表创建表写入内容(data='E:/PythonStudy_Git/调用资料/data_db.xlsx'):
	#读取excel内容,并用sheet名创建表名,第一行名创建keys,最后插入内容

	df=pd.read_excel(data,sheet_name = None)#读取excel表格
	#创建表
	for i in df:#读取表名i,并创建
		print (i)
		Csql_columns=''
		for c in df[i].columns:#读取列名,并创建
			Csql_columns+=c+' varchar(255),'
		sql = f"CREATE TABLE {i}({Csql_columns[:-1]})ENGINE=MyISAM DEFAULT CHARSET=utf8;"	
		print(sql)
		# cursor.execute(sql)#执行sql
		
		#内容插入
		for index,row in df[i].iterrows():#读取行row,并插入内容
			sql2=f"INSERT INTO {i} VALUES "+str(tuple(row))
			print(sql2)
			# cursor.execute(sql2)#执行sql

def 创建材料库(data='E:/PythonStudy_Git/调用资料/材料库2.xlsx'):

	df=pd.read_excel(data,sheet_name = None)#读取excel表格

	Csql_columns=''
	for i in df:#读取最后一个i表名
		pass
	for c in df[i].columns:#读取列名,并创建表材料库,和列名.
		Csql_columns+=c+' varchar(255),'
	sql = f"CREATE TABLE 材料库({Csql_columns[:-1]})ENGINE=MyISAM DEFAULT CHARSET=utf8;"	
	print(sql)
	cursor.execute(sql)

	noecho=[]#建立无重复的列表
	for i in df:
		for index,row in df[i].iterrows():#读取行row,并插入内容
			if row[0] in noecho:#如果材料名重复就pass,不重复就加入noecho列表
				pass
			else:
				noecho.append(row[0])
				sql2=f"INSERT INTO 材料库 VALUES "+str(tuple(row))
				print(sql2)
				cursor.execute(sql2)#执行sql

def 从sql提取数据创建excel():

	cursor.execute(f'select * from 材料库')
	df = pd.DataFrame(cursor.fetchall())
	print(df)
	# df.to_excel('E:/PythonStudy_Git/调用资料/材料库.xlsx','Sheet1')

def 批量删除sql表():
	data='E:/PythonStudy_Git/调用资料/data_db.xlsx'
	df=pd.read_excel(data,sheet_name = None)
	for i in df:#读取表名i,并执行sql语句
		cursor.execute(f"DROP TABLE {i}")

def 读取表创建表写入内容_extra(data='E:/PythonStudy_Git/调用资料/data_db.xlsx'):
	#读取excel内容,并用sheet名创建表名,第一行名创建keys,最后插入内容
	#补充extra:用量key里的内容只保留数字

	df=pd.read_excel(data,sheet_name = None)#读取excel表格
	#创建表
	for i in df:#读取表名i,并创建
		print (i)
		Csql_columns=''
		for c in df[i].columns:#读取列名,并创建
			Csql_columns+=c+' varchar(255),'
		sql = f"CREATE TABLE {i}({Csql_columns[:-1]})ENGINE=MyISAM DEFAULT CHARSET=utf8;"	
		print(sql)
		# cursor.execute(sql)#执行sql
		
		#优化用量key里的内容只保留数字
		#并写入sql
		for index,row in df[i].iterrows():#读取行row,并插入内容
			
			k=0
			for r in row[1]:#如果字段内容里包括数字,k累加1,没有的话就把k位之前的替换原来的值
				if r in ['1','2','3','4','5','6','7','8','9','0','.']:
					k+=1
				else:
					row[1]=row[1][:k]
					break
			sql2=f"INSERT INTO {i} VALUES "+str(tuple(row))
			print(sql2)		
			cursor.execute(sql2)#执行sql



connection.close()