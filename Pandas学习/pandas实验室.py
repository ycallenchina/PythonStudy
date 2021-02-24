

import pandas as pd
import numpy as np
import chardet

def Random_Time(size):
    import datetime
    import time
    import random
     
    end_time=datetime.datetime.now()
    start_time=datetime.datetime.now() + datetime.timedelta(days=-10) # 当前时间减去3分钟
     
    a1=tuple(start_time.timetuple()[0:9])    #设置开始日期时间元组（2020-04-11 16:30:21）
    a2=tuple(end_time.timetuple()[0:9])   #设置结束日期时间元组（2020-04-11 16:33:21）
     
    start=time.mktime(a1)    #生成开始时间戳
    end=time.mktime(a2)      #生成结束时间戳
     
    #随机生成日期字符串
    time_list=[]
    for i in range(size):
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y-%m-%d %H:%M:%S",date_touple)  #将时间元组转成格式化字符串（2020-04-11 16:33:21）
        time_list.append(date)
    
    return tuple(time_list)


boolean=[True,False]
gender=["男","女"]
color=["white","black","yellow"]
df1=pd.DataFrame({
    "height":np.random.randint(150,190,10),
    "weight":np.random.randint(40,90,10),
    "smoker":[boolean[x] for x in np.random.randint(0,2,10)],
    "gender":[gender[x] for x in np.random.randint(0,2,10)],
    "age":np.random.randint(15,90,10),
    "color":[color[x] for x in np.random.randint(0,len(color),10) ]
    }
)    
df2=pd.DataFrame({
    "height":np.random.randint(150,190,10),
    "weight":np.random.randint(40,90,10),
    "smoker":[boolean[x] for x in np.random.randint(0,2,10)],
    "gender":[gender[x] for x in np.random.randint(0,2,10)],
    "age":np.random.randint(15,90,10),
    "color2":[color[x] for x in np.random.randint(0,len(color),10) ]
    }
) 
df3=pd.DataFrame({
    "time":Random_Time(10),
    "height":np.random.randint(150,190,10),
    "weight":np.random.randint(40,90,10),
    "smoker":[boolean[x] for x in np.random.randint(0,2,10)],
    "gender":[gender[x] for x in np.random.randint(0,2,10)],
    "age":np.random.randint(15,90,10),
    "color2":[color[x] for x in np.random.randint(0,len(color),10) ]
    }
    )

def 金额列clean(df):
    df[["记账金额","余额"]]=df[["记账金额","余额"]].applymap(lambda x:x.replace(',',''))
    df[["记账金额","余额"]]=df[["记账金额","余额"]].applymap(float)
    return df

def 保存csv文件(保存路径,df):
    df.to_csv(保存路径,encoding='utf_8_sig',index=False)#不要索引

def 读取csv(表名):
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

def 测试SQL语句(sql):
    import  pymysql.cursors
    # 加载mysql
    connection=pymysql.connect(host='localhost',
                               user='root',
                               password='123456',
                               db='test_data',
                               port=3306,
                               charset='utf8')

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.close()
def 插入索引列(df):

    df['序号']=''
    # df.loc[0,'序号']=99
    #填充序号
    for index,row in df.iterrows():
        df.loc[index,'序号']=int(index+1)#用loc方法填充每行序号
    return df

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)#显示所有df列

    df3['time'] = pd.to_datetime(df3['time'])
    print(df3)
    df3=df3[df3['time']>'2021-2-10']
    df3=df3[df3['time']<='2021-2-13']
    print(df3)
