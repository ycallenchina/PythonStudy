import pandas as pd
import numpy as np


def 时机(df,ch=1,ch_year='2017',ch_month='1'):


	if ch==1: 
		filter_time='2017-01'
		df['序号']=df.index
		df.index=df['时间']
		df=df.loc[filter_time].sort_values('pct_change',ascending=False).head(5)

		df.index=df['序号']
		df.index.name='序号索引'
		
		df=df.sort_values('时间')

	if ch==2:	
		# 过筛1  交易额大于2千万
		df_ch1=df[df['amount']>20000000]
		df_ch1=df_ch1.sort_values('时间',ascending=True)

		# 过筛2 交易额大于2千万 且 涨幅度大于4%
		df_ch2=df_ch1[df_ch1['pct_change']>4]
		df=df_ch2

	return df
if __name__ == '__main__':
	import df股票数据处理 as 处理
	df=处理.获取csv数据()	
	处理.时间格式处理(df)
	df=时机(df)
	print(df)
