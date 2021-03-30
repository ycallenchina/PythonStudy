import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML

df = pd.read_excel(r'E:/pyNote/调用资料/51classNew.xlsx', 'Sheet1')  # 读取excel表格
# print(df.info())#展示读取信息
# print(df.head(2))#头两条
df=df.iloc[:,1:5]

# print(df[df.group=='上证'])#group列中等于 上证的数据
df_sort=df[df.trade_date==20180813].sort_values('open',ascending=False)#按open列的倒叙排
fig,ax=plt.subplots(figsize=(15,8))#生成15宽*8长大小的图fig为图,ax为参数集
ax.barh(df_sort['ts_code'],df_sort['open'])#ts_code为纵坐标,open为横坐标画图

#编色
group_list=list(set(df.group))#去重复生成group的无重复列表
color_list=['#343837','#12e193','#fe7b7c','#fd411e']
group_color=dict(zip(group_list,color_list))#给group组字典对应颜色 组名:颜色
#上色
code_group=df.set_index('ts_code')['group'].to_dict()#用code做建,group做值生成字典 股名:组名

#封装
def bar_chart_race(year):
    df_sort = df[df.trade_date == year].sort_values('open', ascending=False)  # 按open列的倒叙排
    ax.clear()#清楚ax表内容
    #重新画图,给code上色
    ax.barh(df_sort['ts_code'],df_sort['open'],color=[group_color[code_group[i]] for i in df_sort['ts_code']])#装载数据
    plt.title(f'{year}')#给标题为日期
    plt.box(False)#不明代码

fig,ax=plt.subplots(figsize=(15,8))
animator=animation.FuncAnimation(fig,bar_chart_race,frames=[20180810,20180813,20180814,20180815,20180816])
HTML(animator.to_jshtml())#不明代码


plt.show()