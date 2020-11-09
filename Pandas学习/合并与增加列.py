import pandas as pd
import numpy as np
import sys

#读取excel里的数据
df=pd.read_excel('E:/PythonStudy_Git/调用资料/file/菜品报表 (1).xlsx',sheet_name = 0)
#增加时间
df['时间']='2020-10-02'

df2=pd.read_excel('E:/PythonStudy_Git/调用资料/file/菜品报表 (2).xlsx',sheet_name = 0)
print(df2)

'''合并两表,how：连接方式:
有inner(根据条件,如同等id号的合并成一条记录
left左合并
right右合并
outer下合并
默认为inner；'''
df3=pd.merge(df,df2,how="outer")
print(df3)
