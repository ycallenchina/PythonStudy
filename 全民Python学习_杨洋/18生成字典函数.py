# 先给两个等长的列表，或者序列，生成字典

def madedic(x,y):
    dic={}
    for i,q in zip(x,y):
        dic[i]=q
    return (dic)

x=['eff','allen','happy']
y=[i for i in range(3)]

dic=madedic(x,y)
print(dic)