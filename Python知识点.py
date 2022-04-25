
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

def 进度条():
	
	from time import sleep
	from tqdm import tqdm

	for i in tqdm(range(1,100)):
		sleep(0.1)
	sleep(0.5)

def 路径学习():
	import os

	print(__file__)#当前目录
	print(os.path.abspath(__file__))#当前目录 绝对路径
	print(os.path.dirname(os.path.abspath(__file__)))#当前目录的上级目录
	print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#当前目录的上级 的上级目录

def 字符串前面u_r_b含义():
	'''1、字符串前加 u
	例：u"我是含有中文字符组成的字符串。"

	作用：

	后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。

	 

	2、字符串前加 r
	例：r"\n\n\n\n”　　# 表示一个普通生字符串 \n\n\n\n，而不表示换行了。

	作用：

	去掉反斜杠的转义机制。

	（特殊字符：即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n”表示换行，”\t”表示Tab等。 ）

	应用：

	常用于正则表达式，对应着re模块。

	 

	3、字符串前加 b
	例: response = b'<h1>Hello World!</h1>'     # b' ' 表示这是一个 bytes 对象

	作用：

	b" "前缀表示：后面字符串是bytes 类型。

	用处：

	网络编程中，服务器和浏览器只认bytes 类型数据。

	如：send 函数的参数和 recv 函数的返回值都是 bytes 类型

	附：

	在 Python3 中，bytes 和 str 的互相转换方式是
	str.encode('utf-8')
	bytes.decode('utf-8')
	'''