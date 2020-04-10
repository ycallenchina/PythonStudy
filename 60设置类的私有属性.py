#实例:小马赛跑
import random
import time
class Game:
    #属性,可用默认值,例如:s=2
    def __init__(self,n,s=2):
        self.name=n
        self.speed=s
        self.__loc=0#设置私有变量loc,作用是外部引用访问不到,只能内部访问
        
    def run(self):
        self.__loc+=round(self.speed*random.random())#random的方法,返回0-1的随机浮点数
        print(f'{self.name}跑了{self.__loc}米')
    
    def get_loc(self):#可以访问私有属性的方法getter
        return self.__loc

    def set_loc(self,x):#可以设置私有属性的方法setter
        self.__loc=x
    #补充:还可以使用annotaion @标注 来访问和设置私有属性
    '''@property
        def x(self):
            return self.__loc
       @x.setter
        def x(self,c)
            self.__loc=c'''

ma_1=Game('红马',5)
ma_2=Game('黄马',3)

print('第一次用真名,查看ma1_loc=',ma_1._Game__loc)#实际的私有属性名
print('第二次用方法getter,查看ma1_loc=',ma_1.get_loc())
ma_1.set_loc(100)
print('使用setter设置后的ma1_loc=',ma_1.get_loc())

print('----------------------------------------')

#run测试
# while 1:
#     ma_1.run()
#     ma_2.run()

#     print('----------------------------------------')
#     time.sleep(1)#time的延迟方法,单位秒.
