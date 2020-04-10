

def 找遍所有文件里某类型文件的路径(path,x=3,s='.py'):
    '''   输入:#找遍path文件夹里所有尾部最后x=3位为s='.py'的文件
          输出:list类型所有文件路径的列表'''

    import os
    所找文件路径 = []
    #在walk的第二层里,排除venv文件夹
    for 二层 in os.walk(path):
        if 'venv' in 二层[0]:
            pass
        else:
            #在第二层的下一层第三个包里,找最后3个字符等于.py的.
            for 四层 in 二层[2]:
                if 四层[-(x):]==s :
                    所找文件路径.append(二层[0]+'/'+四层)
    return 所找文件路径


def 返回列表中文件里所有内容(目录, 头文件):
    '''输入:list,包含目录文件的路径,头文件为字符串,是包含目录的总文件名
       输出:目录下文件下所有内容逐行返回为list,并逐行标记出处(第几行的意思)'''

    所有内容 = []
    for 一层 in 目录:
        k = 1
        r = open(一层, 'r', encoding='utf-8')
        for 二层 in r.readlines():
            子文件名 = str(一层[len(头文件) + 1:])
            所有内容.append(f'{子文件名} ' + str(k) + '行  ' + 二层 + '\n')
            k += 1
    return 所有内容


def 内容搜索窗口(所有内容):
    '''逐行搜索,所有内容为list文本,所里面包含的信息'''
    from tkinter import Tk ,Entry,Text,Button

    def get(内容):
        # 文本清除:抬头位置'1.0'---1表示行,0表示列,end表示已有内容的后面
        t1.delete('1.0', 'end')
        # ent表示输入行内容,get是获得他的内容函数
        content=inputs.get()
        # 读取整理txt
        for i in 内容:
            if content in i:
                t1.insert('end',i)#t1表示文本框,end表示已有内容的后面

        return

    # 主控件fk
    fm=Tk()
    # 输入框
    inputs=Entry(fm)
    # 文本框
    t1=Text(fm,height=60,width=120)
    # 按钮1
    b1=Button(fm,text='搜索',command=lambda:get(所有内容))#用lanbda 传参,不然commad=get会传参出错

    # 需要显示的控件
    inputs.pack()
    b1.pack()
    t1.pack()
    # 主控fk死循环显示
    fm.mainloop()
