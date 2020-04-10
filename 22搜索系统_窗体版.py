#窗体fk控件实践
import os
from tkinter import Tk ,Entry,Text,Button
def kai():
    os.system('start e:/pyNote/调用资料/整理.txt')
    return
def get():
    # 文本清除:抬头位置'1.0'---1表示行,0表示列,end表示已有内容的后面
    t1.delete('1.0', 'end')
    # ent表示输入行内容,get是获得他的内容函数
    content=inputs.get()
    # 读取整理txt
    f = open('e:\pyNote/调用资料/整理.txt', 'r', encoding='utf-8')
    for i in f.readlines():
        if content in i:
            t1.insert('end',i)#t1表示文本框,end表示已有内容的后面
    f.close()
    return
def getnew():
    # 本代码等同 17归类整理.py 因为import 引用不能用中文,固然起名
    import os
    # import re(备用正则表达式资料)
    # s=re.findall(r"\d+\.?\d*",str(mulu_py))

    # 得到后缀py的目录mulu_py
    mulu=os.listdir('e:\pyNote')
    mulu_py=[]
    for i in mulu:
        if '.py' in i:
            mulu_py.append(i)

    # 生成新记事本‘整理’txt记录
    w = open('e:\pyNote/调用资料/整理.txt', 'w', encoding='utf-8')
    # 依次打开目录提取内容,k计数行
    k=0#k是序列用
    for i in mulu_py:
        k=k+1
        # 先写入目录名,并打开此目录
        w.write(str(k)+'___'+i + '\n\n')
        f = open('e:\pyNote/' + i, 'r', encoding='utf-8')
        #提取lines内容,带有#的注释内容,并写入w
        for i in f.readlines():
            if '#' in i:
                k=k+1
                w.write(str(k)+'        '+i+'\n')
    print('更新成功')
    f.close()
    w.close()
# 主控件fk
fm=Tk()
# 输入框
inputs=Entry(fm)
# 文本框
t1=Text(fm)
# 按钮1
b1=Button(fm,text='搜索',command=get)
# 按钮2
b2=Button(fm,text='打开整理本',command=kai)
# 按钮3
b3=Button(fm,text='更新',command=getnew)

# 需要显示的控件
inputs.pack()
b1.pack()
b2.pack()
b3.pack()
t1.pack()
# 主控fk死循环显示
fm.mainloop()
