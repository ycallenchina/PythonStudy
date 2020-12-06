SELECT * FROM csi中证指数
WHERE NAME IN (
	SELECT NAME
	FROM csi中证指数 
	GROUP BY name
	HAVING SUM(base_point)>1000
	)
