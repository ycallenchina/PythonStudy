
# tushare 新接口 账号:14739570251 密码 a坤


import  tushare as ts
import pandas as pd

#数据导入excel
pro = ts.pro_api('3d98b14b34ae4c172fb871d1dcfebd9edecec57bc5c695afb822921b')#新接口初始化,带自己账号
df = pro.daily(trade_date='20180816')#按天的历史记录 导入
# df = pro.daily(ts_code='002466.SZ', start_date='20110101', end_date='20111231')#新接口,获取指定股票,日期的数据
# # x=ts.get_hist_data('002466',start='2011-01-01',end='2011-12-31')#旧接口
# df.to_excel('E:\pyNote\调用资料/55classNew.xlsx','Sheet1')

print(df)

# # 读取
# def 读取数据():

#     df=pd.read_excel('E:\pyNote\调用资料/61classNew.xlsx','Sheet3')#读取excel表格
