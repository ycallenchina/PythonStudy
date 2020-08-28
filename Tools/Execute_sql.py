from Tools.sql_db import *

def 执行sql(x,表名,字段='',where=1,值=''):
  answer='No Answer'
  if x=='删除表':#删除表
    cursor.execute(f"DROP TABLE {表名}")
    print('删除成功')
  elif x=='清空表':
    cursor.execute(f"TRUNCATE TABLE {表名}")
    answer='清空成功'
  elif x==3:#删除数据库
    cursor.execute("DROP DATABASE 数据库名称")
  elif x=='删除内容行':
    cursor.execute(f"delete from {表名} where {where}")
    answer=f'行名:{where}'
  elif x==5:#删除多行内容
    cursor.execute("delete from code600118 where Date in('7000')")
  elif x=='select':
    cursor.execute(f'select {字段} from {表名} where {where}')
    answer=cursor.fetchall()
  elif x=='表字段名':
    cursor.execute(f'show columns from {表名}')
    answer=tuple([i[0] for i in cursor.fetchall()])
  elif x=='insert_values':
    cursor.execute(f"INSERT INTO {表名} VALUES "+值)
    answer=值
  elif x=='insert_set':
    cursor.execute(f"INSERT INTO {表名} set "+值)
    # print(f"INSERT INTO {表名} set "+值)
    answer=值
  elif x=='create table':
    cursor.execute(f"CREATE TABLE {表名}({字段})ENGINE=MyISAM DEFAULT CHARSET=utf8;" )
    answer='建新表名='+表名+',字段='+字段
  elif x=='update':
    cursor.execute(f"UPDATE {表名} SET {字段} WHERE {where}")
    answer='更新成功'
  else:
    print('没执行任何语句.')
  return answer
	