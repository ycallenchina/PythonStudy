# 获取对象信息
    #type()
import types
class En():
    pass
print(type(123),type('str'),type(En()))
print('---------------------------------------------------# 对象是否是函数怎么办-.1')


def fn():
        pass
print(
    type(fn)==types.FunctionType,
    type(abs)==types.BuiltinFunctionType,
    type(lambda x: x)==types.LambdaType,
    type((x for x in range(10)))==types.GeneratorType
    )
print('------------------------------------------------------# 使用isinstance().2')

class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Husky(Animal):
    def run(self):
        print('Cat is running...')

a = Animal()
d = Dog()
h = Husky()
print(isinstance(h, Husky))
# 还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print('-----------------------------------------------------------# 使用dir().3')
print(dir('abc'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
print(
    len('abc'),
    'abc'.__len__(),
    )
# 获取属性getattr()、设置属性setattr()以及有没有属性hasattr()
class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x * self.x
print('---------------#获取属性getattr()、设置属性setattr()以及有没有属性hasattr().4')

obj=MyObject()

fn=obj.power

print(hasattr(obj, 'x'),
      setattr(obj, 'y',19),
      getattr(obj, 'y'),
      fn()
  )