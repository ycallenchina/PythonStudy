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

def 内嵌销量表(CL_name0,CL_need):#含有递归算法
	
	CL_sheet=CL_name0
	cursor.execute(f"select 材料 from {CL_name0}")
	CL_list=cursor.fetchall()
	for CL_name in CL_list:
		if CL_name[0] in sheetname_All_GlobalX:
			CL_name0=CL_name[0]
			cursor.execute(f"select 用量 from {CL_sheet} where 材料='{CL_name[0]}'")
			sql_fig=cursor.fetchall()
			CL_need=float(sql_fig[0][0])*CL_sales_GlobalX#第二次材料表实际的总用量
			内嵌销量表(CL_name0,CL_need)
		else:
			cursor.execute(f"select 用量 from {CL_sheet} where 材料='{CL_name[0]}'")
			sql_fig1=cursor.fetchall()#配方数据

			cursor.execute(f"select 用量 from 材料库 where 材料='{CL_name[0]}'")
			sql_fig2=cursor.fetchall()#库数据
			
			#用获取的材料名对应的数值相减;算出本次库存剩余数据,并updata到材料库里
			updata_db=float(sql_fig2[0][0])//float(sql_fig1[0][0])
			CL_sheet_MinCount[CL_name[0]]=updata_db
			# CL_sheet_MinCount.append(updata_db)
			# CL_sheet_MinCount.append(CL_name[0])
			# cursor.execute(f"UPDATE 材料库 SET 用量 = '{updata_db}' WHERE 材料='{CL_name[0]}'")
			# print(f"UPDATE 材料库 SET 用量 = '{updata_db}' WHERE 材料='{CL_name[0]}'")

df=pd.read_excel('E:/PythonStudy_Git/调用资料/配方表.xlsx',sheet_name = None)#读取excel表格
sheetname_All_GlobalX=[i for i in df]#获取已有配方表名

df=pd.read_excel('E:/PythonStudy_Git/调用资料/销量表.xlsx',sheet_name = 0)#读取excel表格
for index,row in df.iterrows():#获取销量表的菜单名,及销量
	CL_sheet=row[0]
	CL_sales_GlobalX=float(row[1])
	cursor.execute(f"select 材料 from {CL_sheet}")
	CL_list=cursor.fetchall()
	CL_sheet_MinCount={}

	#执行sql获取表的材料名
	for CL_name in CL_list:#遍历sql表咖喱酱里的材料名
		if CL_name[0] in sheetname_All_GlobalX:
			CL_name0=CL_name[0]
			cursor.execute(f"select 用量 from {CL_sheet} where 材料='{CL_name[0]}'")
			sql_fig=cursor.fetchall()
			CL_need=float(sql_fig[0][0])*CL_sales_GlobalX#材料用量=单位用量*销量
			内嵌销量表(CL_name0,CL_need)
		else:
			cursor.execute(f"select 用量 from {CL_sheet} where 材料='{CL_name[0]}'")
			sql_fig1=cursor.fetchall()#配方数据

			cursor.execute(f"select 用量 from 材料库 where 材料='{CL_name[0]}'")
			sql_fig2=cursor.fetchall()#库数据
			
			#用获取的材料名对应的数值相减;算出本次库存剩余数据,并updata到材料库里
			updata_db=float(sql_fig2[0][0])//float(sql_fig1[0][0])
			CL_sheet_MinCount[CL_name[0]]=updata_db
			# CL_sheet_MinCount.append(updata_db)
			# CL_sheet_MinCount.append(CL_name[0])
			# cursor.execute(f"UPDATE 材料库 SET 用量 = '{updata_db}' WHERE 材料='{CL_name[0]}'")
			# print(f"UPDATE 材料库 SET 用量 = '{updata_db}' WHERE 材料='{CL_name[0]}'")
	print(f'{CL_sheet}    的最多可出:',min(CL_sheet_MinCount.values()))
	print({i:CL_sheet_MinCount[i] for i in CL_sheet_MinCount if CL_sheet_MinCount[i]==min(CL_sheet_MinCount.values())})
	# print(CL_sheet_MinCount)
connection.close()