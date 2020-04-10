A={'a','b','c'}
B={'b','c','d'}
#差集,交集,并集
E=A-B
D=A&B
C=A|B
print(E,D,C)

#统计工具模块
import collections
F=collections.Counter(A)
print(F)

#串串模块,二维列表变一维的方法
import itertools
G=[('张三', 5), ('李四', 2), ('王五', 4), ('赵六', 2)]
# H=list(itertools.chain(*G))
print(*G)