import time
def time_out(late=100):#随机时间函数
	import time
	import random
	rand=random.randint(1,late)/100
	time.sleep(rand)
	print('延时',rand,'秒...')
	return rand
t1=time.strftime("%m-%d %H:%M:%S", time.localtime()) 
t2=time.strftime("%m-%d %H:%M:%S", time.localtime()) 



ticks1 = time.time()
time_out(100)
ticks2 = time.time()
ticks3=ticks2-ticks1
print(round(ticks3,2))