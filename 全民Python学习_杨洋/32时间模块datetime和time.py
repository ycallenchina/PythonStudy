from datetime import datetime


def 设置datetime时间():
	d1 = datetime(2005, 2, 16,10,59)

def 现在时间():
	t=datetime.now()
	return t

def 设置时间格式():#格式化datetime类,并转换为str
	d1 = datetime(2005, 2, 16,10,59)
	d2=d1.strftime('%Y/%m/%d %H/%M/%S')#格式化datetime类,并转换为str

def 字符串转化为datetime类(s):	
	d='20210201093502'
	
	t1=datetime.strptime(s,'%Y%m%d%H%M%S000')
	return t1

def datetime类转换为字符串():
	d1 = datetime(2005, 2, 16,10,59)
	d=str(d1)

def 计算时间差():
	from dateutil.relativedelta import relativedelta#专用于计算时间差的模块

	#加上特定时间
	d1 = datetime(2005, 2, 16,10,59)
	a=relativedelta(months=50)#专用于计算时间差,years,months,days,hours,mintues,seconds.
	x=d1+a
	print(x,'x的类型是:',type(x))
	#算时间差
	delta=x-d1
	print(delta,'delta的类型是:',type(delta))


if __name__ == '__main__':
	d='20210201145510000'
	#设置当天下午3点时间
	t=字符串转化为datetime类(d)
	t_today=datetime(t.year,t.month,t.day,15)
	x=t_today-t
	print(t_today)
	print(t)
	print(x.seconds)
	print(x.seconds<300)