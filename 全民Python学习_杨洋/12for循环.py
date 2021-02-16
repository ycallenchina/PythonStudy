
x=['eff','Allen','Xman','Q博士','98','55']
y=[1,2]
k={1:'qq',2:'kk'}

for e in k.values():
    print('字典的值：',e)

# for循环改不了列表元素，while循环可以修改列表里面元素
for i in y:
    print(i)
    i=i*2
print(y)

q=0
while q<2:
    print(y[q])
    y[q]=66
    q=q+1
print(y)

# range函数使用，指定次数循环,还可以按照步长使用
for i in range(2,6,2):
    print(i)

# in和not in还可以用于判断是否包含某元素.

print(y)
if 66 in y:
 print('在y里面')
else:
 print('不在y里面')

