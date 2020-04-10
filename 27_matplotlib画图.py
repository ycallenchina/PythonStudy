import matplotlib.pyplot as plt
#让maplotlib图形里可以显示中文
plt.rcParams['font.sans-serif']=['fangsong']
plt.rcParams['axes.unicode_minus']=False

姓名=['eff','allen','黄志成','1','2']
战斗力=[34.65,34.85,35,36.05,36.29]

size=[]
for i in 战斗力:
    size.append(i)

#纵横坐标上下限方法-
#plt.xlim(0,10)# plt.ylim(0,110)
#plt.axis([0,5,0,200])

# 网格，表格标题
plt.grid();plt.title('战力表')

#添加坐标轴名称
#plt.xlable
#plt.ylable('战斗力')

# 开始画图:scatter散点图，plot折线图，bar柱形图（width柱形宽），pie饼图
plt.scatter(姓名,战斗力,s=size,marker='*',c='r')#s 形状大小,marker 显示的形状样式,c 形状的颜色 可以用列表指明每个 的颜色

# ！！！savefig必须show前面执行，不然会空白
# plt.savefig('E:/pyNote/测试图3.png')#保存图片

#显示画图
plt.show()