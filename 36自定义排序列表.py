import random
#读文本,产以为列表b
f=open('e:\pyNote\调用资料/105.txt','r',encoding='utf-8')
p=f.readlines()
b=[i.strip() for i in p]
#生成字典
dic= dict.fromkeys(b,0)
vau=[random.randint(1,5) for i in range(len(b))]
print('vau',vau)
for i,j in zip(dic,vau):
	dic[i]=j
print('dic',dic)
#生成2维列表c
c=list(zip(b,vau))
print('c',c)
#排序方法:
def degree(s):
    return dic[s[0]]
#给2维列表从排序
c.sort(key=degree)
print('排序后的c',c)


