#
# import jieba
#
# f=open('e:\pyNote\调用资料/english.txt','r',encoding='utf-8')
# all=[]
# # 用append拆分字符串实验append和exend
# q=[]
# i='im a teach,but i am not happy'

j=['99999']
# q.append(i[0:5])
# q.append(i[5:-1]+i[-1])
# print(i[5:])
q=j.append('111')
print(q)
# 生成词汇列表,用extend方法:函数用于在列表末尾一次性追加另一个序列中的多个值(append区别在于append(obj)用于对象)
# append和extend区别结果举例:print(a+b)a,b=[],append结果[['ee', '2323']],extend结果['ee', '2323']
# # append和extend区别结果举例2:print(a+b)a,b='字符串',append结果['ee2323'],extend结果['e', 'e', '2', '3', '2', '3'],效果等同拆分字符
# for i in f.readlines():
#     all.extend(jieba.lcut(i))
# # 去重复-集合特性法,排序
# all=list(set(all))
# all.sort()
# # 写入新txt,用jion方法转化为字符串.
# f2=open('e:\pyNote\调用资料/entry.txt','w',encoding='utf-8')
# f2.write('\n'.join(all))
# f2.close()
