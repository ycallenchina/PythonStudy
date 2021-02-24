
def 时间格式化():
	import time
	 
	# 格式化成2016-03-20 11:45:39形式
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

def 重组所有容器函数():
	from itertools import product
	for i in list(product((1,2),(3,4))):
		print(i)


def 日期格式化():
	import time
	 
	# 格式化成2016-03-20 11:45:39形式
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )