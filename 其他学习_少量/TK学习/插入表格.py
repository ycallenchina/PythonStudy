from tkinter import *
from tkinter import ttk

root =Tk()#创建窗体
root.geometry('200x600')
root.title('变量监视')#设置标题

dic=['allen','yc','qqqq']
dic2=[1,2,3]

# lable = Label(root, text="变量监控", font=("Fixedsys", 12), width=8, height=1)
# lable.place(x=0,y=0)

#表格
tree = ttk.Treeview(root,columns=['1','2','3'],show='headings',height=30)#设置表
tree.place(x=0,y=30)
# 设置表头大小
tree.column('1',width=50)
tree.column('2',width=50,anchor='center')
tree.column('3',width=50,anchor='center')
#设置表名
tree.heading('3',text='i变量')

#插入数值
tree.insert('','end',values=dic)
tree.insert('','end',values=dic2)
root.mainloop()#显示窗体