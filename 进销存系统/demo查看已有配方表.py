
import pandas as pd
# import numpy as np
import sys
sys.path.append("..")#为了import引用上一级包
from Tools.sql_db import *

cursor.execute('show tables')
All=goto_1list(cursor.fetchall())
All_PF=[i for i in All if i[-3:]=='配方表']#在sql里找出所有配方表

with pd.ExcelWriter(r'E:/PythonStudy_Git/调用资料/newforPF.xlsx') as xlsx:
	for PF_sheet in All_PF:
		df=pd.DataFrame(sql整表(PF_sheet))#从sql获取整张表转换为DataFrame
		df.columns=sql表的字段(PF_sheet)#从sql获取表的列名
		df.to_excel(xlsx, sheet_name=f"{PF_sheet}", index=False)
		print(df)

connection.close()