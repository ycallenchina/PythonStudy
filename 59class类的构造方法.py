
#class 构造方法,初始化方法
#__init__的使用

#实例:小马赛跑
import random
import time
class Game:
    #属性,可用默认值,例如:s=2
    def __init__(self,n,s=2):#构造方法,对象创建时,会自动调用运行一次.
        staff='我是内部工作人员'#局部变量
        self.name=n#对象的属性 name
        self.speed=s
        self.loc=0
        
    def run(self):
        self.loc+=round(self.speed*random.random())#random的方法,返回0-1的随机浮点数
        print(f'{self.name}跑了{self.loc}米')
        
ma_1=Game('红马',5)
ma_2=Game('黄马',3)
ma_3=Game('青马',6)

while 1:
    ma_1.run()
    ma_2.run()
    ma_3.run()
    print('----------------------------------------')
    time.sleep(1)#time的延迟方法,单位秒.
