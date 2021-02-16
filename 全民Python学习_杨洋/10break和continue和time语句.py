import time
import random
# 随机数的用法
guess=random.randint(1,10)
def sleep():
    print('1')
    time.sleep(1)
    return
#break: 跳出整个当前循环
# 多用于情况的终止用途
while True:
    me = int(input('猜猜是多少:'))
    if me>guess:
        sleep()
        print('smaller')
    elif me<guess:
        sleep()
        print('bigger')
    else:
        sleep()
        print('bingo')
        break
print('----------------------------------------------------------------------.1')
# continue:跳出本次当前循环
# 多用于整体里面的特殊情况，例如：搜检字符里面对i‘m的’不做处理
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print ('当前字母 :', letter)