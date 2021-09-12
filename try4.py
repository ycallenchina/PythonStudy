def 距ending时间(s):#默认为0时差
     from datetime import datetime
     t=datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
     t_today=datetime(t.year,t.month,t.day,15)
     delta=t_today-t
     # print('距离ending时间:',delta.seconds,'秒')#距离盘末时间提示
     return delta.seconds/60


print(距ending时间('2017-01-03 14:35:00'))