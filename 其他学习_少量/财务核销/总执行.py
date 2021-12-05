
import A提纯表
import B清洗表
import C写入sql
import D核销
import E合并为csv

期数='21年5期'
start='2021-02-15 00:00:00'
end='2021-02-28 23:59:59'

待处理路径="C:/Users/YcAllenEffy/Desktop/财务账/待处理账表"
已处理1次路径="C:/Users/YcAllenEffy/Desktop/财务账/已处理账表1次"
已处理2次路径="C:/Users/YcAllenEffy/Desktop/财务账/已处理账表2次"
csv导出路径=f'C:/Users/YcAllenEffy/Desktop/财务账/{期数}明细2.csv'


# A提纯表.批量清洗(待处理路径,已处理1次路径)
# B清洗表.批量清洗(已处理1次路径,已处理2次路径,期数,start,end)
# C写入sql.批量导入sql(已处理2次路径,1)
# D核销.批量核销(期数,play=1)
E合并为csv.导出sql表为csv(期数,csv导出路径,play=1)
