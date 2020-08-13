

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


df=pd.read_excel('E:/PythonStudy_Git/调用资料/进货表.xlsx',sheet_name = 0)#读取excel表格
for index,row in df.iterrows():#获取进货表
	CL_name=row[0]
	CL_purchase=float(row[1])

	cursor.execute(f"select 用量 from 材料库 where 材料='{CL_name}'")#库数据
	sql_fig2=cursor.fetchall()
	stock=float(sql_fig2[0][0])

	# #用获取的材料名对应的数值相加;算出本次库存剩余数据,并updata到材料库里
	updata_db=stock+CL_purchase
	updata_db=round(updata_db,2)#保留2位小数
	cursor.execute(f"UPDATE 材料库 SET 用量 = '{updata_db}' WHERE 材料='{CL_name}'")
	# print(f"UPDATE 材料库 SET 用量 = '{updata_db}' WHERE 材料='{CL_name}'")

connection.close()
