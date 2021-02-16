# 在'e:\pyNote\调用资料/'路径下,给字符串adr1（分析文件的名字） ，adr2（新文件名）。这是执行函数，没有返回值。
    #得到的是一个没有重复的单词列表
def madewordlist(adr1,adr2):
    f=open('e:\pyNote\调用资料/'+adr1,'r',encoding='utf-8')
    all=[]
    # 生成词汇列表
    for i in f.readlines():
        # 置换标点,统一小写
        i=i.replace(',',' ')
        i=i.replace('.',' ')
        i=i.lower()
        # 生成列表use空格
        i=i.split(' ')
        # 汇总
        all.extend(i)
    # 去重复-集合特性法,排序
    all=list(set(all))
    all.sort()
    # 写入新txt,用jion方法转化为字符串.
    f2=open('e:\pyNote\调用资料/'+adr2,'w',encoding='utf-8')
    f2.write('\n'.join(all))
    f2.close()
    return

a='english.txt'
b='entry.txt'

madewordlist(a,b)