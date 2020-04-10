from tkinter import Tk, Entry, Text, Button


def get(内容):
    # 文本清除:抬头位置'1.0'---1表示行,0表示列,end表示已有内容的后面
    t1.delete('1.0', 'end')
    # ent表示输入行内容,get是获得他的内容函数
    content = inputs.get()
    # 读取整理txt
    for i in 内容:
        if content in i:
            t1.insert('end', i)  # t1表示文本框,end表示已有内容的后面

    return


# 主控件fk
fm = Tk()
# 输入框
inputs = Entry(fm)
# 文本框
t1 = Text(fm,height=60,width=120)
# 按钮1
b1 = Button(fm, text='搜索', command=lambda: get(所有内容))  # 用lanbda 传参,不然commad=get会传参出错

# 需要显示的控件
inputs.pack()
b1.pack()
t1.pack()
# 主控fk死循环显示
fm.mainloop()

