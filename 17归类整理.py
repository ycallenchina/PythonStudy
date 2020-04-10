# 把目录下.py的所有文件，按照目录和带有#号的内容，整理到一个txt的文件里。

import os
# import re(备用正则表达式资料)
# s=re.findall(r"\d+\.?\d*",str(mulu_py))

# 得到后缀py的目录mulu_py
mulu=os.listdir('e:\pyNote')
mulu_py=[]
for i in mulu:
    if '.py' in i:
        mulu_py.append(i)

# 生成新记事本‘整理’txt记录
w = open('e:\pyNote/调用资料/整理.txt', 'w', encoding='utf-8')
# 依次打开目录提取内容,k计数行
k=0#k是序列用
for i in mulu_py:
    k=k+1
    # 先写入目录名,并打开此目录
    w.write(str(k)+'___'+i + '\n\n')
    f = open('e:\pyNote/' + i, 'r', encoding='utf-8')
    #提取lines内容,带有#的注释内容,并写入w
    for i in f.readlines():
        if '#' in i:
            k=k+1
            w.write(str(k)+'        '+i+'\n')
print(1)
f.close()
w.close()