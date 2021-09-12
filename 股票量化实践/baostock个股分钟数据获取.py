import baostock as bs
import pandas as pd
import numpy as np

# pd.set_option('display.max_rows', 20)
#官网
#http://baostock.com/baostock/index.php/%E9%A6%96%E9%A1%B5

def 保存csv文件(保存路径,df):
    df.to_csv(保存路径,encoding='utf_8_sig',index=False)
def 获取个股df(标的="sh.603508",start='2017-01-01', end='2017-02-20'):
	#### 登陆系统 ####
	lg = bs.login()
	# 显示登陆返回信息
	print('login respond error_code:'+lg.error_code)
	print('login respond  error_msg:'+lg.error_msg)



	# 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
	# frequency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，
	# frequency：不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线每月最后一个交易日才可以获取。
	# adjustflag：复权类型，默认不复权：3；1：后复权；2：前复权。
	rs = bs.query_history_k_data_plus(标的,
	    "date,code,time,open,close,volume,amount,high,low",
	    start_date=start, end_date=end,
	    frequency="15", adjustflag="3")
	

	print('query_history_k_data_plus respond error_code:'+rs.error_code)
	print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

	#### 打印结果集 ####
	data_list = []
	while (rs.error_code == '0') & rs.next():
	    # 获取一条记录，将记录合并在一起
	    data_list.append(rs.get_row_data())
	df = pd.DataFrame(data_list, columns=rs.fields)
	# print(df)

	bs.logout()
	return df
	#### 登出系统 ####

# 读取csv 股票数据
def 获取csv数据():

	保存路径='C:/Users/YcAllenEffy/Desktop/样本股票603508.csv'
	df=pd.read_csv(保存路径)
	return df

if __name__ == '__main__':
	# pass
	df=获取个股df()	
	print(df)
	保存路径='C:/Users/YcAllenEffy/Desktop/样本股1.csv'
	保存csv文件(保存路径,df)
	