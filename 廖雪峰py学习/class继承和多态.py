# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class pig(Animal):
    pass

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
# 继承好处一:
    # 最大的好处是子类获得了父类的全部功能。
    # 由于Animial实现了run()方法，因此，pig作为它的子类，什么事也没干，就自动拥有了run()方法
p=pig();p.run();d=Dog();c=Cat()

# 继承好处二:多态
    # 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
    # 在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处
    # 子类实例是父类,父类实例不是子类
d.run();c.run()

# 类型判断
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
print(isinstance(c, Animal))
print(isinstance(b, Dog))

def run_twice(animal):
    animal.run()
    animal.run()