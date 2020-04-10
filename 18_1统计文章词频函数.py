#先给需要分析的文本全路径，以及需要统计词的列表。返回字典。

def wordcount(adr,k):
    dic= dict.fromkeys(k,0)
    f2=open(adr,'r',encoding='utf-8')
    p2=f2.readlines()

    for line in p2:
        for girls in dic:
            dic[girls]=dic[girls]+line.count(girls)

    f2.close()
    return dic
k=['宝钗','黛玉']
a='e:\pyNote\调用资料/红楼梦.txt'
dic=wordcount(a,k)
print(dic)
