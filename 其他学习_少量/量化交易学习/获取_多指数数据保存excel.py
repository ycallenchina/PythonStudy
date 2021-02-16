#输入:起始日期,末尾日期.格式:'20170101'
import  tushare as ts
import pandas as pd
#新接口,初始化,带自己账号14739570251
pro = ts.pro_api('3d98b14b34ae4c172fb871d1dcfebd9edecec57bc5c695afb822921b')

# df = pro.daily(trade_date='20180810')#获取当天所以股票信息
#初始化df,因为801004.SI是空数据,所以返回只有列头名的dataframe
df = pro.index_daily(ts_code='801004.SI', start_date='20171001', end_date='20171002')
# df.to_excel('E:\pyNote\调用资料/61classNew.xlsx','Sheet1')#导出到excel

# df = pro.daily(ts_code='002466.SZ', start_date='20110101', end_date='20111231')#新接口,获取指定股票,日期的数据
# x=ts.get_hist_data('002466',start='2011-01-01',end='2011-12-31')#旧接口

#读取excel表 获取股票名
df_code=pd.read_excel(r'E:\pyNote\调用资料/61classNew.xlsx','Sheet3')
code_list=df_code.股名.tolist()#取股名列的数据转化为list,内容为str
for code in code_list:
    df_new=pro.index_daily(ts_code=code, start_date='20171001', end_date='20171031')#获取指数数据
    df=pd.concat([df,df_new],axis=0,ignore_index=True)
	#合并2个df 数据,axis=1横向合拼,=0纵向合并,ignore_index=True自动编号

df.to_excel('E:/pyNote/调用资料/63classNew.xlsx','Sheet1')
