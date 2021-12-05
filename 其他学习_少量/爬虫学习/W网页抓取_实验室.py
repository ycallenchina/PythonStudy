

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import json
import pandas as pd

def time_out(late=100):#随机时间函数100等于1秒
	import time
	import random
	rand=random.randint(1,late)/100
	time.sleep(rand)
	print('延时',rand,'秒...')
	return rand

def res_url(url):#常规GET请求


	r=urlopen(url)#打开网址,返回HttpResponse对象
	time_out(200)#延时2秒
	r=r.read()#读取HttpResponse里内容
	bs=BeautifulSoup(r,features='lxml')
	r=bs
	# c=c.decode(encoding='utf-8')
	return r

def get_info(bs):#常规bs解析网页信息
	# content=bs.find(id='article')#原方法
	content=bs.find(attrs = {'class':'article-content'})#防止与关键字同名,使用attrs字典传参数
	tx_cont=content.text#提取文本内容
	content=tx_cont
	return content

if __name__ == '__main__':
	url_财经='https://www.caijing.com.cn/'#财经网首页
	url_财经1='http://stock.caijing.com.cn/20210224/4740885.shtml'
	url=url_财经1
	a=res_url(url)
	r=get_info(a)
	print(r)