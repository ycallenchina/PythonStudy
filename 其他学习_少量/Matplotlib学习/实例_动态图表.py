

# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib

# print matplotlib.matplotlib_fname()
 
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))#设置坐标
line, = ax.plot([], [], lw=2)
def 读取csv文件(路径):
	#encoding为编译方式
	df=pd.read_csv(路径,encoding='utf_8_sig',index_col=False)
	return df

def init():
    line.set_data([], [])
    return line,
 

def animate(i):
	# print(x)
    #linespace(起始值(start),终止值(stop),数量(num)=50,
    #是否包含终止值(endpoint)=True,是否返回步长(retstep)=False,数据类型(dtype)=None)
	x1=x[:i]
	y1 = np.sin(2 * np.pi * (x1 - 0.01 * 0.2))
	# print(x1)
	# print(y1)
	line.set_data(x1, y1)
	return line,




x = np.linspace(0, 2, 100)


#FuncAnimation 参数: frames动画长度 interval 更新频率ms计算 blit选择更新所有点True,只更新变化点Flase
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=200, interval=20, blit=True)
# anim.save('sin.gif', fps=75, writer='imagemagick')
plt.show()

