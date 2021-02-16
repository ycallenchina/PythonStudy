# 简易搜索---把文件里包括？的内容那一行显示出来。

# 输入内容neiro
neiro=str('转换')

# 打开要搜索的文本
f = open('e:\pyNote/调用资料/整理.txt', 'r', encoding='utf-8')
for i in f.readlines():
    if neiro in i:
        print(i)
        #消除换行符
        # x = ''.join(i)
        # k = x.split('\n')
        # x=''.join(k)
        # print(x)
