
import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie,Bar,Timeline
from pyecharts.globals import ThemeType

# ----------数据--------------------
sh=pd.read_csv(r'C:/Users/YcAllenEffy/Desktop/行业每日热点.csv',header=1, index_col=0)


#数据处理----- 删除空值,给时间索引 排序
sh=sh.dropna()
sh.index=pd.to_datetime(sh.index)
sh=sh.sort_index()

# ------------画图-------------------
df=sh.copy()
#原理:用timeline做bar的动画
# bar设置一行数据为二维数据,timeline.add控制行号来实现三维数据

#设置画布大小,主题等
timeline=Timeline(init_opts=opts.InitOpts(width='2000px',height='800px',page_title='123',theme=ThemeType.CHALK))
timeline.add_schema(play_interval=1500)#播放时间间隔

for index in df.index:#循环每个时间点位,
    
    bar=Bar()
    
    #x,y轴数值载入
    bar.add_xaxis(df.columns.values.tolist())
    bar.add_yaxis(str(index),df.loc[index].values.tolist())
    #timeline设置第三维数据
    timeline.add(bar,f'{index}号...')
    
    #样式设置
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title=str(index)),#标题设置
        yaxis_opts=opts.AxisOpts(max_=15),#设置y轴最大值,以免y轴的值游动.
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(
                is_show=True,#展示轴线
                rotate=45, #轴坐标 名旋转角度
                font_size=12,#字体大小
                margin=10,#刻度标签与轴线之间的距离。
                interval=0#隔开几个显示坐标轴名称
            )))
    

    
# bar.load_javascript()#渲染

timeline.render()
# timeline.render()