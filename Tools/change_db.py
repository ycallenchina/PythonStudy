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