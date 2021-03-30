
def 笛卡尔积函数():
	from itertools import product
	for i in list(product((1,2),(3,4))):
		print(i)

def 日期模块time学习():
	import time

	'''1,时间的类型:字符串(str),struct_time类,时间戳(浮点数)
	   2,只有时间戳可以做时间差减法运算,结果为秒单位的float
	   3,struct_time可以提取时间里的年月日,时分秒(tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec)
	 '''

	format = '%Y-%m-%d %H:%M:%S'#格式化的格式设置
	t1="2019-03-09 08:52:51"
	t2="2019-03-11 08:53:51"

	t1_struck=time.strptime(t1,format)#字符串转为struct_time类
	t2_struck=time.strptime(t2,format)

	t1_stamp=time.mktime(t1_struck)#struct_time类转为时间戳
	t2_stamp=time.mktime(t2_struck)

	#转换
	switch_t1_struck=time.localtime(t1_stamp)#时间戳转换为struct_time
	switch_t1_str=time.strftime(format,switch_t1_struck)#struct_time转换为字符串
	print(switch_t1_str)


def 分隔_行_字符串(string):
	Li=string.splitlines()
	return Li 

def 命令行安装包():

	# pip install 安装包名
	# pip show --f iles 安装 包名(展示) 
	# pip install --upgrade 要升级的包名
	# pip uninstall 要卸载的包名
	# pip --help

	pass

