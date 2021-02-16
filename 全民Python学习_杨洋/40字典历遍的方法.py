#建立 初始列表b
f=open('e:\pyNote\调用资料/2.txt','r',encoding='utf-8')
r=f.readlines()
b=[i.strip() for i in r]
print(b)
#统计出现次数,各个次数出现多少次
d={k:b.count(k) for k in b}
print(d)
m=list(d.values())
print(m)
d2={k:m.count(k) for k in m}
print(d2)

#求字典最大值
big=max(d.values())
d3={k:d[k] for k in d if d[k]==big}
print(d3)

#把字典转换为二维列表
print(d.items())
#调换键值的方法
d2={v:k for k,v in d.items()}
print(d)
print(d2)

#解包
a,c,*e=1,2,3,5,6
print(e)