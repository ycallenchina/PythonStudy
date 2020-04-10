#函数递归
# 函数中调用自身,称作递归
# 大而化小,分而治之
# 递归函数必须有结束条件,不能无线递归
# 累加器
def cum_self(N):
    if N==1:
        return 1
    else :
        return N+cum_self(N-1)
print(cum_self(6))
#常规斐波那契数列
c=[1,1]
for i in range(2,10):
    c.append(c[i-2]+c[i-1])
print(c)
#递归算法的斐波那契下标数
def fibo(N):
    if N==1 or N==2:
        return 1
    else:
        return fibo(N-1)+fibo(N-2)
print(fibo(21))
#20米,每次可走1米或2米,计算出走完所以的方法
def jiaobu(k):
    if k==1:
        return 1
    elif k==2:
        return 2
    else :
        return jiaobu(k-1)+jiaobu(k-2)
print(jiaobu(20))
#汉诺塔
#三根柱子,移动圆盘,每次一个,大的圆盘在小的下面,全部移到能一个柱子
def hano(N,source,target):
    if N==1:
        print(1,source,'=>',target)
    else:
        pi=['A','B','C']
        pi.remove(source)
        pi.remove(target)
        media=pi[0]

        hano(N-1,source,media)
        print(N,source,'=>',target)
        hano(N-1,media,target)
hano(3,'B','C')

#递归扁平 多维列表
a=[[121.0, 55.0, 555.0, [3,2,4,[5,6]], 454.0, 232.0], [323.0, 455.0, [1,2,3], 323.0, 455.0, 233.0]]
b=[]
def k(N):
    for i in N:
        if isinstance(i, list):
            k(i)
        else:
            b.append(i)
k(a)
print(b)