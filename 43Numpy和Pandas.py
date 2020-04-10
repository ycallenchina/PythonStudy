import numpy as np

a=[[121.0, 55.0, 555.0], [232.0, 454.0, 232.0], [323.0, 455.0, 233.0] ,[323.0, 455.0, 233.0]]

b=np.array(a)#列表转换为nd array对象
b=b.reshape(2,6)#转换为2行,6列
c=b.tolist()#转回列表
print(c)
d=b.T#行列对换
print(d)

# a.append([1,[1,2]])
e=np.array(a)
e.ravel()#降维,从二维降到一维
print(e)

import pandas as pd
g=pd.read_excel('E:/pyNote/调用资料/43class.xlsx','Sheet1')#读取excel表格
print(g)

k=g.iloc[4:,3:]#提取[行,列]数据dataframe对象里面4行到最后,及3列到最后的内容
f=[121.0, 55.0, 555.0,232.0, 454.0, 232.0, 323.0, 455.0]
f=np.array(f)
f=f.reshape(4,2)
print(f)
print(k)
y=k+f#矩阵加法运算
print(y)
print(y.T)
y.T.to_excel('E:/pyNote/调用资料/43classNew.xlsx','Sheet1')#保存为excel,但是会覆盖整个excel表,建议新建.
