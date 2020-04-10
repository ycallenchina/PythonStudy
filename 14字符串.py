
# 字符串与列表相似的属性和方法
x='1231245234'

print(x[::-1])
print(x[3])

# 字符串与列表的不同
# 字符串不能直接赋值修改，不过可以用切片方法修改
# replace方法--修改文本里的所有重复字符
x1='015你好不好'
print(x1.replace('好','死'))
# count:统计出现次数
y=x1.count('好')
print(y)
# strip() 去空格，准确用法：去掉字符串里头尾的，strip里参数
j='   家具   '  
j1=j.strip()#默认是去掉两头空格
print(j1.strip('具'))
print('000')



# s=[str(i) for i in s] 列表生成器新写法
# s=''.join(s) 列表变字符串方法
# y.split('j')  字符串变列表

# s.find(4)
# s.find('4')   找位置
# s.find('0')
# s.find(4,11)
# s.find('4',11)
# s.count()     出现次数
# len(s)
# s.rfind('4')
# y='      54654654    '

# y
# y.lstrip()
# y='SkjkljlkLKJLlkdkfd'
# y.lower()     变小写
# y.upper()
# y.swapcase()
# y.title()
# y.capitalize()首字母大写

