
# tushare 新接口 账号:14739570251 密码 a坤


import  tushare as ts
import pandas as pd
#新接口
pro = ts.pro_api('3d98b14b34ae4c172fb871d1dcfebd9edecec57bc5c695afb822921b')#新接口初始化,带自己账号14739570251

# df = pro.daily(trade_date='20180810')#获取当天所以股票信息

'''市场代码	说明
MSCI	MSCI指数_国际
CSI	中证指数
SSE	上交所指数
SZSE	深交所指数
CICC	中金指数_板块61种
SW	申万指数
OTH  其他指数'''
# df = pro.index_basic(market='SW')#获取市场里的指数
df = pro.index_daily(ts_code='801004.SI', start_date='20171001', end_date='20171031')#获取具体指数每日数据
df.to_excel('E:\pyNote\调用资料/64classNew.xlsx','Sheet1')#导出到excel

# df = pro.daily(ts_code='002466.SZ', start_date='20110101', end_date='20111231')#新接口,获取指定股票,日期的数据
# x=ts.get_hist_data('002466',start='2011-01-01',end='2011-12-31')#旧接口
print(df)


