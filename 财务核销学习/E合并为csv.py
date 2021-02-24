
import pandas as pd
import  pymysql
import  pymysql.cursors

connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
cursor = connection.cursor()

def 保存csv文件(保存路径,df):
    df.to_csv(保存路径,encoding='utf_8_sig',index=False)

def 保存xlsx文件(保存路径,df):
	df.to_excel(保存路径,encoding='utf_8_sig',index=False)

def 合并sql表(核销期):
	
	sql=f'''
	SELECT  序号 ,'信用卡' AS 所属, 交易日期, 记账金额, 收_支, 余额,摘要, 交易场所,备注,核销,财务期
	FROM 信用卡账表
	WHERE 财务期='{核销期}'
	
	UNION ALL 

	SELECT 序号,'金卡' AS 所属, 交易日期, 记账金额, 收_支, 余额,摘要, 交易场所,备注,核销,财务期
	FROM 金卡账表
	WHERE 财务期='{核销期}'

	UNION ALL

	SELECT 序号,'微信' AS 所属, 交易时间,金额_元,收支,余额,支付方式,交易对方,备注,核销,财务期
	FROM 微信账表
	WHERE 财务期='{核销期}'

	UNION ALL

	SELECT 序号,'支付宝' AS 所属, 付款时间,金额_元,收支,余额,商品名称,交易对方,备注,核销,财务期
	FROM 支付宝账表
	WHERE 财务期='{核销期}'

	ORDER BY 财务期,所属,序号
	'''
	return sql

def 导出sql表为csv(合并期,导出路径,play=0):

	sql=合并sql表(合并期)
	cursor = connection.cursor()
	cursor.execute(sql)
	keys=[i[0] for i in cursor.description]#去sql字段名

	df=pd.DataFrame(cursor.fetchall())
	df.columns=tuple(keys)

	if play==0:
		print(sql)
		print(df)
	else:
		# print(df)
		保存csv文件(导出路径,df)

if __name__ == '__main__':

	合并期='21年3期'
	导出路径=f'C:/Users/YcAllenEffy/Desktop/财务账/{合并期}明细2.csv'
	导出sql表为csv(合并期,导出路径,play=0)


	connection.close()