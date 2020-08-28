import  pymysql
import  pymysql.cursors
import time

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

from Tools.Execute_sql import *

#获取已有配方表
def unpack_SQLfig(n):#解包sql提取的多维数据(递归方法)
    for i in n:
        if isinstance(i, tuple):
            return unpack_SQLfig(i) #为了使递归里面的函数往回传递数据的方法,加return
        else:
            return i

def goto_1list(N):#扁平多维列表或元组为一维列表
    q=[]
    def goto_1list(N):
        for i in N:
            if isinstance(i, list) or isinstance(i, tuple):
                goto_1list(i)
            else:
                q.append(i)
    goto_1list(N)
    return q

def sql材料的用量(表名,材料名):
	cursor.execute(f"select 用量 from {表名} where 材料='{材料名}'")
	return float(unpack_SQLfig(cursor.fetchall()))

def sql表的总用量(表名):
	cursor.execute(f'select sum(用量) from {表名}')
	return float(unpack_SQLfig(cursor.fetchall()))
	
def sql表的材料list(表名):
	cursor.execute(f"select 材料 from {表名}")
	return goto_1list(cursor.fetchall())

def sql整表(表名):
  cursor.execute(f"select * from {表名}")
  return cursor.fetchall()

def sql表的字段(表名):
    cursor.execute(f'SHOW COLUMNS FROM {表名}')#返回的是字段资料:((字段1,类型,作用)(字段2,类型,作用))
    sql_column=cursor.fetchall()
    keys=[i[0] for i in sql_column]
    return  tuple(keys)

def 记录表(df,表名):
  db_time=str(df.columns[1])

  for index,row in df.iterrows():
    if row[1]!=0:
      sql=f"INSERT INTO {表名} VALUES "+str(tuple(row)+(db_time,))
      cursor.execute(sql)
      # print(sql)

def excel创建sql表(df_OrderedDict,表名):
    Csql_columns=''
    for c in df_OrderedDict[表名].columns:#读取列名,并创建
      Csql_columns+=c+' varchar(255),'
    print((f"CREATE TABLE {表名}({Csql_columns[:-1]})ENGINE=MyISAM DEFAULT CHARSET=utf8;" ))
      # cursor.execute(f"CREATE TABLE {表名}({Csql_columns[:-1]})ENGINE=MyISAM DEFAULT CHARSET=utf8;" )

def excel写入sql表(df_OrderedDict,表名):
    #内容插入
    content=[]
    for index,row in df_OrderedDict[表名].iterrows():#读取行row,并插入内容
      print(f"INSERT INTO {表名} VALUES "+str(tuple(row)))
      content.append(tuple(row))
      # cursor.execute(f"INSERT INTO {PF_name} VALUES "+str(tuple(row)))
    return tuple(content)


def sql材料库更新excel(创建名):
  import pandas as pd

  cursor.execute(f'select * from 材料库')
  df = pd.DataFrame(cursor.fetchall())
  for index,row in df.iterrows():
    row[1]=0  
  df.columns=('材料',localtime_GlobalX)
  # print(df)
  df.to_excel(f'E:/PythonStudy_Git/调用资料/{创建名}.xlsx','Sheet1',index=False)

def sql更新销售表excel(创建名):
  import pandas as pd

  PF_iterrows=[(i[:-3],0) for i in PF_all_GlobalX]
  df = pd.DataFrame(PF_iterrows)
  df.columns=('材料',localtime_GlobalX)
  df.to_excel(f'E:/PythonStudy_Git/调用资料/{创建名}.xlsx','Sheet1',index=False)

cursor.execute('show tables')#从sql获取所有表名
All=goto_1list(cursor.fetchall())
PF_all_GlobalX=[i for i in All if i[-3:]=='配方表']#在sql里找出所有配方表
localtime_GlobalX=time.strftime("%Y-%m-%d "+'00:00:00', time.localtime())#获取当前时间