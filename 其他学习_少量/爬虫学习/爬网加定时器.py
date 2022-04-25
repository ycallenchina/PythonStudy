
import json
import datetime

t1=datetime.datetime.now()

 # 获取百度热搜,返回txt列表
def catch_www():
	from urllib.request import urlopen
	from bs4 import BeautifulSoup 

	百度url='https://top.baidu.com/board?tab=realtime'

	r=urlopen(百度url)#打开网址,返回HttpResponse对象
	c=r.read()#读取,返回bytes
	bs=BeautifulSoup(c,features='lxml')#把读取的bytes对象,使用beautifulsoip提取数值,参数features未知道功能
	b=bs.select('.c-single-text-ellipsis')
	txt=[i.text.strip() for i in b]

	# print(txt)
	return txt

# 从data取出时间算出时间差,单位秒
with open('data.json','r') as f:
	dic=eval(f.read())
	time=dic['save_time']

	now=datetime.datetime.now()
	second=(now-datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")).total_seconds()
	print('文件保存时差为:',round(second,0),'秒')

# 如果时差second 大于600秒就从新保存现在时间
if second>6                                                                                                                       :#大于10分钟就执行
	with open('data.json','w') as f:
		new_time=datetime.datetime.now()
		top10=catch_www()

		save_dic=dict(save_time=str(new_time),save_top10=top10)
		f.write(json.dumps(save_dic))
		print('ok save')
		print('新的top10是:',top10)
else:
	with open('data.json','r') as f:
		dic=eval(f.read())
		top10=dic['save_top10']
		print('现在的top10是:',top10)

t2=datetime.datetime.now()
print('程序耗时:',t2-t1)