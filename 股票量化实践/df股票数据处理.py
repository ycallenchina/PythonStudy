import pandas as pd
import numpy as np
from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.sans-serif']=['Microsoft YaHei']

def 时间格式处理(df):
	# 数据格式处理
	df['time']=df['time'].astype('str')
	df['时间']=pd.to_datetime(df['time'].str[:-5])
	# df['close']=df['close'].astype('float')

	df['change']=df['close']-df['open']
	df['pct_change']=df['change']/df['open']*100
	df['年']=df['时间'].dt.year
	# return df
	# df.info()

def 获取csv数据(保存路径='C:/Users/YcAllenEffy/Desktop/样本股1.csv'):

	# 保存路径='C:/Users/YcAllenEffy/Desktop/样本股票603508.csv'
	df=pd.read_csv(保存路径,encoding='utf_8_sig')
	return df

if __name__ == '__main__':
	# pass
	df=获取csv数据()	
	时间格式处理(df)
	print(df)

