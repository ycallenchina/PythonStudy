

#一  引用 tuar api  获取新兴 股票的数据 不用自动 ,每次打开程序 记录一次.用csv记录.记录时间为本月2021.3.1日起,按照每分钟记录价格.

#二  引用 qt界面 显示 设置初始资金,持股市值,市值,收益. 操作记录 收益图

#三  量化策略逻辑

# 一

def 保存csv文件(保存路径,df):
    df.to_csv(保存路径,encoding='utf_8_sig',index=False)
# tushare 新接口 账号:14739570251 密码 a坤
def 实时行情():
	import easyquotation

	quotation = easyquotation.use('tencent') # 新浪 ['sina'] 腾讯 ['tencent', 'qq']
	tmp_dict = quotation.market_snapshot(prefix=True) # prefix 参数指定返回的行情字典中的股票代码 key 是否带 sz/sh 前缀
	print(tmp_dict['sz000001'])#查看实时股价

import  tushare as ts
import pandas as pd
pd.set_option('display.max_columns', None)#显示所有df列
#新接口
ts.set_token('3d98b14b34ae4c172fb871d1dcfebd9edecec57bc5c695afb822921b')#ts接口初始化
pro = ts.pro_api('3d98b14b34ae4c172fb871d1dcfebd9edecec57bc5c695afb822921b')#ts.pro接口初始化,带自己账号14739570251
# df = pro.daily(ts_code='000778.SZ', start_date='20210101', end_date='20210110')
# df = pro.query('trade_cal', exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')


df = ts.pro_bar(ts_code='000778.SZ', start_date='20210301', end_date='20210311', freq='5min')
print(df)
print(df)
