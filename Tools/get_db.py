
def 获取指数(code_list,start,end,path):
	'''# 输入:指数名的列表,起始日期,末尾日期_格式:'20170101',输出的文件全路径
	   # 输出:生成excel文件,内容是一定日期的多指数的数据'''
	import  tushare as ts
	import pandas as pd
	#新接口,初始化,带自己账号14739570251
	pro = ts.pro_api('3d98b14b34ae4c172fb871d1dcfebd9edecec57bc5c695afb822921b')

	#初始化df,因为801004.SI是空数据,所以返回只有列头名的dataframe
	df = pro.index_daily(ts_code='801004.SI', start_date=start, end_date=end)

	#取股名列的数据转化为list,内容为str
	for code in code_list:
		df_new=pro.index_daily(ts_code=code, start_date=start, end_date=end)#获取指数数据
		df=pd.concat([df,df_new],axis=0,ignore_index=True)
		#合并2个df 数据,axis=1横向合拼,=0纵向合并,ignore_index=True自动编号
	df.to_excel(path,'Sheet1')


def 读取一列数据(path, y, sheet='Sheet1'):
	'''#输入:excel数据的路径,取数据的第几列y,默认sheet='Sheet1'
	   #输出:list格式 第y列的数据'''

	import pandas as pd
	df = pd.read_excel(path, sheet)  # 读取excel表格
	y_name = df.columns.values  # 获取df的列名
	df_list = df[y_name[y-1]].tolist()
	return df_list
