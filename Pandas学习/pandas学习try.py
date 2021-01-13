

import pandas as pd
import numpy as np

boolean=[True,False]
gender=["男","女"]
color=["white","black","yellow"]
df1=pd.DataFrame({
    "height":np.random.randint(150,190,10),
    "weight":np.random.randint(40,90,10),
    "smoker":[boolean[x] for x in np.random.randint(0,2,10)],
    "gender":[gender[x] for x in np.random.randint(0,2,10)],
    "age":np.random.randint(15,90,10),
    "color":[color[x] for x in np.random.randint(0,len(color),10) ]
    }
)    
df4=pd.DataFrame({
    "height":np.random.randint(150,190,10),
    "weight":np.random.randint(40,90,10),
    "smoker":[boolean[x] for x in np.random.randint(0,2,10)],
    "gender":[gender[x] for x in np.random.randint(0,2,10)],
    "age":np.random.randint(15,90,10),
    "color2":[color[x] for x in np.random.randint(0,len(color),10) ]
    }
) 

def clean(x):
    if isinstance(x,int):
        x=np.log(x)
    else:
        pass
    return x

#检查每列第一值数据的类型
# for column in df1.columns.values:
#     print(type(df1[column][0]))
#     print(isinstance(df1[column][0],np.bool_))
# pd.set_option('display.max_columns', None)#显示所有列,不隐藏
df11=df1.copy()
df2=df1.applymap(type)

print(df2.head(3))
print('原生df\n',df11)