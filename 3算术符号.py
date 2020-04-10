#算术符号优先级:乘方>正负号>乘除>加减
#运算符号,都是半角.
#注意除法
import sys#sys._getframe().f_lineno,返回自身代码所在的行数

print(f'  {sys._getframe().f_lineno}  行结果:整除运算',8//3)#整除,就是舍去小数的意思
print(f'  {sys._getframe().f_lineno}  行结果:负数的整除运算',-7//2)#注意负数的整除,取最小值
print(f'  {sys._getframe().f_lineno}  行结果:模运算求余',7%2)#求余,模运算
