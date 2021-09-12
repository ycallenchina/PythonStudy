#!/use/bin/python
#-*-coding:utf-8-*-

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import threading,time
import urllib.request as urlreq
import time 
#外观状态的改变
def disab_lfm1():
    entr1_1["state"]="disable"
    entr1_2["state"]="disable"
 
def enab_lfm1():
    entr1_1["state"]="normal"
    entr1_2["state"]="normal"
    checkbox1_3["state"] = "normal"
 
def enab_lfm2():
    entr2_1["state"] ="normal"
    entr2_2["state"] ="normal"
    entr2_3["state"] ="normal"
    entr2_4["state"] ="normal"
    entr2_5["state"] ="normal"
    entr2_6["state"] ="normal"
 
def disab_lfm2():
    entr2_1["state"] ="disable"
    entr2_2["state"] ="disable"
    entr2_3["state"] ="disable"
    entr2_4["state"] ="disable"
    entr2_5["state"] ="disable"
    entr2_6["state"] ="disable"
 
def change_stat():
    if checkbox_val.get():
        enab_lfm2()
    else:
        disab_lfm2()
#发送SMTP邮件
def send_mail():
    import smtplib
    from email.mime.text import MIMEText
    msg_from = entr2_6.get() #发件人
    passwd = entr2_3.get() #密码
    msg_to = entr2_5.get() #收件人
    subject = entr2_4.get()
    content = entr1_1.get()+entr2_4.get()+"\n告警！告警！！告警！！！"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        sendM = smtplib.SMTP(entr2_1.get(), 25)
        sendM.login(msg_from, passwd)
        sendM.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
    finally:
        sendM.quit()
 
#从停止中点击开始运行后的状态改变
def start_moniter():
    global monit_state,td
    # txinfo3_1.delete(0.0,END)
    monit_state=True
    btn1_r["state"]="disable"
    btn1_r['text'] = "运行中"
    btn2_r["text"] = "停止"
    btn2_r["state"]="normal"
    checkbox1_3["state"] = "disable"
    # disab_lfm2()
    disab_lfm1()
    unm = 0
    while monit_state:
        unm += 1
        web_moniter() #无限循环的监控
        time.sleep(int(entr1_2.get()))
 
#创建新的线程
def new_thread():
    global td
    td = threading.Thread(target=start_moniter)
    td.setDaemon(True)
    td.start()
 
#线程中要运行的无限循环
def web_moniter():
    urladd =entr1_1.get()
    timeot=int(entr1_2.get())
    try:
        # txinfo3_1.delete(1.0, END)
        web_f = urlreq.urlopen(url=urladd, timeout=timeot)
        print(web_f.getcode())
        if web_f.getcode() == 200:
            succ_info = "%s正常\n" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print("%s" % (succ_info))
            # succ_info ='happy\n'
            txinfo3_1.insert(1.0, succ_info)
            txinfo3_1.see(END)
    except:
        fail_info = "%s不正常\n---------婷婷最美了----------\n" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("%s" % (fail_info))
        txinfo3_1.insert(1.0, fail_info)
        if checkbox_val.get():
            send_mail()


def 回测_thread2():
    global td

    td = threading.Thread(target=happy2)
    td.setDaemon(True)
    td.start()

def happy2():
    global td
    import 获取股票数据
    import 均线计算
    import 新兴股票策略


    df=获取股票数据.获取个股df(标的=entr1_1.get(),start=entr1_2.get(), end=entr1_3.get())
    df=均线计算.增加ma列(df)
    a=新兴股票策略.peple()

    for index,row in df.iterrows():
        t=a.执行策略(row['close'],row['ma5'],row['time'])
        if not(t is None):
            # txinfo3_1.delete(1.0, END)
            txinfo3_1.insert(1.0, t)
            txinfo3_1.insert(1.0, '----------------\n')
            txinfo3_1.see(END)

def uptate_text():#更新输入框体函数
    global td

    for i in range(10):
        time.sleep(1)
        content=str(i)
        smtp_var2=StringVar()
        smtp_var2.set(content)
        entr2_1 = Entry(labelframe2,width=30,textvariable=smtp_var2, state="disable")#state='disable'参数为 不可更改.
        entr2_1.grid(row=1, column=0)

def new_thread2():
    global td

    td = threading.Thread(target=happy)
    td.setDaemon(True)
    td.start()

def happy():#更新文本框的函数
    global td
    con_list=[
'买入操作:因为当前价格3.7大于进场价3.6\n,买入时间: 2021 0201 1456\n,买入价格: 3.7\n,买入资金量: 99999.90\n,剩余资金: 0.1\n',
'卖出操作:因为当前价格4.7大于3.8,且小于均线5,并发生在盘末时间 2021 0201 1456\n,卖出时间: 2021 0201 1456\n,卖出价格: 4.7\n,卖出资金量: 127026.9\n,剩余资金: 127027\n',
'策略结束,本次策略盈利: 27027.0\n',
'本次策略回测时间为:2021/01/08至2021/03/03,回测标的为:sz.000778,共有1632条记录,执行操作2次.\n']
    for i in con_list:
        time.sleep(1)
        # txinfo3_1.delete(1.0, END)
        txinfo3_1.insert(1.0, i)
        txinfo3_1.insert(1.0, '----------------\n')
        txinfo3_1.see(END)

def list_1():
    l=[1,2,3]
    return l

#从运行中停止后的改变
def stop_moniter():
    global monit_state
    print(td.isAlive())
    monit_state=False
    btn1_r["state"]="normal"
    btn1_r['text'] = "开始"
    btn2_r["text"] = "停止中"
    btn2_r["state"]="disable"
    checkbox1_3["state"]="disable"
    enab_lfm1()
    if checkbox_val.get():
        # enab_lfm2()
        pass
    else:
        # disab_lfm2()
        pass
#构造windows外观及默认值

#构造windows外观及默认值
root = Tk()
root.title("黄志成量化系统1.0")
root.resizable(0,0)
labelframe1 = LabelFrame(root,width=25, height=30, text="回测股票设置")
labelframe1.grid(row=0, column=0,sticky=N)
labelframe2 = LabelFrame(root, width=25, height=20,text="策略信息")
labelframe2.grid(row=1, column=0,sticky=S)
labelframe3 = LabelFrame(root, text="监控结果")
labelframe3.grid(row=0, column=1, rowspan=3,sticky=N)
leble1_1 = Label(labelframe1, text="回测股票：")
leble1_1.grid(row=0, column=0,sticky=W)
leble1_2 = Label(labelframe1, text="回测开始时间：")
leble1_2.grid(row=2, column=0,sticky=W, )
leble1_3 = Label(labelframe1, text="回测结束时间：")
leble1_3.grid(row=4, column=0,sticky=W, )
web_addr=StringVar()
web_addr.set("sz.000778")
entr1_1 = Entry(labelframe1,width=32,textvariable=web_addr)#网页地址
entr1_1.grid(row=1, column=0, columnspan=2,sticky=W)
moni_time =StringVar()
moni_time.set('2021-01-01')
moni_time2 =StringVar()
moni_time2.set('2021-03-01')
entr1_2 = Entry(labelframe1, width=10, textvariable=moni_time) #起时间
entr1_2.grid(row=3, column=0,sticky=W)
entr1_3 = Entry(labelframe1, width=10, textvariable=moni_time2) #末时间
entr1_3.grid(row=5, column=0,sticky=W)
checkbox_val=BooleanVar()
checkbox_val.set(False)
checkbox1_3 = Checkbutton(labelframe1,variable=checkbox_val, text="是否...", command=change_stat)
checkbox1_3.grid(row=3, column=1)
leble2_1 = Label(labelframe2, text="进场策略")
leble2_1.grid(row=0, column=0,sticky=W)
leble2_2 = Label(labelframe2, text="平仓策略")
leble2_2.grid(row=2, column=0,sticky=W)
# leble2_3 = Label(labelframe2, text="平仓仓策略2")
# leble2_3.grid(row=4, column=0,sticky=W)
leble2_4 = Label(labelframe2, text="再进场策略")
leble2_4.grid(row=6, column=0,sticky=W)
leble2_5 = Label(labelframe2, text="再平仓策略")
leble2_5.grid(row=8, column=0,sticky=W)
leble2_6 = Label(labelframe2, text="......")
leble2_6.grid(row=10, column=0,sticky=W)
leble2_7 = Label(labelframe2, text="条件1")
leble2_7.grid(row=3, column=0,sticky=W)
leble2_8 = Label(labelframe2, text="条件2")
leble2_8.grid(row=4, column=0,sticky=W)
smtp_var=StringVar()
smtp_var.set("当前价格 大于  进场价")
entr2_1 = Entry(labelframe2,width=30,textvariable=smtp_var, state="disable")#state='disable'参数为 不可更改.
entr2_1.grid(row=1, column=0)
user_var=StringVar()
user_var.set("当前价格 大于 平仓价,且小于均线")
entr2_2 = Entry(labelframe2,width=25,textvariable=user_var,state="disable")
entr2_2.grid(row=3, column=0,sticky=E)
user_var2=StringVar()
user_var2.set("时间发生在盘末5分钟")
entr2_3 = Entry(labelframe2,width=25,textvariable=user_var2,state="disable")
entr2_3.grid(row=4, column=0,sticky=E)
pw_var=StringVar()
pw_var.set("password")
# entr2_3 = Entry(labelframe2,width=30,textvariable=pw_var, show="@",state="disable")
# entr2_3.grid(row=5, column=0)
title_var=StringVar()
title_var.set("-*-------*-")
entr2_4 = Entry(labelframe2,width=30,textvariable=title_var,state="disable")
entr2_4.grid(row=7, column=0)
title_var=StringVar()
title_var.set("......")
entr2_5 = Entry(labelframe2,width=30,textvariable=title_var,state="disable")
entr2_5.grid(row=9, column=0)
title_var=StringVar()
title_var.set("......")
entr2_6 = Entry(labelframe2,width=30,textvariable=title_var,state="disable")
entr2_6.grid(row=11, column=0)
txinfo3_1=ScrolledText(labelframe3, height=50, width = 60)
txinfo3_1.pack()
frame4=Frame(root)
frame4.grid(row=2,column=0)
btn1_r=Button(frame4,width=10,text ="开始", command=new_thread)
btn1_r.grid(row=0, column=0)
btn2_r=Button(frame4,width=10,text ="停止中", state="disable", command=stop_moniter)
btn2_r.grid(row=0, column=1)
# btn3_r=Button(frame4,width=10,text ="update", command=new_thread2)#第三个按钮
# btn3_r.grid(row=1, column=0)
btn4_r=Button(labelframe1,width=10,text ="回测", command=回测_thread2)#第三个按钮
btn4_r.grid(row=5, column=1)
monit_state = True


root.mainloop()