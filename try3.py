#!/usr/bin/python
# -*- coding: utf-8 -*-

#@Author           :  BigBro
#@DateTime         :  2015-11-17 16:57:30
#@Filename         :  weiyunsc_2.2.py
#@Description      :  微云收藏 2.2 自动检测 剪贴板 


import tkinter
import urllib.parse
import os

running = False # Global flag
old_text = ' '
def getClipboardText(tk):
    # win32clipboard.OpenClipboard()
    # result = win32clipboard.GetClipboardData(win32con.CF_TEXT)
    # win32clipboard.CloseClipboard()
    result = tk.clipboard_get()
    return result

def weiyunsc2_0(tk):
    #input('复制网址，回车')
    url=getClipboardText(tk)
    #url=url.decode('utf-8') #transform bytes into str  #tk下 获取的内容直接为str,不需要转换
    url = str(url)
    
    chrome = 'chrome.exe'

    prefix = r'http://sc.qq.com/'
    prefix2 =r'mp.weixin.qq.com' 
    if url.startswith(prefix):
        url = url[17:] #strip 'http://sc.qq.com/'
        url= urllib.parse.unquote(url)
        url_list_str = ''.join([u  if u !='&' else '^&' for u in list(url) ]) #cmd 命令行 对&是保留字,需要^来转义
        os.system("{0} {1}".format(chrome,url_list_str))
    elif url.startswith(prefix2):
        os.system("{0} {1}".format(chrome,url))
    else:   
        url=''.join([u  if u !='&' else '^&' for u in list(url) ])#如果u !='&'则u就是u,否则,u='^&'
        os.system("{0} {1}".format(chrome,url))

def WatchClipboard(tk):#监视剪切板 返回
    global old_text
    text = getClipboardText(tk)
    if running:
        if old_text != text:
            weiyunsc2_0(tk)
            old_text = text
    tk.after(500, lambda:WatchClipboard(tk))

def start():
    """Enable scanning by setting the global flag to True."""
    global running
    running = True

if __name__ == '__main__':
    top = tkinter.Tk() #定义一个窗口
    top.title('微云收藏2.2') #定义窗口标题
    top.geometry('400x200')     #定义窗体的大小，是400X200像素

    func = tkinter.Button(top,text='开始',command = start)
    func.pack(expand = 'yes', fill = 'both')


    quit = tkinter.Button(top, text='Quit',
        command=top.quit)
    quit.pack(expand='yes', fill = 'both')

    top.after(500, lambda:WatchClipboard(top))

    tkinter.mainloop()