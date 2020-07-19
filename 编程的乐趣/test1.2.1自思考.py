

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

def madedb(data):
	db=[]
	for i in range(data[0],data[1]):
		datax=[]
		datax.append(i)
		datax.append(i+1)
		db.append(tuple(datax))
	return db

datai=[6,12]

schedule=madedb(datai)	
meetingtime=pickdb(data)

#循环次数统计
m_count=0
s_count=0
#出席时间点的名人出现次数统计字典
s_dict=dict.fromkeys(range(len(schedule)),0)

#思路是求:meetingtime名人出席时间段在schedule日程的时间段中有多少个.
for s in schedule:
	for m in meetingtime:
		if m[0]<=s[0]<m[1] or m[0]<s[1]<m[1] :
			s_dict[s_count]+=1
			m_count+=1
		else:
			m_count+=1
	s_count+=1		
print(schedule)
print(s_dict)



