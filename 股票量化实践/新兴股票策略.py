
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
import time 

def 读csv为df(表名):
    import pandas as pd
    import numpy as np
    import chardet
    #先判断文件编译方式,获得编码的encoding
    with open(表名,'rb') as file:
        s=file.read()
        d=chardet.detect(s)
        编译方式=d['encoding']
    #读取excel表格  
    df=pd.read_csv(表名,encoding=编译方式,index_col=False)
    return df
#只做一只股票000778
class peple(object):
	def __init__(self):
		self.原始资金=100000
		self.资金=100000
		self.持股市值=0
		self.剩余资金=100000
		self.持有=0
		self.价格=[5,3,3]
		self.当前策略=self.decide0
		self.进场价=3.6
	"""docstring for tactics"""
	def buy_stock(self,price,time_now):#买
		self.持有=int(self.资金/price)#保留持股整数
		self.资金=self.资金-self.持有*price#买后剩余资金
		print('买入时间:',time_now[:4],time_now[4:8],time_now[8:12],)
		con='买入时间:'+str(time_now[:8])+' '+str(time_now[8:12])+'\n'
		print('买入价格:',price)
		con=con+'买入价格:'+str(price)+'\n'
		print('买入资金量:',self.持有*price)
		con=con+'买入资金量:'+str(self.持有*price)+'\n'
		print('剩余资金:', round(self.资金,2))
		con=con+'剩余资金量:'+str(round(self.资金,2))+'\n'
		con=con+'-----------------------------'+'\n'
		print('-----------------------------')
		return con

	def sell_stock(self,price,time_now):#卖

		self.资金=self.资金+self.持有*price#卖后剩余资金
		print('卖出时间:',time_now[:4],time_now[4:8],time_now[8:12],)
		print('卖出价格:',price)
		print('卖出资金量:',round(self.持有*price,2))
		print('剩余资金:',round(self.资金))
		print('-----------------------------')
	def over(self,price,ma,time_now):#结束策略
		print('策略结束,本次策略盈利:',round(self.资金-self.原始资金,2))
		self.当前策略=self.pass_go
		print('-----------------------------')

	def pass_go(self,price,ma,time_now):
		pass

	def decide0(self,price,ma,time_now):#决策0买入时
		best_price=self.进场价#best_price为十个交易日内的最高价
		if price>best_price :
			print(f'买入操作:因为当前价格{price}大于进场价{self.进场价}')
			buy_meg=f'买入操作:因为当前价格{price}大于进场价{self.进场价}'+'\n'
			buy_meg=buy_meg+self.buy_stock(price,time_now)
			self.当前策略=self.decide1
			return buy_meg	

	def decide1(self,price,ma,time_now):#决策1
		if price<3.5:
			self.sell_stock(price,time_now)
			self.当前策略=self.over
		elif price>3.8:
			ma5=ma
			if price<ma5:
				# print('-------------注意价格低于ma5均线.-----------------')#低于ma均线后提示.
				if 距ending时间(time_now)<301:#盘末5分钟时
					print(f'卖出操作:因为当前价格{price}大于3.8,且小于均线{ma},并发生在盘末时间',time_now[:4],time_now[4:8],time_now[8:12])
					self.sell_stock(price,time_now)
					self.当前策略=self.over
		elif price>6:
			self.sell_stock(price)
			self.当前策略=self.over
	
	def 执行策略(self,price,ma=5,time_now='20210201145600000'):
		策略_msg=self.当前策略(price,ma,time_now)
		return 策略_msg

def 距ending时间(s):#默认为0时差
	from datetime import datetime
	t=datetime.strptime(s,'%Y%m%d%H%M%S000')
	t_today=datetime(t.year,t.month,t.day,15)
	delta=t_today-t
	# print('距离ending时间:',delta.seconds,'秒')#距离盘末时间提示
	return delta.seconds

if __name__ == '__main__':
	#获取股票数据
	pd.set_option('display.max_columns', None)#显示所有df列
	路径='C:/Users/YcAllenEffy/Desktop/333.csv'
	df=读csv为df(路径)
	df['time']=df['time'].apply(str)#把时间列的数据int类变为str类
	# print(df)

	a=peple()
	for index,row in df.iterrows():
		# print('time:',row['time'],'close,',row['close'],'ma5:',row['ma5'])
		a.执行策略(row['close'],row['ma5'],row['time'])


	# print('本次策略回测时间为:2021/01/08至2021/03/03,回测标的为:sz.000778,共有1632条记录,执行操作2次.')


	# #简易模拟
	# 价格=[5,4.2,4.6,4.7,4.9,4.77,6.1,99]
	# for i in 价格:
	# 	print('--------------')


		