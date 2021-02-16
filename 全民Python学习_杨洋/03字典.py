
#导入列表,读取105文本
f=open('e:/pyNote/调用资料/105.txt','r',encoding='utf-8')
p=f.readlines()
b=[i.strip() for i in p]#逐行提取文本,并去两端空格

#生成字典
dic= dict.fromkeys(b,0)
print(dic)

#修改字典print()
dic['宝钗']=10
#执行删除'宝钗'键时,会一并返回对应的值,所以可以增加新键,并取代删除键的值
dic['取代宝钗']=dic.pop('宝钗')
print(dic)


