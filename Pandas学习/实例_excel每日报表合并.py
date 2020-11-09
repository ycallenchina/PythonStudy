import pandas as pd
import numpy as np
import sys

#初始化df
df_init=pd.read_excel(f'E:/PythonStudy_Git/调用资料/file/菜品报表.xlsx',sheet_name = 0)

cai_index=(('1','2020-10-01'),('2','2020-10-02'))
for i in cai_index:
	#逐个打开表,并增加时间列
	df=pd.read_excel(f'E:/PythonStudy_Git/调用资料/file/菜品报表 ({i[0]}).xlsx',sheet_name = 0)
	#增加时间
	df['时间']=i[1]
	df_init=pd.merge(df_init,df,how="outer")

print(df_init)
# df_init.to_excel('E:/pyNote/调用资料/菜品报表1111.xlsx','Sheet1')
