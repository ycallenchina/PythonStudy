
import pandas as pd
import numpy as np


表名="D:/PythonStudy_Git/调用资料/导出测试2.xlsx"
#创建表
df=pd.read_excel(表名,sheet_name = 0)#读取excel表格
df2=df.applymap(lambda x:x.strip())
print(df2)
print(type(df2))