class made_db(object):
    def __init__(self):
        self.list=[]

    def 扁平化多维列表(self,N):

        '''#输入：仅限列表和元组
           #输出：一维列表'''
        for i in N:
            if isinstance(i, list) or isinstance(i, tuple):
                self.扁平化多维列表(i)
            else:
                self.list.append(i)
        return self.list

a=[1,2,[4,4],(2,2)]
b=made_db()
c=b.扁平化多维列表(a)
print(c)


#仅用函数的递归扁平算法
def changeto_1list(N):#扁平多维列表或元组为一维列表

    q=[]
    def changeto_1list(N):
        for i in N:
            if isinstance(i, list) or isinstance(i, tuple):
                changeto_1list(i)
            else:
                q.append(i)
    changeto_1list(N)
    return q

a=[1,2,[4,4],(2,2)]
print(changeto_1list(a))


def unpack_SQLfig(n):#解包多维数据
    for i in n:
        if isinstance(i, tuple):
            return unpack_SQLfig(i) #为了使递归里面的函数往回传递数据的方法
        else:
            return i

