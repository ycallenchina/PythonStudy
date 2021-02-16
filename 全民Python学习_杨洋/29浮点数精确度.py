from decimal import Decimal
# Decimal精度高，性能低
# round方便、不能解决精度问题
# format设置输出格式
#inf表示无穷大,nan表示不是数字
x=Decimal('0.1')+Decimal('0.2')
y=format(2.5,'0.2f')
i=float('inf')
k=float('-inf')

print(i/k)
print(1/i)
print(k)
print(round(3.465,2))
print(x)
print(y)