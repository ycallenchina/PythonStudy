
#elif 按照从下到上的包含关系，不然>1的情况放上面就会永远不会执行下面>5的情况。
house=int(input('输入房产数：'))
# 多分支判断结构
if house>5:
    print('大哥，你来了')
elif house>2:
    print('哥，你来了')
elif house>1:
    print('你来了')
else:
    print('滚')
#逻辑判断的顺序：not》》and》》or，所以避免循序的错误最好用（）表面你的逻辑关系。
age=int(input('请输入年龄：'))
gender=input('请输入性别：')

if gender=='女' and not 20<age<30:
    print('你不是我要找的人')
else:
    print('妞，你来啦!')