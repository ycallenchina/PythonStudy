import pandas as pd
import numpy as np
import sys
import chardet

with open ('E:/PythonStudy_Git/调用资料/1234.txt',encoding='utf-8') as f:
	s=f.readlines()#逐行读1234txt文件里数据

a=[]

#把有空格的数据分开,并去掉空格
for i in s:#遍历每行数据
	q=0#字符切分计数
	for k in i:#分析数据字符
		if k==' ':#字符里有空格就一分为二append进a列表
			a.append(i[:q])
			a.append(i[q:].strip())#去字符两头空格
			break
		q+=1
b=np.array(a)#列表转换为numpy.array格式,做维度变化
# result = b.reshape((66,2 ))
print(a)

# df=pd.DataFrame(result)#转换为pandas.dataframe数据准备导出excle
# print(df)
# df.to_excel('E:/pyNote/调用资料/材料单.xlsx','Sheet2')
