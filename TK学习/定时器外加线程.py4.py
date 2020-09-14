# import pandas as pd
# import numpy as np
import sys
sys.path.append("..")#为了import引用上一级包
import time
import threading

def fun_timer():
    print('Hello Timer!')
    global timer
    timer = threading.Timer(2, fun_timer)
    timer.start()
    print(time.strftime("%b %d %Y %H:%M:%S", time.localtime()))

timer = threading.Timer(1, fun_timer)
timer.start()
time.sleep(15) # 15秒后停止定时器
timer.cancel()