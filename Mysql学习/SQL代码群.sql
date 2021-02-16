#嵌套子查询
SELECT * FROM csi中证指数
WHERE NAME IN (
	SELECT NAME
	FROM csi中证指数 
	GROUP BY name
	HAVING SUM(base_point)>1000
	)

#工行核销微信
TRUNCATE TABLE 金卡临时;#清空临时卡
INSERT INTO 金卡临时 SELECT * FROM 金卡20年50期;#导入归附卡数据
TRUNCATE TABLE 微信临时;#清空临时卡
INSERT INTO 微信临时 SELECT * FROM 微信20年50期;#导入归附卡数据
#用子查询 核销两条相关数据
UPDATE 金卡20年50期 SET 核销='微信核销' WHERE 序号 IN (
SELECT DISTINCT jk.序号
FROM 金卡临时 AS jk INNER  JOIN 微信临时 AS wx
ON jk.`记账金额`=wx.`金额_元` AND DATE(jk.`交易日期`)=DATE(wx.`交易时间`)
)

#查询时自动增加一列参考序号
set @ROW = 0;
SELECT *,@row:=case when @row is null then 1 else @row+1 end as RNr
FROM 账表微信

#创建财务表
CREATE TABLE `qe` (
	`字段 1` INT(11) NOT NULL,
	`字段 2` DECIMAL(10,2) NOT NULL,
	`字段 3` VARCHAR(255) ,
	PRIMARY KEY (`字段 1`) USING BTREE
)

DEFAULT CHARSET=UTF8
ENGINE=MYISAM ;

#财务汇总临时
#CREATE TABLE 财务汇总临时 

SELECT  序号 ,'信用卡' AS 所属, 交易日期, 记账金额, 收_支, 余额,摘要, 交易场所,核销 
FROM 信用卡20年50期

UNION ALL 

SELECT 序号,'金卡' AS 所属, 交易日期, 记账金额, 收_支, 余额,摘要, 交易场所,核销 
FROM 金卡20年50期

UNION ALL

SELECT 序号,'微信' AS 所属, 交易时间,金额_元,收支,余额,支付方式,交易对方,核销
FROM 微信20年50期

UNION ALL

SELECT 序号,'支付宝' AS 所属, 付款时间,金额_元,收支,余额,商品名称,交易对方,核销
FROM 支付宝20年50期


#删除主键
ALTER  TABLE  支付宝账表 DROP  PRIMARY  KEY 
