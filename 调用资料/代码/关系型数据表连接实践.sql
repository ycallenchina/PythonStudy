SELECT 菜名id表.`菜id`,SUM(销售金额),菜名id表.`菜品名称`
FROM 菜名id表 INNER JOIN andyou9月明细 
ON 菜名id表.`菜id`=andyou9月明细.`菜id`
	WHERE DAY (时间) IN (1,2,3)
	GROUP BY 菜名id表.`菜id`,菜名id表.`菜品名称`