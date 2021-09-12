import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
# 初始化设置中文字体
sns.set_style('whitegrid', {'font.sans-serif':['simhei', 'Arial']})

def 柱形图(df,x1,y1):
	g=sns.barplot(x=x1,y=y1,data=df,palette='spring',alpha=0.6,ci=None)
	g.figure.canvas.draw()
	g.set_xticks(g.get_xticks())
	g.set_yticks(g.get_yticks())
	g.set_xticklabels(labels=g.get_xticklabels(), size='x-large',rotation=30,horizontalalignment='right')
	g.set_yticklabels(labels=g.get_yticklabels(), rotation=90, size='x-large')
	plt.show()



if __name__ == '__main__':
	sh=pd.read_csv(r'C:/Users/YcAllenEffy/Desktop/国际卖场数据2011-2015.csv')
	df=sh.head(10)
	柱形图(df,'商品子类','总额')
