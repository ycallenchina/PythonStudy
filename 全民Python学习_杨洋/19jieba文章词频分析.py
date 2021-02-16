#打开f路径的文件，用jieba分词生成k列表，再去重复的词语生成n k列表，再k列表里统计n k的每个词出现次数。
# 用双循环生成字典并排序，排序后会生成一个list1列表。由元组对组成。
# 最后写入txt文本
import jieba

f = open('e:\pyNote\调用资料/日记.txt', 'r', encoding='utf-8')
k = []
# 生成词汇列表
for i in f.readlines():
    # 用jieba来分词
    k.extend(jieba.lcut(i))
# 去重复
n_k=list(set(k))
n_k1=[]
# 统计
for i in n_k:
    n_k1.append(k.count(i))

# 双循环生成字典。
dic={}
for n_k,n_k1 in zip(n_k,n_k1):
    dic[n_k]=n_k1
list1=sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(list1)

f2= open('e:\pyNote\调用资料/entry.txt', 'w', encoding='utf-8')

# 写回进去新文本里
for i in list1:
    # f2.write('\n')
    # for a in i:
    #     f2.write(str(a))
    i2=''.join(str(i))
    i2=i2+'\n'
    f2.write(i2)

f.close()
f2.close()

