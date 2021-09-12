import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
# 初始化设置中文字体
sns.set_style('whitegrid', {'font.sans-serif':['simhei', 'Arial']})
plt.rcParams['axes.unicode_minus'] = False



def 气泡图(df,size1='数据值'):
	#图表长15，宽5，透明度0.7，隐藏图例，点的面积、轴标签调整为合适的大小
	g = sns.scatterplot(x=df.index, y=[0]*len(df), data=df, 
	                    size=size1, alpha=0.7, hue=df.index, legend=False, 
	                    sizes=( 200, 200 * df[size1].max()/df[size1].min() ))
	    
	g.figure.set_size_inches(15, 5) #图形大小设置
	g.figure.canvas.draw() #画图
	g.set_xticks(g.get_xticks())# 获取x轴数值
	g.set_yticks(g.get_yticks()) #获取y轴数值
	g.set_xticklabels(labels=g.get_xticklabels(), size='large')#x轴标签字体设置large 大号
	g.set_yticklabels(labels=g.get_yticklabels(), size='x-large');#y轴标签字体设置为x-large 加大号