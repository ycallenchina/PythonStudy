# read,readline,seek,方法的用法
a=open('go.txt',encoding='utf-16')
#a.read()读完整篇文章 r,r2循序读取行,已经结尾所以读不到信息
print(a.read())
r=a.readline()
print(r)
r2=a.readline()
print(r2)
# seek后重新读取第一行信息
a.seek(0)
r3=a.readline()
print(r3)