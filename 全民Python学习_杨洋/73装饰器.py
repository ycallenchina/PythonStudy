


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

# 装饰器使用说明---------------------------------------------
array=[2,4,124,6,73]

def deco_para(parameter):#传参到装饰器,外部参数.
    print('enter deco_para')

    def deco_func(func):
        print('enter deco_func')

        def wrapper(*args, **kwargs):#原方法的自身参数
            print('enter wrapper')
            print(parameter)
            print('---wrapper: before func---')
            a=func(*args, **kwargs)
            print('---wrapper: after func---')
            return a

        return wrapper

    return deco_func


@deco_para(123)
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    print('--start--')
    print(bubble_sort(array))