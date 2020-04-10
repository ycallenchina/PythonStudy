# 统计词频__给定文章的路径,一个列表,统计文章里的词频.返回字典
def wordcount(adr,k):
    dic= dict.fromkeys(k,0)
    f2=open(adr,'r',encoding='utf-8')
    p2=f2.readlines()

    for line in p2:
        for girls in dic:
            dic[girls]=dic[girls]+line.count(girls)

    f2.close()
    return dic
# 生成字典__给定两个列表x,y,按循序生成字典.
def madedic(x,y):
    dic={}
    for i,q in zip(x,y):
        dic[i]=q
    return (dic)

# 词汇表__给1,2两个字符串,在'e:\pyNote\调用资料/'路径下,读取no.1文章,生成词汇表,创建no.2文件.
def madewordlist(adr1,adr2):
    import jieba
    f=open('e:\pyNote\调用资料/'+adr1,'r',encoding='utf-8')
    all=[]
    # 生成词汇列表
    for i in f.readlines():
        # 用jieba来分词
        all.extend(jieba.lcut(i))

    # 去重复-集合特性法,排序
    all=list(set(all))
    all.sort()
    # 写入新txt,用jion方法转化为字符串.
    f2=open('e:\pyNote\调用资料/'+adr2,'w',encoding='utf-8')
    f2.write('\n'.join(all))
    f2.close()
    return
