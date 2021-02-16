# 用105文本输入，方便的建立一个需要统计字符的字典dic

# 读取文本为列表,但是列表的字符串里含有\n换行符号
f=open('e:\pyNote\调用资料/105.txt','r',encoding='utf-8')
p=f.readlines()
x=''.join(p)
k=x.split('\n')
# 去换行符\n方法,先转换为字符串,再用\n做分隔符转回列表--k
#新建字典方法fromkeys
dic= dict.fromkeys(k,0)

# 
# 测试:print('宝钗你还好么,我的宝钗'.count('宝钗'))
f2=open('e:\pyNote\调用资料/红楼梦.txt','r',encoding='utf-8')
p2=f2.readlines()

for line in p2:
    for girls in dic:
    	# 统计字典的每个key里的value.
        dic[girls]=dic[girls]+line.count(girls)
print(dic)

# 给字典的值排序,生成元组,默认为升序，reverse = True变为倒序排列
list1=sorted(dic.items(),key=lambda x:x[1],reverse = True)
print(list1)

# for y in dic:
#     print(y,'出现了',dic[y],'次')
#
f.close()
f2.close()
