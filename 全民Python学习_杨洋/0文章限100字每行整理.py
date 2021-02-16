# 打开文件,写入文件
f=open('e:/pyNote/调用资料/红楼梦.txt', 'r', encoding='utf-8')
f2=open('e:/pyNote/调用资料/entry.txt', 'w', encoding='utf-8')


new=[]
for i in f.readlines():
    if i  !='\n':
        while len(i)>100:
             # 每行多于100字就换行,循环
             f2.write(i[:100]+'\n')
             i = i[100:]
        else:
            f2.write(i)

f.close()
f2.close()
