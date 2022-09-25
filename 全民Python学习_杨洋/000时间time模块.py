def time_limi(time1,limi1):
	import time
	#time 有三种格式 
	#1.struct_time对象格式,方便看时间
	#2.字符串格式
	#3.时间戳格式,方便时间运算


	# struct_time 格式化成 2016-03-20 11:45:39 字符串形式
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

	# 字符串转换为 struct_time
	print(type(time.strptime('2016-03-20 11:45:39','%Y-%m-%d %H:%M:%S')))


	# 字符串生成时间戳,方便时间运算
	c=time.mktime(time.strptime(time1,'%Y-%m-%d %H:%M:%S'))
	
	# 时间时间限制运算 大于限制则返回真
	# time.time 本身就是时间戳格式
	if (time.time()-c)//60 >limi1:
		return True
	else:
		return False



c='2022-09-25 18:07:07'
print(time_limi(c,30))