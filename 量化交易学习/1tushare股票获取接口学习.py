import tushare as ts
#获取大盘指数
# df=ts.get_hist_data('000860',start='2019-11-11',end='2019-11-15')
df=ts.get_today_all()#获取当日全部数据
# dataframe取值,从表里取值:取第二行的值df.iloc[1]
# dfname._stat_axis.values.tolist() # 行名称
# dfname.columns.values.tolist()    # 列名称
print(df)
print(df._stat_axis.values.tolist())#行
print(df.columns.values.tolist())#列
# for j in range(len(df)):
#     for i in df.iloc[j]:
#         print(i)

# 导入excel
# df.to_excel('e:/pyNote/调用资料/股票.xlsx')
# # 行业分类数据
# df=ts.get_industry_classified()
# print(type(df))
# 保存为excel
# df.to_excel('e:/pyNote/调用资料/股票.xlsx')#一次性获取全部日k线数据


# date：日期
# open：开盘价
# high：最高价
# close：收盘价
# low：最低价
# volume：成交量
# price_change：价格变动
# p_change：涨跌幅
# ma5：5日均价
# ma10：10日均价
# ma20:20日均价
# v_ma5:5日均量
# v_ma10:10日均量
# v_ma20:20日均量
# turnover:换手率