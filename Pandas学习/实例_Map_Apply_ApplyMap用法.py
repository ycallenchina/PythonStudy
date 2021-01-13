

'''
Pandas
数据处理工具,共3种
Map
Apply
ApplyMap
'''


import pandas as pd
import numpy as np


#Map--- Series一维数据的处理,常用于:一列或一行批量替换值

'''举例:
生成一张个人信息表格
各列分别代表身高、体重、是否吸烟、性别、年龄和肤色'''
boolean=[True,False]
gender=["男","女"]
color=["white","black","yellow"]
data=pd.DataFrame({
    "height":np.random.randint(150,190,100),
    "weight":np.random.randint(40,90,100),
    "smoker":[boolean[x] for x in np.random.randint(0,2,100)],
    "gender":[gender[x] for x in np.random.randint(0,2,100)],
    "age":np.random.randint(15,90,100),
    "color":[color[x] for x in np.random.randint(0,len(color),100) ]
}
)
#展示生成表
data2=data.copy()
print('原生\n',data2)

#Map

#map的使用方法--Series以为数据的处理
#提问:gender列男值替换为1,女值不变.
def gender_map(x):
    gender = 1 if x == "男" else x
    return gender
#注意这里传入的是函数名，不带括号
#注意data["gender"]是series类.
data["gender"] = data["gender"].map(gender_map)
print('map使用\n',data)
data=data2.copy()#重置data


#Apply_series

#Apply的使用方法--Series以为数据的处理
'''
Apply--- Series一维数据的处理
常用于:一列或一行批量替换值(可带参数)
'''
#提问:同表中,对age列进行参数计算调整的实现方法
def apply_age(x,bias,bias2):
    return (x+bias)*bias2
#以元组的方式传入额外的参数
#Args提供传参:-3和2分别传入apply_age函数里的bias和bias2
data["age"] = data["age"].apply(apply_age,args=(-3,2))
print('apply使用\n',data)
data=data2.copy()#重置data



#Apply_DataFrame

'''
Apply---DataFrame二维数据的处理
常用于:对相关多列或者多行数据进行处理

它控制了你指定的操作是沿着0轴还是1轴进行。
axis=0代表对列columns进行，
axis=1代表对行row进行.
'''
#举例:axis=0时,沿着0轴求和
data_sum=data[["height","weight","age"]].apply(np.sum, axis=0)
print('sum\n',data_sum)
#沿着0轴取对数_改变原来data
data[["height","weight","age"]]=data[["height","weight","age"]].apply(np.log, axis=0)
print('改log\n',data)
data=data2.copy()#重置data
#沿着0轴取对数_不改变data
data_log=data[["height","weight","age"]].apply(np.log, axis=0)


# 举例:axis=1时
# 计算每人的BMI指数:BMI=体重/身高的平方
def BMI(series):
    weight = series["weight"]
    height = series["height"]/100
    BMI = weight/height**2
    return BMI
data["BMI"] = data.apply(BMI,axis=1)#增加了一列"BMI"
print("BMI计算\n",data)
data=data2.copy()#重置data

'''
总结一下对DataFrame的apply操作：
1.	当axis=0时，对每列columns执行指定函数；当axis=1时，对每行row执行指定函数。
2.	无论axis=0还是axis=1，其传入指定函数的默认形式均为Series，可以通过设置raw=True传入numpy数组。
3.	对每个Series执行结果后，会将结果整合在一起返回（若想有返回值，定义函数时需要return相应的值）
4.	当然，DataFrame的apply和Series的apply一样，也能接收更复杂的函数，如传入参数等，实现原理是一样的，具体用法详见官方文档。
'''



#ApplyMap

'''
ApplyMap---DataFrame二维数据的处理
常用于:对整表数据进行处理
'''
#生成新表,纯浮点数
df_float = pd.DataFrame(
    {
        "A":np.random.randn(5),
        "B":np.random.randn(5),
        "C":np.random.randn(5),
        "D":np.random.randn(5),
        "E":np.random.randn(5),
    }
)
print('浮点数\n',df_float)
# 题问: 现在想将DataFrame中所有的值保留两位小数显示:
df_float=df_float.applymap(lambda x:"%.2f" % x)
print('浮点数保留2位小数\n',df_float)