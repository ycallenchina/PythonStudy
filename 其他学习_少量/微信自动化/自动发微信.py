import itchat

# 参数itchat.auto_login(hotReload=True)实现第一次运行时扫码，一定时间内再次运行就不用扫码了
itchat.auto_login(hotReload=True)
# itchat.auto_login(enableCmdQR=-1)

# 给文件助手发微信
# itchat.send('你好',toUserName='filehelper')

# 获取微信好友字段名
vx_file=itchat.search_friends(name='linmeo')
vx_name_key=vx_file[0]['UserName']

itchat.send('Hello!,This is auto send from python.',toUserName=vx_name_key)

# 登出
itchat.logout()