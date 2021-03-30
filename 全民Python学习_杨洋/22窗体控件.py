# 窗体控件学习
from tkinter import Tk ,Entry,Text,Button

def task1():
    t1.insert('end','come on come on')
    return

def save():
    f=open('e:/pyNote/调用资料/entry2.txt','a')
    f.write(t1.get(1.0,'end'))
    f.close()

fm=Tk()
# 单行文本
# ent=Entry(fm)
# ent.pack()
# 文本框
t1=Text(fm)
# 按钮
b1=Button(fm,text='task1',command=task1)
b2=Button(fm,text='save',command=save)
# 显示,及循序
b1.pack()
t1.pack()
b2.pack()
fm.mainloop()
