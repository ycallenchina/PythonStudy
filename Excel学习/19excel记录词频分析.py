#打开f路径的文件，用jieba分词生成k列表，再去重复的词语生成n k列表，再k列表里统计n k的每个词出现次数。
# 用双循环生成字典并排序，排序后会生成一个list1列表。由元组对组成。
# 最后写入excel
import jieba

f = open('e:\pyNote\调用资料/日记.txt', 'r', encoding='utf-8')
k = []
# 生成词汇列表
for i in f.readlines():
    # 用jieba来分词
    k.extend(jieba.lcut(i))
# 去列表重复，得到一个没有重复的词语表
n_k = list(set(k))

# 做内容统计：提取n_k里每个词，再重复的原表k里出现的次数。

n_k1 = []
for i in n_k:
    n_k1.append(k.count(i))
# 因为n k 和 n k1有顺序的，所以可以用双循环来生成字典,再按倒序排列
dic = {}
for n1, n2 in zip(n_k, n_k1):
    dic[n1] = n2
list1 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# print(list1)

# 建立新excel并写入
import xlwings as xw

app = xw.App()
wb = app.books.add()
ws = wb.sheets[0]
ws.range('B2').value = list1

wb.save('E:\pyNote\调用资料/try333.xlsx')
wb.close()
app.quit()