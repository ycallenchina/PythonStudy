
def 笛卡尔积函数():
	from itertools import product
	for i in list(product((1,2),(3,4))):
		print(i)

def 日期格式化():
	import time
	# 格式化成2016-03-20 11:45:39形式
	print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )


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