select category,sbase_point from csi中证指汇总 
where sbase_point!=(
	select sum(base_point) from csi中证指数 
where csi中证指数.category=csi中证指汇总.category)
	