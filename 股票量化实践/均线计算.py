import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
import time 

def 读csv为df(表名):
    import pandas as pd
    import numpy as np
    import chardet
    #先判断文件编译方式,获得编码的encoding
    with open(表名,'rb') as file:
        s=file.read()
        d=chardet.detect(s)
        编译方式=d['encoding']
    #读取excel表格  
    df=pd.read_csv(表名,encoding=编译方式,index_col=False)
    return df

def 保存csv文件(保存路径,df):
    df.to_csv(保存路径,encoding='utf_8_sig',index=False)



def 前4天价格总和(df,date):

    L=list(df['date'])#取日期为列表

    L_4=L[L.index(date)-4:L.index(date)]#把日期列表里date的前四天date取出
    sumL_4=[df[df['date'].str.contains(i)]['close'].iloc[0] for i in L_4]#取出前四天date对应的收盘价.
    return sum(sumL_4)#计算出前四天收盘价总和

def Str_to_Datetime(s): #读取时间方法
    t1=datetime.strptime(s,'%Y-%m-%d')
    return t1


def 增加ma列(df):
    #规范 类似格式
    df['close']=df['close'].apply(float)
    df['open']=df['open'].apply(float)
    df['time']=df['time'].apply(str)#把时间列的数据int类变为str类

    df_close_time=df[df['time'].str.contains("150000000")]#标记每日收盘价
    start=df['date'].loc[0]
    ma_start=Str_to_Datetime(start)+timedelta(days=4)
    now_date=''#初始化日期,重复日期不操作,不重复日期才计算

    #逐个记录前4个交易的价格总和.
    for index,row in df.iterrows():
        if Str_to_Datetime(row['date'])>=ma_start:#4天后的记录
            if now_date!=row['date']:
                price_4days=df.loc[index,'new']=前4天价格总和(df_close_time,row['date'])
                now_date=row['date']#记录本次日期用于下个日期的对比.
            else:
                #如果上次日期和本次日期一致则,记录与上次日期一样的价格.
                df.loc[index,'new']=price_4days

    #逐个计算前4个交易日的价格总和加上目前实时的价格,除以5得到实时的ma5均线.
    for index,row in df.iterrows():
        if Str_to_Datetime(row['date'])>=ma_start:
            df.loc[index,'ma5']=round((row['new']+row['close'])/5,2)

    df=df[df['ma5'].notnull()]#只保留ma5里有数值得记录,去掉'ma5'列里为NaN值得记录.

    return df

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)#显示所有df列
    路径='C:/Users/YcAllenEffy/Desktop/222.csv'
    df=读csv为df(路径)

    df=增加ma列(df)

    # 保存路径='C:/Users/YcAllenEffy/Desktop/333.csv'
    # 保存csv文件(保存路径,df)
    # df=df.applymap(type)
    print(df)