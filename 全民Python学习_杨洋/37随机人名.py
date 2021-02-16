import random


姓=['邱','伦','杀','王','李']
名=['马','婷','力','静','玉','爱','芝','特']

i=0
名册=[]
while i<20:

    姓名=''.join(random.sample(姓,1)+random.sample(名,random.randint(1,2)))
    if 姓名 not in 名册:
        名册.append(姓名)
        i=i+1




print(名册)
