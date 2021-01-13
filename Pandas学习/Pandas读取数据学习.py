
import pandas as pd
import numpy as np
import sys

#pandas的读取文件方法:read_table,read_csv,read_excel

'''表名确定的方法:
1,在pd.read_excel()里第二个参数可以直接输入表名
2,或者用sheet_name = 数字or列表,数字来说明第几个表or列表里的哪几张表(单表的返回对象为:''DataFrame'')
3,用sheet_name = None,用来代表所有的表(多表返回对象为:'collections.OrderedDict')
	3.1,OrderedDict,DataFrame为层级关系,可用for循环解OrderedDict来得到它里面的DataFrame的表名.
	3.2,用df[数字],来得到每个DataFrame的内容.
'''

df=pd.read_excel('E:/PythonStudy_Git/调用资料/pystudy2.xlsx',sheet_name = None)#读取excel表格
print(type(df))#DataFrame的属性:两个索引,一是行索引index,二是列索引columns
for i in df:
	print (i)


# # iterrows按照行读取数据,每次读一行,迭代为(insex, Series)对。
# # iteritems按照列读取数据,每次读一列迭代为(列名, Series)对
# # itertuples:按照行读取数据,迭代为元祖
a=[]
k=0
q=0
# for index,row in df.iteritems():#取pandas数据,按照每次取一列/行数据来取,index为列号,row为列/行内容
# 	q+=1
# 	for i in range(len(row)):
# 		a.append(row[i])
# 		k+=1
# print(q)#计数器q
# print(k)#计数器k,看循环次数
# print(a)	

def 写入excel多表(df):#pandas写入excel多张sheet表方法
	
	with pd.ExcelWriter(r'E:/PythonStudy_Git/调用资料/newforPF.xlsx') as xlsx:
		for i in df:
			df[i].to_excel(xlsx, sheet_name=f"{i}", index=False)

写入excel多表(df)

# b=np.array(a)#列表转换为array格式
# df = pd.DataFrame(a)#转换为dataframe格式
# df列名获取    :for column in df1.columns.values: 读取df的列名
# df.to_excel('E:/pyNote/调用资料/材料单.xlsx','Sheet1')
# df.to_csv时候乱码问题解决,df.to_excel('E:/pyNote/调用资料/材料单.xlsx',encoding="utf_8_sig")

#显示所有列
pd.set_option('display.max_columns', None)#pd数据显示所以列
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
#显示前10行
# df.head(10)