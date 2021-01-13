
import pandas as pd
import numpy as np
import chardet


表名='C:/Users/YcAllenEffy/Desktop/待处理账表/微信20年50期.csv'

#先判断文件编码方式
with open(表名,'rb') as file:
    s=file.read()
    d=chardet.detect(s)#chardet编码方式判断函数,参数为bytes对象,返回encoding字典.
    编码方式=d['encoding']
print('编码方式为:',编码方式)

#读取excel表格  
df=pd.read_csv(表名,encoding=编码方式)
#逐行读取dataframe
# for index,row in df.iterrows():
#     print(row)

for column in df.columns.values:
    print(f'{column}\t',type(df[column][0]))    
