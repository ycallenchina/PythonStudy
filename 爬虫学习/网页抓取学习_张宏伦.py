
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import chardet
import urllib
import json
import pandas as pd
#GET
def get_url(url):#常规GET请求

	# url='http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'

	r=urlopen(url)#打开网址,返回HttpResponse对象
	# r=r.read()#读取HttpResponse里内容
	# bs=BeautifulSoup(c,features='lxml')  #features为网页解析器,可选项
	# c=c.decode(encoding='utf-8')
	return r

def post_url():#POST请求

	import urllib.parse
	import urllib.request
	data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')#post的数据
	response = urllib.request.urlopen('http://httpbin.org/post',data=data)#请求有post的
	print(response.read())

	url='http://shuju.wdzj.com/depth-data.html'
	data=bytes(urllib.parse.urlencode({'type1':1,'type2':2,'status':0,'wdzjPlatId':59}),encoding='utf8')
	response = urllib.request.urlopen(url,data=data)
	result=response.read()
	c=result.decode(encoding='utf-8')

	print(c)

def Simulant_Requests(url):#模拟浏览器的GET请求
	import requests
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
	r = requests.get(url,headers=headers)
	html=r
	html = r.text#返回字符串
	# print(html)
	return html

def get_info(url):#专用___单部电影详情页解析
	#获取info里的纯文本
	res=Simulant_Requests(url)
	bs=BeautifulSoup(res,features='lxml')#把读取的bytes对象,使用beautifulsoip提取数值,参数features未知道功能

	content=bs.find(id='info')#查找id='info'的html内容
	tx_cont=content.text#提取文本内容
	L=tx_cont.splitlines()#提取每行,存入列表

	dic={}
	for i in L:
		i=i.split(':')
		if i[0]=='':
			pass
		else:
			dic[i[0]]=i[1]
	return dic

def create_df():
	df = pd.DataFrame(columns=['电影名', '评分', 'url', '导演','类型','国家','上映日期'])
	return df


def take_record(sub):#解析字典,选取内容生成新字典
	#把字典整理归类
	dic={}
	a=sub
	dic['电影名']=a['title']
	dic['评分']=a['rate']
	dic['url']=a['url']

	b=get_info(a['url'])#取出详情页
	if '导演' in b:
		dic['导演']=b['导演']
	if '类型'in b:
		dic['类型']=b['类型']
	if '制片国家/地区' in b:
		dic['国家']=b['制片国家/地区']
	if '上映日期' in b:
		dic['上映日期']=b['上映日期']
	return dic

def time_out(late=100):#随机时间函数
	import time
	import random
	rand=random.randint(1,late)/100
	time.sleep(rand)
	return rand

def main(url):
	#主程序
	''' 首席分析结构
			请求的html结构为:
			{'subjects':[{电影字典1},{电影字典2}...]}
		1,请求豆瓣电影,每次记录10行,自动增加50开始位置数:	
			用range做第一层循环(防死循环),从0-1000每次增加200共5次[0,200...800]
			每次请求电影主网页,获得10条电影内容(delay随机2秒),实际是从0,200...800这几个位置开始抽取10个样本
		2,每条电影内容再请求这部电影的详情页(delay随机3秒),Max请求50条,Max delay3*50+2*5=160秒
		3,用df储存,返回df
		4,用try 保护请求的异常错误,返回空的df.
	'''
	pd.set_option('display.max_columns', None)#显示所有df列
	df=create_df()
	roll=1#
	for i in range(0,1000,200):
		start=i#规定循环数,防止无限循环
		try:#尝试请求.
			a=Simulant_Requests(url+str(start))
			a=json.loads(a)#解析html内容为字典
			rand=time_out(200)#延迟
			print('总内容链接第',roll,'循环_','请求成功,延迟为:',rand)
			roll+=1
		except Exception as e:
			print('Requests请求异常错误:\n',e,'\nLine at:',e.__traceback__.tb_lineno)
			print('请求返回为:\n',a)
			return df
		a=a['subjects']#取出存电影的list
		if a!=[]:#如果a为[]代表没有了
			k=1#计数器
			for sub in a:#逐个取出电影的字典
				record=take_record(sub)#解析字典,选取字段存入
				df=df.append(record,ignore_index=True)#添加一条记录入df
				rand=time_out(300)#延迟
				print('添加记录成功',k,'条','请求延迟:',rand)
				k+=1#计数器自增
		else:
			break

	print(df)
	return df

def csv保存(df):
	保存路径='C:/Users/YcAllenEffy/Desktop/网页抓取.csv'
	df.to_csv(保存路径,encoding='utf_8_sig',index=False)#不要索引

def url_x(tages,page_limit,page_start):
	'''
	网址结构 tages 为大分类:如,热门,日本,韩国,豆瓣高分等.
			page_limit 为每次所显示的电影数量.
			page_start 为电影的索引号开始点.
			总结:在tages大类里 从start索引号开始展示limit个电影数量
	'''
	page_limit=str(page_limit)
	page_start=str(page_start)
	url_x=f'https://movie.douban.com/j/search_subjects?type=movie&tag={tages}&page_limit={page_limit}&page_start={page_start}'
	return url_x

if __name__ == '__main__':
	url_sina='http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'#新浪高考资料
	url1='https://movie.douban.com/j/search_tags?type=movie&source=index'#豆瓣电影标签
	url2='https://movie.douban.com/j/search_tags?type=tv&source=index'#豆瓣tv标签
	url3='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'#豆瓣tv内容详情
	#不完整url4,缺start参数
	url4='https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%86%B7%E9%97%A8%E4%BD%B3%E7%89%87&page_limit=10&page_start='#豆瓣电影内容详情
	url5='https://movie.douban.com//subject//34960094//'#单部电影详情页


	tages='日本'
	page_limit=str(10)
	page_start=str(0)
	
	# url=url_x(tages,page_limit,page_start)	
	url=url1
	a=Simulant_Requests(url)
	print(a)
