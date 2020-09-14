
		
class mishu(object):
	def __init__(self, arg='无名'):
		self.name = arg

	def sayhello(self):#用self来代表自身
		print('领导你好,我是',self.name)

	def id(self):#self为实例中每次自动第一个传入的参数.
		print('我的内在self地址是:', id(self))
	def no_id():#如果不写self,会报错,no_id() takes 0 positional arguments but 1 was given
		print('试试')

m1=mishu()#创建类
m2=mishu()
print('m1,m2类型:',type(m1),type(m2))#m1,m2开辟了不同的地址
print('m1,m2地址',id(m1),id(m2))
print()

m1.name='张秘书'#实例,添加属性
m1.sayhello()#执行方法
print()

m1.id()#理解对self的用法.
print('我的外在对象的id是:',id(m1))
