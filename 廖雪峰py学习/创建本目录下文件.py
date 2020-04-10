

import os
print('\n监控本文件名----------------------------------------------------------------------.1\n')
print(__file__)
# 获取本文件名方法
print(os.path.basename(__file__))
print('\n创建新路径----------------------------------------------------------------------.2\n')
# 创建的新文件名
cre='qqqq.py'
old=__file__
# 切掉本文件名加上新文件名
new=old[:-len(os.path.basename(__file__))]+cre
print(new)
# f=open(new,'w')