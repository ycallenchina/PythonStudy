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