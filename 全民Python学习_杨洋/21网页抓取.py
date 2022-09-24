from urllib.request import urlopen
import chardet
from bs4 import BeautifulSoup

r=urlopen('https://www.boc.cn/sourcedb/whpj/')#打开网址,返回HttpResponse对象


c=r.read()#读取,返回bytes


bs=BeautifulSoup(c,features='lxml')#把读取的bytes对象,使用beautifulsoip提取数值,参数features未知道功能
# print(bs)
t=bs.find('table')#找到第一个table,返回的是标签对象
t_all=bs.find_all('table')#找到所有table

t_2=t_all[1]#提取第二个table标签内容

all_tr=t_2.find_all('tr')#找所有tr的标签内容

all_tr.pop(0)#删除第一个tr内容

for i in all_tr:
	all_td=i.find_all('td')#找到td的标签内容
	print(all_td)
	print(all_td[0].text,all_td[4].text)#只要标签内的内容 



# 获取百度热搜案例----------------------------------------------------------------------------
def get_www_info():
	百度url='https://top.baidu.com/board?tab=realtime'
	网易url='http://c.m.163.com/nc/article/headline/T1348647853363/0-10.html'

	r=urlopen(百度url)#打开网址,返回HttpResponse对象
	c=r.read()#读取,返回bytes
	bs=BeautifulSoup(c,features='lxml')#把读取的bytes对象,使用beautifulsoip提取数值,参数features未知道功能

	# 获取热搜盒子
	b_info=[]
	box=bs.find_all(class_='category-wrap_iQLoo')
 	# 遍历盒子
	for i in box:
		# 获取盒子里的标题
		box_tile=i.select('.c-single-text-ellipsis')[0].text
		# 获取盒子里的热度
		box_hot=i.select('.hot-index_1Bl1a')[0].text
		# 获取盒子里的图片 其中 recursive=False 参数表示只取元素里的子级元素,子孙等不取.
		box_src=i.find_all(class_='img-wrapper_29V76')[0].find_all('img',recursive=False)[0]['src']
		b_info.append([box_tile,box_hot,box_src])

	# print(b_info)
	return b_info[:10]


if __name__ == '__main__':
	pass
	# get_www_info()