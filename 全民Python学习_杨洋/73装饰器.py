
#---------------------------- 原始函数名更新装饰器用法

def senior_q(f):#高级的senior
	def new(r):
		print("高阶函数,已装饰")
		return f(r)
	return new

def for_girth(r):#求周长girth
	return 3.14*r*2

for_girth=senior_q(for_girth)

print(for_girth(3))



#-------------------------------装饰器@wraps的用法
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

#-----------------------从装饰器传参到被装饰函数
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

# ----------------# 使用 *args,**kwargs解决，当被装饰的函数的参数变化时，装饰器的参数也得变化的问题
import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)    # 运行的为test函数
        stop_time = time.time()
        print("程序运行的时间%s"%(start_time-stop_time))
        print(*args,**kwargs)
    return wrapper

@timmer
def test(name,age):
    time.sleep(3)
    print("test函数执行完毕")
test("henry",18)

@timmer
def test2(name,age,addr):
    time.sleep(3)
    print("test2函数执行完毕")
test2("heihei","16","China")    # 程序不在报错

# 输出
# test函数执行完毕
# 程序运行的时间-3.000153064727783
# henry 18
# test2函数执行完毕
# 程序运行的时间-3.0007944107055664
# heihei 16 China

## 浅浅了解*args与**kwargs

# *args：将多个实参放入一个元组中，可以传多个参数

# **kwargs：按照关键字传值，将多余的值以字典的形式传递