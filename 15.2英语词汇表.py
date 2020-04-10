

f=open('e:\pyNote\调用资料/english.txt','r',encoding='utf-8')

all=[]
# 生成词汇列表
for i in f.readlines():
    # 置换标点,统一小写
    i=i.replace(',',' ')
    i=i.replace('.',' ')
    i=i.lower()
    # 生成列表use空格
    i=i.split(' ')
    # 汇总
    all.extend(i)

# 去重复-集合特性法,排序
all=list(set(all))
all.sort()

# 写入新txt,用jion方法转化为字符串.
f2=open('e:\pyNote\调用资料/englishTRY.txt','w',encoding='utf-8')
f2.write('\n'.join(all))
f2.close()

f.close()





