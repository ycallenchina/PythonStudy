

def go_回测():
	import 获取股票数据
	import 均线计算
	import 新兴股票策略

	df=获取股票数据.获取个股df(标的="sz.000757",start='2021-02-06', end='2021-03-03')
	df=均线计算.增加ma列(df)
	print(df)
	df.info()

	a=新兴股票策略.peple()

	for index,row in df.iterrows():
		t=a.执行策略(row['close'],row['ma5'],row['time'])
		if not(t is None):
			pass
		# print(t)
