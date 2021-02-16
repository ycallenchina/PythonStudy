
import pandas as pd
import numpy as np
import chardet
#副
def 找遍所有文件里某类型文件的路径(path,x=4,s='.csv'):
    '''   输入:#找遍path文件夹里所有尾部最后x=3位为s='.py'的文件
          输出:list类型所有文件路径的列表'''

    import os
    所找文件路径 = []
    #在walk的第二层里,排除venv文件夹
    for 二层 in os.walk(path):
        if 'venv' in 二层[0]:
            pass
        else:
            #在第二层的下一层第三个包里,找最后3个字符等于.py的.
            for 四层 in 二层[2]:
                if 四层[-(x):]==s :
                    所找文件路径.append((二层[0]+'/'+四层,四层))
    return 所找文件路径
#副
def clean(x):#清洗数据类型为str的数据
    if isinstance(x,str):
        x=x.strip()
    else:
        pass
    return x

def 金额列clean(df):
    df[["记账金额","余额"]]=df[["记账金额","余额"]].applymap(str)#未知列的格式,统一全为文本
    df[["记账金额","余额"]]=df[["记账金额","余额"]].applymap(lambda x:x.replace(',',''))
    df[["记账金额","余额"]]=df[["记账金额","余额"]].applymap(float)
    return df
def 金额列clean2(df):
    df[["金额_元"]]=df[["金额_元"]].applymap(lambda x:x.replace('¥',''))
    df[["金额_元"]]=df[["金额_元"]].applymap(lambda x:x.replace(',',''))
    df[["金额_元"]]=df[["金额_元"]].applymap(float)
    return df
#副
def 插入索引列(df):

    col_name = df.columns.tolist()#列名转为列
    col_name.insert(0,'序号')#第一列插入序号
    df=df.reindex(columns=col_name)#改列名,已增加列
    for index,row in df.iterrows():
        df.loc[index,'序号']=int(index+1)#用loc方法填充每行序号
    return df

#副    
def 增加期数_核销列(df,期数):
    df['财务期']=期数
    df['核销']=''
    return df
#副
def 优化列名_forSQL(df):
    #清洗列名,sql语法要求
    col_name = df.columns.tolist()
    j=0
    for i in col_name:
        #改名方法
        col_name[j]=col_name[j].strip()#去两头空格
        col_name[j]=col_name[j].replace('(','_')#置换括号/等,sql语法要求列名不能有括号
        col_name[j]=col_name[j].replace('（','_')
        col_name[j]=col_name[j].replace(')','')
        col_name[j]=col_name[j].replace('）','')
        col_name[j]=col_name[j].replace('/','')
        j+=1
    df.columns=col_name#替换原有列名
    return df
#副
def 整合收支列(df):
    df=df.where(df.notnull(),'')
    df['收_支']='支出'#增加收_支列,填充字符串'支出'
    for index in df.index:
        if df.loc[index,'记账金额_收入'] !='':
            df.loc[index,'记账金额_支出']=df.loc[index,'记账金额_收入']
            df.loc[index,'收_支']='收入'
    df.rename(columns={'记账金额_支出':'记账金额'}, inplace = True)#把合并的列名改为金额交易.
    return df
#副    
def 精炼列(表名,df):
    if "信用卡" in 表名:
        df['备注']=''
        df=df[['序号','交易日期','摘要','交易场所','记账金额','收_支','记账币种','余额','对方户名','备注','财务期','核销']]
    elif '金卡' in 表名:
        df['备注']=''
        df=df[['序号','交易日期','摘要','交易场所','记账金额','收_支','记账币种','余额','对方户名','备注','财务期','核销']]
    elif '支付宝' in 表名:
        df['余额']=0
        df['付款方式']=''
        df=df[['序号','付款时间','交易来源地','交易对方','商品名称','收支','金额_元','余额','交易状态','服务费_元','成功退款_元','资金状态','备注','财务期','核销']]       
    elif '微信' in 表名:
        df['余额']=0
        df=df[['序号','交易时间','交易对方','收支','金额_元','支付方式','余额','当前状态','备注','财务期','核销']]
    else:
        pass
    return df

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

#主
def 清洗excel表数据(表名,期数):
    import pandas as pd
    import numpy as np

    df=读csv为df(表名)
    #处理数据
    df=插入索引列(df)
    df=增加期数_核销列(df,期数)
    df=优化列名_forSQL(df)
    df=df.applymap(clean)#str类型数据去两头空格
    if '卡'in 表名:#只有工行卡要整合收支.
        df=整合收支列(df)
        df=金额列clean(df)
    if '微信'in 表名:#微信的金额列
        df=金额列clean2(df)
    df=精炼列(表名,df)
    df=df.where(df.notnull(),'')#最后去掉NAN

    return df

def 批量清洗(文件路径,保存路径,期数):

    All_file=找遍所有文件里某类型文件的路径(文件路径)
    for i in All_file:
        print('正在处理:',i[1])
        
        清洗excel表数据(i[0],期数).to_csv(保存路径+'/'+i[1],encoding='utf_8_sig',index=False)
        print('处理完成:',i[1])

    return

if __name__ == '__main__':
    
    文件路径="C:/Users/YcAllenEffy/Desktop/已处理账表1次"
    保存路径="C:/Users/YcAllenEffy/Desktop/已处理账表2次"
    期数='21年1期'
    批量清洗(文件路径,保存路径,期数)



