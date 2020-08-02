
import  pymysql.cursors
import tushare as ts

# 加载mysql,建立连接
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
#建立链接载体,加载cursor
cursor = connection.cursor()

#创建语句:
#创建表,表面,persons3 表头字段Id_p为int类型,varchar为字符串255类型,指定Id_p为key.搜索引擎为InnoDB,默认为CHARSET=utf8编码.
#搜索引擎:
	#InnoDB 感觉暂定更先进的引擎,但是python写入插入语句对数据库无效
	#MyISAM 较常规的引擎,可以用python写入插入语句

sql = "CREATE TABLE Persons3(Id_P int,内容 varchar(255),PRIMARY KEY (`Id_P`))ENGINE=InnoDB DEFAULT CHARSET=utf8;"
		#数据类型说明
		'''数据类型
			数据类型 TINYINT	1 byte	(-128，127)	(0，255)	小整数值
					SMALLINT	2 bytes	(-32 768，32 767)	(0，65 535)	大整数值
					MEDIUMINT	3 bytes	(-8 388 608，8 388 607)	(0，16 777 215)	大整数值
					INT或INTEGER	4 bytes	(-2 147 483 648，2 147 483 647)	(0，4 294 967 295)	大整数值
					BIGINT	8 bytes	(-9,223,372,036,854,775,808，9 223 372 036 854 775 807)	(0，18 446 744 073 709 551 615)	极大整数值
					FLOAT	4 bytes	(-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38)	0，(1.175 494 351 E-38，3.402 823 466 E+38)	单精度
					浮点数值
					DOUBLE	8 bytes	(-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)	0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308)	双精度
					浮点数值
					DECIMAL	对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2	依赖于M和D的值	依赖于M和D的值	小数值
			日期类型
					DATE	3	1000-01-01/9999-12-31	YYYY-MM-DD	日期值
					TIME	3	'-838:59:59'/'838:59:59'	HH:MM:SS	时间值或持续时间
					YEAR	1	1901/2155	YYYY	年份值
					DATETIME	8	1000-01-01 00:00:00/9999-12-31 23:59:59	YYYY-MM-DD HH:MM:SS	混合日期和时间值
					TIMESTAMP	4	
					1970-01-01 00:00:00/2038

					结束时间是第 2147483647 秒，北京时间 2038-1-19 11:14:07，格林尼治时间 2038年1月19日 凌晨 03:14:07

					YYYYMMDD HHMMSS	混合日期和时间值，时间戳
			字符串类型
					CHAR	0-255 bytes	定长字符串
					VARCHAR	0-65535 bytes	变长字符串
					TINYBLOB	0-255 bytes	不超过 255 个字符的二进制字符串
					TINYTEXT	0-255 bytes	短文本字符串
					BLOB	0-65 535 bytes	二进制形式的长文本数据
					TEXT	0-65 535 bytes	长文本数据
					MEDIUMBLOB	0-16 777 215 bytes	二进制形式的中等长度文本数据
					MEDIUMTEXT	0-16 777 215 bytes	中等长度文本数据
					LONGBLOB	0-4 294 967 295 bytes	二进制形式的极大文本数据
					LONGTEXT	0-4 294 967 295 bytes	极大文本数据'''
sql = f"select * from code600118 where Date='2019-11-15'"#选中语句
sql = f"DROP TABLE code000860"#删除表

#执行语句
cursor.execute(sql)

#返回结果:
# returns=cursor.execute(sql)#执行并返回获取的数据条数
# cursor.fetchone()：将只返回一条结果，返回单个元组如('id','title')。
# cursor.fetchall() :也将返回所有结果，返回二维元组，如(('id','title'),),
# cursor.fetchmany(3)获取前三行数据，元组包含元组

connection.close()#关闭连接,等于关闭所有载体cursor.

