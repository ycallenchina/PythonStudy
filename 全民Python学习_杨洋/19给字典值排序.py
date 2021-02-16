import partA

y=[i for i in range(3)]
x=['eat','good','go']
dic=partA.madedic(x,y)
dic['good']=3
print(dic)
# 给字典按照值排序,生成新的字典,reverse默认为False,为True时倒序排列
list1=sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(list1)
