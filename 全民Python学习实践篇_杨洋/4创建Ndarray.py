

import numpy as np

def Numpy的核心_笔记():
	# ndarray 
	# 其中n表示 第几维度
	# d表示 dimensional 维度
	# array 表示数组
	pass

def 创建Ndarray():
	x=[1,2,3,'abc','qqq']

	'''向上兼容法制:在容器转换为ndarray时,
		如果遇到容器内容里类型不统一的情况下
		ndarray会强制统一容器里的内容.
		并使用向上兼容法制:整数-浮点数-字符串.
		法则为:有字符串就全都字符串,没有就全浮点,再没有就整数.
'''
	nd_x=np.array(x)
	print(type(nd_x))
	for i in nd_x:
		print(type(i),i)
	
	pass
def 创建多维数组():
	pass
def 创建随机数组():
	pass
def 导入csv文件创建Ndarray():
	pass

if __name__ == '__main__':
	创建Ndarray()