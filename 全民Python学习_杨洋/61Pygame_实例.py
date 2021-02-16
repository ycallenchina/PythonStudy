import pygame
import random

def Pygame模块说明():
	pygame.init()#初始化pygame 加载此电脑声卡显卡等驱动
	#加载资料
	screen=pygame.display.set_mode((500,280))#设置游戏窗口大小
	back_img=pygame.image.load('E:/pyNote/调用资料/view.jpg')#加载背景图
	马1=pygame.image.load('E:/pyNote/调用资料/马1.png')#加载马图
	#图片填充,刷新
	screen.blit(back_img,(0,0))#填充背景图片入游戏窗口,补充:(x,y)从左上角算起越右x越大,越下y越大
	screen.blit(i.get_img(),i.get_loca())#填充马图片
	pygame.display.update()#刷新窗口
	#时间控制
	pygame.time.delay(100)#停顿100毫秒
	#原理是使用while循环,改变图片位置,不断填充,刷新图片,来实现动画效果.
	#若退出while循环执行以下命令
	for event in pygame.event.get():#退出命令
		if event.type == pygame.QUIT:
			pygame.quit()#退出pygame	


class hourse:
	def __init__(self,n,s,img,y):
		self.name=n
		self.speed=s
		self.__img=pygame.image.load(img)#加载马1图
		self.__y=y
		self.__x=0

	def run(self):
		self.__x=self.__x+round(self.speed*random.random())

	def get_img(self):
		return self.__img

	def get_loca(self):
		return (self.__x,self.__y)

pygame.init()#初始化pygame 加载此电脑声卡显卡等驱动

screen=pygame.display.set_mode((500,280))#设置游戏窗口大小
back_img=pygame.image.load('E:/pyNote/调用资料/view.jpg')#加载背景图

h_s=[
hourse('black',5,'E:/pyNote/调用资料/马.png',100),
hourse('red',10,'E:/pyNote/调用资料/马2.png',200)
]


while True:
	screen.blit(back_img,(0,0))#填充背景图片入游戏窗口
	for i in h_s:
		screen.blit(i.get_img(),i.get_loca())#填充马图片
		i.run()
	pygame.display.update()#刷新窗口
	pygame.time.delay(100)#停顿100毫秒
	
	for event in pygame.event.get():#退出命令
		if event.type == pygame.QUIT:
			pygame.quit()#退出pygame		


