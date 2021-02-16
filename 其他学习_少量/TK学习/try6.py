# 窗体控件学习
from tkinter import Tk ,Entry,Text,Button

def task1():
    t1.insert('end','come on come on')
    return

def save():
    f=open('e:\pyNote\调用资料/entry2.txt','a')
    f.write(t1.get(1.0,'end'))
    f.close()

fm=Tk()
fm.title('try')
fm.geometry('200x180')
a=Button(fm,text='try',width=15,height=1,command=task1).place(x=40,y=20)
b=Button(fm,text='try2',width=15,height=1,command=save).place(x=40,y=70)
c=Button(fm,text='try3',width=15,height=1,command=save).place(x=40,y=120)

fm.mainloop()
