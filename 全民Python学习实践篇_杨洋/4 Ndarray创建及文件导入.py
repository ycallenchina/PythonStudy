#!/usr/bin/env python
# coding: utf-8

# ## 创建ndarray

# In[35]:


import numpy as np
import pandas as pd
x=[1,2,3,'abc','qqq']
x_nd=np.array(x)#创建ndarray方法
x_nd


# ## 笔记---创建ndarray注意
# ####    结构会强制统一.
# #### 	向上兼容法则
#     向上兼容法制:在容器转换为ndarray时,
#     如果遇到容器内容里类型不统一的情况下
#     ndarray会强制统一容器里的内容.
#     并使用向上兼容法制:整数-浮点数-字符串.
#     法则为:有字符串就全都字符串,没有就全浮点,再没有就整数.
# ####    dtype='U11' 
#     表示用的时unico 11长度类型

# ## 创建多维数组

# In[6]:


x=[[3,5,7],[2,5,6]]
x_nd=np.array(x)
x


# #### 对于长度不一致者,不推荐进行ndarray转换操作

# In[8]:


x2=[[3,5,],[2,5,6]]
x2_nd=np.array(x)
x2_nd


# ## 函数生成数组
# #### numpy.zeros 生成内容都为0的数组
# #### numpy.ones
# #### numpy.eye
# #### numpy.arange
#     zeros((n,m),dtype='int'):其中n表示行数,m表示列数,dtype表示指定数据类型
#     zeros((1,2,3...n),dtype='int') :其中用zeros生成n为数组.

# In[9]:


a=np.zeros((3,4),dtype='int')
a


# In[10]:


a=np.ones((3,4))
a


# ####  eye的参数只能是纯数字

# In[12]:


a=np.eye(4)
a


# #### arange参数:起始值,末值,步长(步长可用任意实数) 

# In[16]:


a=np.arange(-5,10,0.2)
a


# # 函数生成随机数组 

# ###  np.random.rand(n,m)   生成0-1之间的随机浮点数.n表示二维行数,m表示二维的列数.同理可以生成n维数组

# In[19]:


a=np.random.rand(3,5,2)
a


# ###  np.random.randint(n,m,(a,b)) 生成n到m之间,a行b列的整数 数组,同理可以生成n维数组

# In[20]:


a=np.random.randint(3,5,(2,4))
a


# ### np.random.choice(容器,(a,b)) 生成容器里的随机内容 a行b列的数组,同理可以生成n维数组  

# In[21]:


a=np.random.choice(['effy','yc','hzc'],(2,4))
a


# ####  randn():生成正太分布的随机数组
# #### uniform():生成均匀分布的随机数组
# #### 原理 unmpy.random.uniform(low,high,size)
# 参数介绍
# low: 采样下界，float类型，默认值为0；
# high: 采样上界，float类型，默认值为1；
# size: 输出样本数目，为int或元组(tuple)类型。

# In[34]:


a=np.random.randn(2,10)#生成2行10列的正态分布随机数组
a


# In[52]:


a=np.random.uniform(1,100,100)#10个均匀的1-10数组
a


# ### 转化为dataframe 后用图标画出随机数组.

# In[53]:


df = pd.DataFrame(a)
df


# In[54]:


import matplotlib.pyplot as plt
plt.figure(1)
plt.scatter(df.index,df[0])
plt.show()


# # 导入文件_ndarray 

# ###  np.loadtxt('导入路径',delimiter=',')分隔符号为,号.也可以指定数据类型,dtype='int'

# ### np.genfromtxt用法与loadtxt类似,增多了filling_values参数,可以filling_values=0指定空置内容等于0.
