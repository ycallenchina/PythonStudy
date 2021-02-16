


#装饰器高阶函数的用法
def senior_q(f):#高级的senior
	def new(r):
		print("高阶函数,已装饰")
		return f(r)
	return new

def for_girth(r):#求周长girth
	return 3.14*r*2

for_girth=senior_q(for_girth)

print(for_girth(3))



#装饰器@wraps的用法
print('#装饰器@wraps的用法----------------------')
from functools import wraps 

def q(f):
	@wraps(f)
	def new(r):
		new33=str(f(r))+':我已经被装饰'
		return new33
	return new

@q#作用等于p=q(p),所以p已经被装饰
def p(r):
	return 3.14*r*2

print(p(3))

