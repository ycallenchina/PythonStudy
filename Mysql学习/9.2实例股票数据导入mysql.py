import  pymysql
import  pymysql.cursors
import tushare as ts

# 加载mysql
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
# 填写股票名,和时间
symbol='600118'
time1='2019-11-11'
time2='2019-11-15'
#获取股票数据
df=ts.get_hist_data(symbol,start=time1,end=time2)
x=df._stat_axis.values.tolist()#读取行名:日期
# 确保数据提取成功print一下
print(df)

# 创建表:symbol=股票名,表名=code股票名(因为表名不能是数字)
cursor = connection.cursor()
code_symbol='code'+symbol
sql =f"CREATE TABLE {code_symbol}(Date varchar(255),close varchar(255),p_change varchar(255),volume varchar(255),PRIMARY KEY (`Date`)) DEFAULT CHARSET=utf8;"
# 执行sql语句:创建表
cursor.execute(sql)

# 逐行读取数据入mysql
for j in range(len(df)):
    # 执行sql语句,其中x为dataframe提取的行名,日期
    # j为行变量,数字均为固定列:例如df.iloc[j][2] df数据的第j行第2列的数据
    # 提取的数据为:x列 日期,2列 收盘close,6列 涨福p_change,4列 成交量_volume
    sql=f"INSERT INTO {code_symbol} VALUES ('{x[j]}','{df.iloc[j][2]}','{df.iloc[j][6]}','{df.iloc[j][4]}')"
    cursor.execute(sql)

connection.close()
