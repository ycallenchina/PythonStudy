
import sys
#分行写法,有括号的,可以自动分行
print(f' {sys._getframe().f_lineno}  行结果:',
	1)

#反斜线,可做分行
a=2**2+\
6
print(f' {sys._getframe().f_lineno}  行结果:',a)

#;号可以连接多行
b=2;c=b+20
print(f' {sys._getframe().f_lineno}  行结果:',c)



import math
math.sin(3)
math.cos(1)
math.log(1)
print(f'  {sys._getframe().f_lineno}  行结果:',math.gcd(9,6))#求公约数
print(f' {sys._getframe().f_lineno}  行结果:',math.factorial(4))#阶乘计算

#知识点:内置模块   像print这种函数不需导入,因为他是python解释器的内置模块 __builtins__
#知识点:标准库  例如re,math,os,sys等 资料网站:docs.python.org
import winsound
winsound.Beep(1000,500)#发生模块Beep(频率,时长单位毫秒)
