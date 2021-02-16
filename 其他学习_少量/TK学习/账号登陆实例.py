 

from tkinter import *

root = Tk()
root.title('山丘')
root.geometry('300x160')
Label(root,text='账号：').place(x=30,y=30)
Label(root,text='密码：').place(x=30,y=70)

#保存一个字符串类型
v1 = StringVar()
v2 = StringVar()
#输入框
e1 = Entry(root,textvariable=v1)#textvariable为可变化文本变量.
e2 = Entry(root,textvariable=v2,show='*')   #用*号代替用户输入的内容
e1.place(x=80,y=30)
e2.place(x=80,y=70)
def show():
    print(f'账号：{v1.get()}')
    print('密码：%s' % v2.get())
    e1.delete(0,END)    #获取完信息，清楚掉输入框的
    e2.delete(0,END)    #0,END，表示从第0个到最后一个
Button(root,text='获取信息',width=10,command=show).place(x=20,y=120)
Button(root,text='退出',width=10,command=root.quit).place(x=180,y=120)
mainloop()


