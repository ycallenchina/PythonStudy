

def 使用3大法制():
	#1导入即可执行.
	#2何时导入何时执行.
	#3重复导入不再执行.
	pass

def 引用及命名规则():
	#import 的包名字不能以'数字'和'_'开头
	#import 的包名不能与python里的关键字同名
	pass

def 变量和方法的引用():
	#引用本目录下的包可直接import
		#impot A包后,A包的变量,引用 A.变量
		#impot A包后,A包的方法,引用 A.方法()
	import GuessMusic
	a=GuessMusic.guess
	print('我是GuessMusic包:a=',a)
	print()
	#引用非本目录下的包
		#import sys
		#sys.path.append("..")#为了import引用上一级包
		#sys.path.append("绝对路径")#为了import此路径下的包
	import sys
	sys.path.append("D:/PythonStudy_Git/Pandas学习")
	import pandas实验室
	print('我是pandas实验室包:\n',pandas实验室.df1)

	#引用机制:
	'''引用X包的方法时,如果此方法里面还有引用别的方法则不需要理会.
	   因为此时的运行机制是,用谁的方法或变量都会自动加上包名前缀,如:X.方法(),X.属性'''

# 变量和方法的引用()