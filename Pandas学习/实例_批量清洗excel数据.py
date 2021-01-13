
import pandas as pd
import numpy as np
import chardet
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

def clean(x):#清洗数据类型为str的数据
    if isinstance(x,bool):#因为bool类型也属于str
        return x 
    elif isinstance(x,str):
        x=x.strip()
    else:
        pass
    return x


def 清洗excel表数据(表名):
    import pandas as pd
    import numpy as np
    import chardet

    #先判断文件编译方式,获得编码的encoding
    with open(表名,'rb') as file:
        s=file.read()
        d=chardet.detect(s)
        编译方式=d['encoding']

    #读取excel表格  
    df=pd.read_csv(表名,encoding=编译方式)
    #处理数据
    df2=df.applymap(clean)
    return df2#返回新dataframe

待清洗文件路径="C:/Users/YcAllenEffy/Desktop/待处理账表"
q=找遍所有文件里某类型文件的路径(待清洗文件路径)
for i in q:
    保存路径="C:/Users/YcAllenEffy/Desktop/已处理账表"
    清洗excel表数据(i[0]).to_csv(保存路径+'/'+i[1],encoding="utf_8_sig")