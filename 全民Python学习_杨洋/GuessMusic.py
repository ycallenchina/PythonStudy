import random
import winsound

guess=0
rand=random.randint(1,7)

if __name__ == '__main__':
	while guess!=rand:
		winsound.Beep(rand*1000,1000)#发生模块Beep(频率,时长单位毫秒)
		guess=int(input('猜猜是第几音阶:',))

		if guess<rand:
			print('小了')
		elif guess>rand:
			print('大了')
		print('猜对了')

