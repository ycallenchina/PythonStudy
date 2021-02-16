
a=['a','b','c']
b=[1,2,3]

#字典生成式
dic={k[0]:k[1] for k in zip(a,b)}
print(dic)

#zip生成字典
dic2=dict(zip(a,b))
print(dic2)

#字典生成式 -带判断语句
dic={k[0]:k[1] for k in zip(a,b) if k[1]>1}
print(dic)

