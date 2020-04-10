# 去行头数字
r=open('test333.py','r',encoding='utf-8')
new=[]
num=[i for i in range(10)]
# 测试
# i='   231231'
# print(i.strip())
# print(str(num))
# print(i[0] in str(num))

# 去掉行首数字生成new列表
for i in r.readlines():
    # 去空行
    if i!='\n':
        j=i.strip()
        # print(j)
        if j[0] in str(num):
            # 把数字换成' '空格
            new.append(' '+j[1:])
        else:
            new.append(j)

# 将new转换字符串写入r2
r2=open('test444.py','w',encoding='utf-8')
for i in new:
    r2.write(str(i)+'\n')

r.close()
r2.close()