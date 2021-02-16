f1=open('E:/PythonStudy_Git/调用资料/106.txt','r',encoding='utf-8')
data=[i.strip() for i in f1.readlines()]

def pickdb(data):
	db=[]
	for i in data:
		k=0
		for i2 in i:
			if i2==' ':
				datax=[]
				datax.append(int (i[:k]))
				datax.append(int(i[k+1:]))
				db.append(tuple(datax))
				k+=1
			else:
				k+=1
	return db

sched=pickdb(data)

start=sched[0][0]
end=sched[0][1]
for i in sched:
	start=min(start,i[0])
	end=max(end,i[1])

def countMan(sched,start,end):
	count1=[0]*(end+1)
	for i in range(start,end+1):
		for s in sched:
			if s[0]<=i<s[1]:
				count1[i]+=1
	return count1

countMan_real=countMan(sched,start,end)
countMax=max(countMan_real[start:end+1])
time=countMan_real.index(countMax)

print(f'Best time to attend the party is at {time} oclock:{countMax} celebrities will be attending')
print(start,end)
print(sched)