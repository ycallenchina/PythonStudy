import os

x=input('打开几号文件：')
print(x)

print(type(x))
print(f'start e:/pyNote/{x}.txt')
os.system(f'start e:/pyNote/调用资料/{x}.txt')
#插入中间字符串写法
print(f'123{x}68')