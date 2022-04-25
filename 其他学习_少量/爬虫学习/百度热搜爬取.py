from urllib.request import urlopen
import chardet
from bs4 import BeautifulSoup

百度url='https://top.baidu.com/board?tab=realtime'
网易url='http://c.m.163.com/nc/article/headline/T1348647853363/0-10.html'

r=urlopen(百度url)#打开网址,返回HttpResponse对象

c=r.read()#读取,返回bytes
bs=BeautifulSoup(c,features='lxml')#把读取的bytes对象,使用beautifulsoip提取数值,参数features未知道功能

# 获取类名为.c... 的标签
b=bs.select('.c-single-text-ellipsis')[0].text

# 标签的text取出文本内容,contents也可以,不过是列表需要解包
# for index,i in enumerate(b):
# 	print(index+1,i.text)

# t=bs.find('table')#找到第一个table,返回的是标签对象


print(b)