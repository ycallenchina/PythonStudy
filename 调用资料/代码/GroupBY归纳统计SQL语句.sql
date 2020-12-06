SELECT category,NAME,COUNT(NAME), SUM(base_point),'new' AS newname 
	FROM csi中证指数 
	GROUP BY category ,name
	HAVING SUM(base_point)>1000