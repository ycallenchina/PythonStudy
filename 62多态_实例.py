import pygame
import random
#多态对象,只要有相同方法,就可以一起引用.
'''例如:下面hourse和fans类,虽然类不同,但是 get_lmg(),和get_loca(),run(),方法一样.
就可以同时归为h_s列表.被for循环引用'''

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

class fans:
	def __init__(self,img,y,x,begin=True):
		self.__img=pygame.image.load(img)#加载马1图
		self.__y=y
		self.__x=x
		self.__begin=begin

	def run(self):
		if self.__begin==True:
			self.__y+=30
		if self.__begin==False:	
			self.__y+=(-30)
		self.__begin=not self.__begin

	def get_img(self):
		return self.__img

	def get_loca(self):
		return (self.__x,self.__y)



pygame.init()#初始化pygame 加载此电脑声卡显卡等驱动

screen=pygame.display.set_mode((500,280))#设置游戏窗口大小
back_img=pygame.image.load('E:/pyNote/调用资料/view.jpg')#加载背景图
h_s=[
hourse('black',5,'E:/pyNote/调用资料/马.png',100),
hourse('red',10,'E:/pyNote/调用资料/马2.png',200),
fans('E:/pyNote/调用资料/啦啦队.png',220,200,False),#多态对象,相同方法,就可以一起引用.
fans('E:/pyNote/调用资料/啦啦队.png',220,100),
fans('E:/pyNote/调用资料/啦啦队.png',220,300)
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


