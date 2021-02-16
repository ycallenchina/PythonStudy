# class学习_类后面有括号和没有括号的区别
# 有括号就是执行方法,没有括号就是使用它的属性值
class clsTest():
    y = '000'
    q = '111'

    def __init__(self):
        self.y = '你'

x = clsTest
print(x.y,x.q)
x = clsTest()
print(x.y)