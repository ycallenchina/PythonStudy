
import easyquotation
import time
def time_out(late=100):#随机时间函数
	import time
	import random
	rand=random.randint(1,late)/100
	time.sleep(rand)
	# print('延时',rand,'秒...')
	return rand

for i in range(10):
	time_start = time.time()
	quotation = easyquotation.use('tencent') # 新浪 ['sina'] 腾讯 ['tencent', 'qq']
	tmp_dict = quotation.market_snapshot(prefix=True) # prefix 参数指定返回的行情字典中的股票代码 key 是否带 sz/sh 前缀
	time_end = time.time()
	time_use = time_end-time_start
	print(
	tmp_dict['sz000001']['name'],
	tmp_dict['sz000001']['now'],
	'Now:',time.strftime("%m-%d %H:%M:%S", time.localtime()) ,
	'Pass:',round(time_use,2),'秒')#查看实时股价

	print('------------------------------------------------')