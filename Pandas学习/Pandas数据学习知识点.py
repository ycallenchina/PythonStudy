
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

boolean=[True,False]
gender=["男","女"]
color=["white","black","yellow"]
df=pd.DataFrame({
    "height":np.random.randint(150,190,10),
    "weight":np.random.randint(40,90,10),
    "smoker":[boolean[x] for x in np.random.randint(0,2,10)],
    "gender":[gender[x] for x in np.random.randint(0,2,10)],
    "age":np.random.randint(15,90,10),
    "color":[color[x] for x in np.random.randint(0,len(color),10) ]
    }
)
 
print(type(df))#DataFrame的属性:两个索引,一是行索引index,二是列索引columns
for i in df:
	print (i)

def 获取df数据信息():
	df.info()
	pass
def 判断df里的数据类型():
	df=df.applymap(type)
	
def 读取每行(df):
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
def 删除列():
	df=df.dorp(['列名1','列名2'],axis=1)#axis参数有两个值:0表示按照行操作,1表示按照列操作

def 读取csv文件(路径):
	#encoding为编译方式
	df=pd.read_csv(路径,encoding='utf_8_sig',index_col=False)
def 设置index值(路径):
	#index_col=False——重新设置一列成为index值
	#index_col=0——第一列为index值,同理index_col=1得话第二列为index值
	#df.index=['1','2','3']来设置具体index值	
	df=pd.read_csv(路径,encoding='utf_8_sig',index_col=False)
	df.index=['1','2','3']
def 保存csv文件(保存路径,df):
	df.to_csv(保存路径,encoding='utf_8_sig',index=False)#不要索引

def 写入excel多表(df):#pandas写入excel多张sheet表方法
	
	with pd.ExcelWriter(r'E:/PythonStudy_Git/调用资料/newforPF.xlsx') as xlsx:
		for i in df:
			df[i].to_excel(xlsx, sheet_name=f"{i}", index=False)
def 分组():
	df=df.groupby('分组列')#按照分组列 分组
	df=df.agg('mean')#取分组里数据的平均值
	pass

def 改df列名(df):
	df.rename(columns={df.columns.values[0]:'序号'},inplace=True)#0为第一列
	df.rename(columns={'A':'a', 'C':'c'}, inplace = True)#把A改为a,C为c
	df.rename(columns={'被改列名':'改后列名'})#单列名修改

def 列与列数据交互():
	df['值1列+值2列']=df['值1列']+df['值2列']
	pass

def df提取列(df):
	df=df[['序号','交易日期','记账金额','收_支''备注']]

def 筛选(df):
	df[df['gender']=='男']#筛选gender列为男的数据


def 打印显示设置(df):
	pd.set_option('display.max_columns', None)#pd数据显示所以列
	#显示所有行
	pd.set_option('display.max_rows', None)
	#设置value的显示长度为100，默认为50
	pd.set_option('max_colwidth',100)
	#显示前10行
	df.head(10)

def 获取列名方法(df):
	print(df.columns.values)
	print(list(df))
	print(df.column.tolist())
	print(df.columns)

def df时间属性(df):
	df['time'] = pd.to_datetime(df['time'])#转换列为datetime格式
	data['year']=data['time'].dt.year#增加年列
	data['day']=data['time'].dt.day#增加日列
	data['hour']=data['time'].dt.hour#增加小时列
	data['minute']=data['time'].dt.minute#增加分钟列
	
	df=df[df['time']>'2021-2-10']#筛选时间大于2-10号的,包括2-10
	df=df[df['time']<'2021-2-13']#筛选时间小于2-13号的,不包括2-13
	df[df['time'].dt.month==2]#筛选月份为2月的记录
	pass

def 添加行记录(df):

	record={'height':'199'}
	df=df.append(record,ignore_index=True)
	return df

def 创建新df():
	df = pd.DataFrame(columns=['A', 'B', 'C', 'D'])
	return df

def 某列包含未知内容(df,列名='date',包含内容='未知',新列='新列1'):
	# 返回所有包含内容的记录
	df[新列]=df[df[列名].str.contains(包含内容)]
	return df

def df取值(df):
	#当df为二维数组时,iloc里有两个参数,并可以做冒号:切片处理
	行头,行尾,列头,列为=0,0,0,0
	df.iloc[行头:行尾,列头:列尾]
	# 当df为一维数组时,iloc里面只有一个参数,也可以做切片处理
	df.iloc[行头:行尾]

def 根据条件写入数据(df):
	# 条件为在'time'列包含'150000000'的记录里写入1,否则写入0,并创建'新列'记录.
	df['新列']=np.where(df['time'].str.contains("150000000"),1,0)

def 创建or修改某个列里的数据(df):
	索引=0#一般0为第一个数据
	df.iloc[index,'列名']='所修改的值'
	
def 空值nan处理(df):
	df=df[df['列名'].notnull()]#取为不空值nan的记录
	df=df[df['列名'].notnull()]#取为空值nan的记录

def 设置索引(df):
	#方法一 把列直接放入索引列
	df=df.set_index('df的列名')
	#方法二 把列复制放入索引列
	df.index=df['df的列名']
	pass

def 添加索引(df):
	df.set_index('month',append=True)
	pass
# b=np.array(a)#列表转换为array格式
# df = pd.DataFrame(a)#转换为dataframe格式
# df列名获取    :for column in df1.columns.values: 读取df的列名
# df.to_excel('E:/pyNote/调用资料/材料单.xlsx','Sheet1')
# df.to_csv时候乱码问题解决,df.to_excel('E:/pyNote/调用资料/材料单.xlsx',encoding="utf_8_sig")