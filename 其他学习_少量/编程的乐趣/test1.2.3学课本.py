

def pickdb():
	f1=open('E:/PythonStudy_Git/调用资料/106.txt','r',encoding='utf-8')
	data=[i.strip() for i in f1.readlines()]
	db=[]
	for i in data:
		k=0
		for i2 in i:
			if i2==' ':
				datax=[]
				datax.append(float (i[:k]))
				datax.append(float(i[k+1:]))
				db.append(tuple(datax))
				k+=1
			else:
				k+=1
	return db

schedule=pickdb()
schedule_new=[]
for i in schedule:
	schedule_new.append((i[0],'start'))
	schedule_new.append((i[1],'end'))

print(schedule_new)
def 给列表排序(sList):
	
	for i in range(len(sList)-1):
		run=i
		for c in range(i,len(sList)):
			if sList[run][0]>sList[c][0]:
				run=c
		sList[run],sList[i]=sList[i],sList[run]
def choosetimes(sList):

	maxcout=times=rcount=0

	for i in sList:
		if i[1]=='start':
			rcount+=1
		elif i[1]=='end':
			rcount+=-1
		if rcount>maxcout:
			maxcout=rcount
			times=i[0]
	return maxcout,times

给列表排序(schedule_new)
a,b=choosetimes(schedule_new)
print(a,b)

