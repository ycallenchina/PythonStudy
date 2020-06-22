import pandas as pd
import numpy as np
import sys

#pandas的读取文件方法:read_table,read_csv,read_excel
df=pd.read_excel('E:/PythonStudy_Git/调用资料/pystudy.xlsx','Sheet1')#读取excel表格
# print(df)
a=[]
k=0
q=0
# iterrows按照行读取数据,每次读一行,迭代为(insex, Series)对。
# iteritems按照列读取数据,每次读一列迭代为(列名, Series)对
# itertuples:按照行读取数据,迭代为元祖
for index,row in df.iteritems():#取pandas数据,按照每次取一列/行数据来取,index为列号,row为列/行内容
	q+=1
	for i in range(len(row)):
		a.append(row[i])
		k+=1
print(q)#计数器q
print(k)#计数器k,看循环次数
print(len(a))	



# b=np.array(a)#列表转换为array格式
# df = pd.DataFrame(a)#转换为dataframe格式
# df.to_excel('E:/pyNote/调用资料/材料单.xlsx','Sheet1')