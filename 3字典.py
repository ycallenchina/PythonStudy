
#导入列表
f=open('e:/pyNote/调用资料/105.txt','r',encoding='utf-8')
p=f.readlines()
b=[i.strip() for i in p]

#生成字典
dic= dict.fromkeys(b,0)
vau=[i for i in range(len(b))]
for i,j in zip(dic,vau):
	dic[i]=j
print(dic)

#修改字典print()
dic['邱婷婷']=dic.pop('宝钗')
print(dic)

