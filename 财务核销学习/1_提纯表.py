



import pandas as pd
import chardet
try :
	def 找遍所有文件里某类型文件的路径(path,x=4,s='.csv'):
	    '''   输入:#找遍path文件夹里所有尾部最后x=3位为s='.py'的文件
	          输出:list类型所有文件路径的列表'''

	    import os
	    所找文件路径 = []
	    #在walk的第二层里,排除venv文件夹
	    for 二层 in os.walk(path):
	        if 'venv' in 二层[0]:
	            pass
	        else:
	            #在第二层的下一层第三个包里,找最后3个字符等于.py的.
	            for 四层 in 二层[2]:
	                if 四层[-(x):]==s :
	                    所找文件路径.append((二层[0]+'/'+四层,四层))
	    return 所找文件路径
		
	def 求编译(文件路径):
		with open(文件路径,'rb') as f_rb:
			破译=chardet.detect(f_rb.read())
			编译方式=破译['encoding']
			if 编译方式=='GB2312':#更换
				编译方式='GB18030'
		return 编译方式

	def rewrite(文件路径,编译方式):#重新写入过筛后的内容
		开的内容={'微信':'交易时间','金卡':'交易日期','信用卡':'交易日期','支付宝':'付款时间'}
		关的内容={'微信':'微信没有关内容','金卡':',,,,,,,,,,,,','信用卡':'信用卡没有关内容','支付宝':'-----------------'}
		开关=0
		
		for i in 开的内容:
			if i in 文件路径:
				开启值=开的内容[i]
				关闭值=关的内容[i]

		with open(文件路径,encoding=编译方式) as f:
			文本=[]
			for i in f.readlines():#开关控制添加文本内容
				# print(i)
				if 开启值 in i:
					开关=1
				elif 关闭值 in i:
					开关=0
				elif i==' \n':#针对信用卡,最后一行为:' \n'
					开关=0
				if 开关==1:
					文本.append(i)
		return 文本
	
	def save(文本,保存路径):
		with open(保存路径,'w',encoding='UTF-8-SIG') as f2:
			for i in 文本:
				f2.write(i)

	def 批量清洗(文件路径,保存路径):
		All_file=找遍所有文件里某类型文件的路径(文件路径)
    	#遍历文件名
		for i in All_file:
			文本=rewrite(i[0],求编译(i[0]))
			save(文本,保存路径+'/'+i[1])


	if __name__ == '__main__':

		文件路径='C:/Users/YcAllenEffy/Desktop/财务账/待处理账表'
		保存路径="C:/Users/YcAllenEffy/Desktop/财务账/已处理账表1次"

		批量清洗(文件路径,保存路径)	


except Exception as e:
	print('异常错误:',e,'\nLine at:',e.__traceback__.tb_lineno)