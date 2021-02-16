
from tkinter import *
from tkinter import ttk

root =Tk()#创建窗体
root.geometry('200x600')
root.title('变量监视')#设置标题


lable = Label(root, text="变量监控", font=("Fixedsys", 12), width=8, height=1)
lable.place(x=0,y=0)

#表格
tree = ttk.Treeview(root,columns=['1','2','3'],show='headings',height=30)#设置表
tree.place(x=0,y=30)
# 设置表头大小
tree.column('1',width=50)
tree.column('2',width=50,anchor='center')
tree.column('3',width=50,anchor='center')
#设置表名
tree.heading('1',text='i')
def end():
	global root
	root.mainloop()
#插入数值
def go(i,root=root):
	tree.insert('','end',values=i)
	print('ok')
	# root.mainloop()
	# a=Button(root,text='try',width=15,height=1,command=go).place(x=40,y=20)
if __name__ == '__main__':
	# go('i love you')
	end()
	# root.after(2000,end)
	# root.mainloop()
	# root.mainloop()