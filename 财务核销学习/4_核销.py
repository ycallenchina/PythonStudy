

def 执行sql(sql,play=0):
	import  pymysql
	import  pymysql.cursors
	connection=pymysql.connect(host='localhost',
	                           user='root',
	                           password='123456',
	                           db='test_data',
	                           port=3306,
	                           charset='utf8')
	cursor = connection.cursor()
	Answer='未执行sql'
	if play==0:
		print(sql)
	else:	
		cursor.execute(sql)
		Answer=cursor.fetchall()
	connection.close()
	return Answer

def 核销执行(主账,副账,核销期,play=0):
	import pandas as pd
	#关联字段表
	df=pd.DataFrame({
	'金卡账表':['金卡临时','金卡核销','记账金额','交易日期'],
	'信用卡账表':['信用卡临时','信用卡核销','记账金额','交易日期'],
	'微信账表':['微信临时','微信核销','金额_元','交易时间'],
	'支付宝账表':['支付宝临时','支付宝核销','金额_元','付款时间']
	},
	index=['临时卡','核销语','金额','时间']
	) 
	#分清交易场所是微信的还是支付宝
	账list=[主账,副账]
	if any('微信' in i for i in 账list):
		if any('金卡' in i for i in 账list):
			场所条件="交易场所 LIKE '财付通%' AND 支付方式 LIKE '%(1475)%'"
		elif any('信用卡' in i for i in 账list):
			场所条件="交易场所 LIKE '财付通%' AND 支付方式 LIKE '%(4189)%'"
	elif any('支付宝' in i for i in 账list):
		场所条件="交易场所 LIKE '支付宝%'"
	else:
		场所条件="交易场所='场所出错!'"

	sql=f'''
	UPDATE {主账} SET 核销='{df.loc['核销语',副账]}' WHERE 序号 IN (
	SELECT DISTINCT A.序号
	FROM {df.loc['临时卡',主账]} AS A INNER  JOIN {df.loc['临时卡',副账]} AS B
	ON A.`{df.loc['金额',主账]}`=B.`{df.loc['金额',副账]}` AND DATE(A.`{df.loc['时间',主账]}`)=DATE(B.`{df.loc['时间',副账]}`)
	WHERE {场所条件}
	)
	AND 财务期='{核销期}'
	'''
	执行sql(sql,play)
	return
def 加载临时表(主账,副账,核销期,play=0):
	#初始化
	临时卡={'金卡账表':'金卡临时',
		    '信用卡账表':'信用卡临时',
		    '微信账表':'微信临时',
		    '支付宝账表':'支付宝临时'}

	#加载临时表
	清空_主账临时=f'''TRUNCATE TABLE {临时卡[主账]}'''
	清空_副账临时=f'''TRUNCATE TABLE {临时卡[副账]}'''
	写入_主账临时=f'''INSERT INTO {临时卡[主账]} SELECT * FROM {主账} WHERE 财务期="{核销期}"'''
	写入_副账临时	=f'''INSERT INTO {临时卡[副账]} SELECT * FROM {副账} WHERE 财务期="{核销期}"'''
	All_重载=[清空_主账临时,清空_副账临时,写入_主账临时,写入_副账临时]
	
	for i in All_重载:
		执行sql(i,play)	
	return

def 两表对账(主账,副账,核销期='20年50期',play=0):
	def 对账sql(主账,副账):
		import pandas as pd
		#关联字段表
		df=pd.DataFrame({
		'金卡账表':['金卡临时','金卡核销','记账金额','交易日期'],
		'信用卡账表':['信用卡临时','信用卡核销','记账金额','交易日期'],
		'微信账表':['微信临时','微信核销','金额_元','交易时间'],
		'支付宝账表':['支付宝临时','支付宝核销','金额_元','付款时间']
		},
		index=['临时卡','核销语','金额','时间']
		) 

		sql=f'''
		SELECT SUM({df.loc['金额',主账]})
		FROM {主账} 
		WHERE 核销='{df.loc['核销语',副账]}' AND 财务期='{核销期}'
		'''
		return sql

	#两表取对应的账,例:工行的微信核销的金额  等于  微信里工行核销的金额.
	#然后看看总和是否相等
	主对副=对账sql(主账,副账)
	主账总和=执行sql(主对副,play)
	副对主=对账sql(副账,主账)
	副账总和=执行sql(副对主,play)
	if 主账总和[0][0]==副账总和[0][0]:
		print('本次账已对','\n','结果是:',主账,'对',副账,'金额为',主账总和,'核销期:',核销期)
	else:
		print('对账有误','\n','结果是:',主账,主账总和,'对',副账,副账总和,'核销期:',核销期)
	return	

def 清账(清账期,play=0):
	import pandas as pd
	#关联字段表
	df=pd.DataFrame({
	'金卡账表':['金卡临时','金卡核销','记账金额','交易日期'],
	'信用卡账表':['信用卡临时','信用卡核销','记账金额','交易日期'],
	'微信账表':['微信临时','微信核销','金额_元','交易时间'],
	'支付宝账表':['支付宝临时','支付宝核销','金额_元','付款时间']
	},
	index=['临时卡','核销语','金额','时间']
	) 

	for i in df:
		sql=f'''TRUNCATE TABLE {df.loc['临时卡',i]};'''
		执行sql(sql,play)
		sql=f'''UPDATE {i} SET 核销='' WHERE 财务期='{清账期}'; '''
		执行sql(sql,play)

def 核销(主账,副账,核销期='20年50期',play=0):

	加载临时表(主账,副账,核销期,play)#本期数据重新加载
	核销执行(主账,副账,核销期,play)#主对副
	核销执行(副账,主账,核销期,play)#副对主
	两表对账(主账,副账,核销期,play)#主副是否相等
	return 


def 批量核销(核销期,play=0):
	工行卡=['金卡账表','信用卡账表']
	手机卡=['微信账表','支付宝账表']
	for i in 工行卡:
		for j in 手机卡:
			核销(i,j,核销期,play)#play=0只显示sql语句不执行sql

if __name__ == '__main__':
	
	批量核销('21年3期',play=1)
	# 清账('21年3期',0)
