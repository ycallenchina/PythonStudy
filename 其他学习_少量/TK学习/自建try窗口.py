# 窗体控件学习
# import pandas as pd
# import numpy as np
from tkinter import Tk ,Entry,Text,Button
from functools import partial
import sys
sys.path.append("..")#为了import引用上一级包
from Tools.模拟运行Shell import *

open_try()
fm=Tk()
fm.title('try')
fm.geometry('200x180')

open1=partial(open_try,k=1)
open2=partial(open_try,k=2)#传参方法1
a=Button(fm,text='try',width=15,height=1,command=open1).place(x=40,y=20)
b=Button(fm,text='try2',width=15,height=1,command=open2).place(x=40,y=70)
c=Button(fm,text='try3',width=15,height=1,command=lambda:open_try(3)).place(x=40,y=120)#传参方法2

fm.mainloop()
