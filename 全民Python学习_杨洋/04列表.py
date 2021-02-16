 #列表资料网站 https://www.runoob.com/python3/python3-list.html

import random as ran
x=['eff','Allen','Xman','Q博士','98','55']
y=[1,2]
q=[1,2,4,3,5,6]
q.reverse()
#列表--函数
# q.reverse()更改原列表，倒序序排列
# q.sort()更改原列表，正序排列
print(q)
print('列表长度：',len(x),'\n取列表某个值：',x[3],'\n倒数取值：',x[-2],'\n最大值：',max(x),'\n最小值：',min(x))
# 列表--切片器
# 列表--切片器（左封闭，右开的规则，举例1：切片为取第二个，3，4，第五个不取）
# 切片器，也有步长使用方法举例：x[1:4：2]步长2取值
# 切片器，反向切片方法x[8:3:-2]反向取步长2值
print('切片范围[1:4]:',x[1:4],'\n切片范围[:2]:',x[:2],'\n切片范围[:-3]:',x[:-3])

# 列表的运算
print('列表的运算+',x+y,'\n列表的运算*',x*2)


# while 1==1:
#     i=ran.randint(0,len(x)-1)
#     print('x元素:',i)
#     # 字典不能被input函数使用，input里面必须是str
#     s=input(x[i]+' is whose name:')

# 列表对象的方法：append(增加元素),count(统计元素）
# index（元素出现第一次的位置）insert(插入位置，元素）
# pop（删除下表i元素）且返回删除的元素。，remove(删除第一个i元素）
# reverse （顺序倒序排），sort（默认从小到大排序）