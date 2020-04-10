

f=open('e:\pyNote\调用资料/105.txt','r',encoding='utf-8')
p=f.readlines()
print(p)
x=''.join(p)
print(x)
k=x.split('\n')
# 去\n方法:先转换为字符串,再用\n做分隔符转回列表--k

#创建字典,初始化值为0
dic= dict.fromkeys(k,0)
print(dic)

# 用打包方法zip： 双循环，双列表生成字典
vau=[i for i in range(10)]
for i,j in zip(dic,vau):
	dic[i]=j
print(dic)