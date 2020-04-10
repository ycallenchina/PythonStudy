
import tushare as ts
#获取大盘指数
df = ts.get_index()
print(df)
print(type(df))
# # 行业分类数据
# df=ts.get_industry_classified()
# print(type(df))
# 保存为excel
# df.to_excel('e:/pyNote/调用资料/股票.xlsx')#一次性获取全部日k线数据