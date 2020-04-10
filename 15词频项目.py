

f=open('e:\pyNote\调用资料/红楼梦.txt','r',encoding='utf-8')

# readlines方法有最大限额,所以截断了西游记1/3成西游记2来用.
k=0
for i in f.readlines():
     if '宝钗' in i:
        k+=1
        
print('宝钗：',k)

f.close()

def