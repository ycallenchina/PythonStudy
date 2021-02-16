from math import sin
from matplotlib import  pyplot
x=range(20)
y=range(10)
a=[i/10 for i in range(1,100)]
b=[sin(i) for i in a]

# 列表生成器-双循环
k=[i*j for i in x for j in y]
print(k)

# 列表生成器-判断语句
k=[i*j for i in x for j in y if i*j>70]
print(k)
# pyplot.plot(a,b)
#
# pyplot.show()