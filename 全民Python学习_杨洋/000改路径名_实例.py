 import os
import sys
print('\n监控本文件名----------------------------------------------------------------------.1\n')
print(__file__)
# 获取本文件名方法

print(os.path.realpath(__file__))#绝对路径
print('\n创建新路径----------------------------------------------------------------------.2\n')
# 创建的新文件名
新名='新路径.txt'
旧路径=os.path.realpath(__file__)

# 切掉本文件名加上新文件名
# os.path.basename()： 返回路径最后的文件名
新路径=旧路径[:-len(os.path.basename(__file__))]+新名
print(新路径)

print('\n创建新路径----------------------------------------------------------------------.3\n')

# import os, sys
# print("this is :",os.getcwd())  # 获取当前文件的位置
# print("this is :", __file__)  # 当前文件的路径
# print("this is :", os.path.basename(__file__))  # 返回路径最后的文件名
# print("this is :", sys._getframe().f_lineno)  # 当前代码的行数


#该路径名方法2
print(f'  {sys._getframe().f_lineno}  行结果:',)
print(__file__)
# 获取本文件名方法
print(f'  {sys._getframe().f_lineno}  行结果:',)
print(os.path.basename(__file__))
# 创建的新文件名
cre='qqqq.py'
old=__file__
# 切掉本文件名加上新文件名
new=old[:-len(os.path.basename(__file__))]+cre
print(f'  {sys._getframe().f_lineno}  行结果:',)
print(new)
# f=open(new,'w')