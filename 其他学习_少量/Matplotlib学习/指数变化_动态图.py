import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
#可现实中文的设置
plt.rcParams['font.sans-serif']=['fangsong']
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel(r'E:\pyNote\调用资料/62classNew.xlsx', 'Sheet1')  # 读取excel,指数2017-2018数据
# print(df.info())#展示读取信息
# print(df.head(2))#头两条
df=df.iloc[:,1:4]#获取1,2,3列所有行数据

#封装
def bar_chart_race(year):
    df_sort = df[df.trade_date == year].sort_values('close')  # 按close列的倒叙排
    ax.clear()#清楚ax表内容
    #重新画图,给code上色
    ax.barh(df_sort['ts_code'],df_sort['close'])#装载数据
    plt.title(f'{year}')#给标题为日期
    plt.box(False)#不明代码

fig,ax=plt.subplots(figsize=(10,18))#画图

date_list=list(set(df.trade_date))#去重复获取日期参数
date_list.sort()#给日期从前往后排序

animator=animation.FuncAnimation(fig,bar_chart_race,frames=date_list)#fig图,bar主参,frames是日期变化参数.
HTML(animator.to_jshtml())#不明代码


plt.show()