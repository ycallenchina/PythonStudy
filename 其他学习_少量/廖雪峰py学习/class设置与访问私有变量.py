# 拒绝外部访问变量
"""如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，
外部不能访问，所以，我们把Student类改一改："""
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender= gender
    # 访问私有变量方法
    def set_gender(self,gender):
        self.__gender = gender
        return self.__gender
    def get_gender(self):

        return self.__gender

bart = Student('Bart', 'male')
"""不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name"""
print(bart._Student__name)
# 测试新建方法访问与修改
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')