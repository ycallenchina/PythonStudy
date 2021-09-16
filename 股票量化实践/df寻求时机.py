import pandas as pd
import numpy as np


def 时机(df,ch=1,filter_time='2017'):

	df_ch=df.copy()
	#寻找某段时间内的数据--时机1
	#且5分钟内涨幅最高的5条数据--时机2
	if ch==1: 
		df_ch['序号']=df_ch.index
		df_ch.index=df_ch['时间']

		df_ch=df_ch.loc[filter_time].sort_values('pct_change',ascending=False).head(8)

		df_ch.index=df_ch['序号']
		df_ch.index.name='序号索引'
		
		df_ch=df_ch.sort_values('时间')

	
	#过筛	
	if ch==2:	
		# 过筛1  交易额大于2千万
		df_ch1=df_ch[df_ch['amount']>20000000]
		df_ch1=df_ch1.sort_values('时间',ascending=True)

		# 过筛2 交易额大于2千万 且 涨幅度大于4%
		df_ch2=df_ch1[df_ch1['pct_change']>4]
		df_ch=df_ch2

	return df_ch
if __name__ == '__main__':
	import df股票数据处理 as 处理
	df=处理.获取csv数据()	
	处理.时间格式处理(df)
	df=时机(df)
	print(df)
