#
# 1. dir() 函数
#  dir([object]) 会返回object所有有效的属性列表。示例如下：
#
# 2. vars() 函数
# vars([object]) 返回object对象的__dict__属性，其中object对象可以是模块，类，实例，或任何其他有__dict__属性的对象。所以，其与直接访问__dict__属性等价。示例如下（这里是反例，mser对象中没有__dict__属性）：
#
# 3. help() 函数
# help([object])调用内置帮助系统。输入
#
#
# 4. type() 函数
# type(object)返回对象object的类型。
#
# 5. hasattr() 函数
# hasattr(object, name)用来判断name（字符串类型）是否是object对象的属性，若是返回True，否则，返回False
#
# 6. callable() 函数
# callable(object)：若object对象是可调用的，则返回True，否则返回False。注意，即使返回True也可能调用失败，但返回False调用一定失败。

