import pandas as pd
import numpy as np
import sys
import  pymysql
import  pymysql.cursors
import chardet

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

def 建表SQL语句(df,表名):
    head=f'CREATE TABLE {表名}' #创建表名  
    col_name=''
    for col_i in df:#创建列名和其类型
        #字段类型设置
        if col_i=='序号':#序号列类型设置
            col_name+=col_i+' INT(11) NOT NULL,'
        elif any(j in col_i for j in ['元','退款','额']):#数字列类型设置
            col_name+=col_i+' DECIMAL(10,2) NOT NULL,'
        else :#其他文本列类型设置
            col_name+=col_i+' VARCHAR(255),'
    body=f"({col_name}PRIMARY KEY (`序号`) USING BTREE)"#设置字段主键
    tail=" ENGINE=MyISAM DEFAULT CHARSET=utf8;"#设置表的格式组成整句SQL
    
    sql=head+body+tail#头身尾
    return sql
#主
def csv创建sql(表名,sql_go=False):

	#读取csv,提取编译方式
	#自动获取编译方式
	# with open(表名,'rb') as file:
	#     s=file.read()
	#     d=chardet.detect(s)
	#     编译方式=d['encoding']
	
	d=表名.split("/")#用分裂法,获取文件名
	sql_name=d[-1][:-4]

	编译方式='utf_8_sig'
	df=pd.read_csv(表名,encoding=编译方式)#读取csv为df,index_col=0为取消index
	df=df.where(df.notnull(),'')#去dataframe里的空值nan,替换为''

	sql=建表SQL语句(df,sql_name)
	if sql_go :#sql_go为Ture时执行sql语句,不然只是print.
		cursor.execute(sql)#执行sql
	else:
		print(sql)

def csv内容写入sql(表名,sql_go=False):
	#读取csv,提取编译方式
	# with open(表名,'rb') as file:
	#     s=file.read()
	#     d=chardet.detect(s)
	#     编译方式=d['encoding']

	d=表名.split("/")#用分裂法,获取文件名
	sql_name=d[-1][:-4]
	print('开始写入sql表:',sql_name)

	编译方式='utf_8_sig'
	df=pd.read_csv(表名,encoding=编译方式)#读取csv为df,index_col=0为取消index
	df=df.where(df.notnull(),'')#去dataframe里的空值nan,替换为''

	#内容插入
	for index,row in df.iterrows():#读取行row,并插入内容
		sql2=f"INSERT INTO {sql_name} VALUES "+str(tuple(row))
		if sql_go :#sql_go为Ture时执行sql语句,不然只是print.
			cursor.execute(sql2)#执行sql
		else:
			print(sql2)

def 找遍所有文件里某类型文件的路径(path,x=4,s='.csv'):
    '''   输入:#找遍path文件夹里所有尾部最后x=3位为s='.py'的文件
          输出:list类型所有文件路径的列表'''

    import os
    所找文件路径 = []
    #在walk的第二层里,排除venv文件夹
    for 二层 in os.walk(path):
        if 'venv' in 二层[0]:#排除venv文件
            pass
        else:
            #在第二层的下一层第三个包里,找最后3个字符等于.py的.
            for 四层 in 二层[2]:
                if 四层[-(x):]==s :
                    所找文件路径.append((二层[0]+'/'+四层,四层))
    return 所找文件路径

def 批量导入sql(文件路径,sql_go=False):

	All_file=找遍所有文件里某类型文件的路径(文件路径)
	#遍历文件名
	for i in All_file:
		路径=i[0]
		csv内容写入sql(路径,sql_go)
if __name__ == '__main__':

	路径="C:/Users/YcAllenEffy/Desktop/已处理账表2次"
	批量导入sql(路径,1)

connection.close()

