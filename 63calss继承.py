#继承学习
#1.子类如何继承父类的属性及方法
#2.子类如何拥有自己特别的属性和方法
#3.多态引用子类运行
#4.如何查看子父的关系:isinstance
class man:
	def __init__(self):
		self.name='im man'
		self.age='im yong'

	def say(self):
		print(f'{self.name},{self.age}.hello everone!')

class chinese_man(man):
	def __init__(self):
		man.__init__(self)#添加自己的属性前,先加载父类的属性
		self.name='im chinese_man'#拥有自己特别的属性:用同名属性盖过父类的属性.
	
	#有同名方法时,子类覆盖父类.
	def say(self):
		print(f'你好,{self.name},{self.age}.hello everone!')

class korean_man(man):
	def __init__(self):
		man.__init__(self)
		self.name='im korean_man'
	
	def say(self):
		print(f'欧巴,{self.name},{self.age}.hello everone!')

#完全继承时,属性和方法都与父类不同名,就会拥有父类所以属性和方法
class world_man(man):
	pass;

A=[chinese_man(),korean_man(),world_man()]

for i in A:
	i.say()
	print('-----')


#子类属于父类,同子类相互没有归属关系.
#补充:isinstance(实例,类名),实例必须有chinese_man()括号,类名man没有括号.
print('chinese_man属于man类么:',isinstance(chinese_man(),man),'\n',
	  'korean_man属于man类么:',isinstance(korean_man(),man),'\n',
	  'world_man属于chinese_man类么:',isinstance(world_man(),chinese_man)	
	  )
