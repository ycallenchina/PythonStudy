
# delete from tablename where id=?;

import  pymysql
import  pymysql.cursors

#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#port 必须是数字不能为字符串
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='test_data',
                           port=3306,
                           charset='utf8')
#开
sheets=['code000860','code000987','code600118']

cursor = connection.cursor()

#选择列的 内容=eff 的那一行记录
#执行sql语句并赋值给returns,它的返回值是 选择的记录条数
for i in sheets:
    sql = f"select * from {i} where Date='2019-11-15'"
    returns=cursor.execute(sql)
    print(returns)
    #写入sql
    #cursor.fetchall() 可查选中的记录内容,用法与next()类似,储存形式二维tuple
    for i  in cursor.fetchall():#解包 cursor.fetchall() 内容
        sql2=f'INSERT INTO 尝试无主键 VALUES {i}'
        print(sql2)
        cursor.execute(sql2)#逐条插入表 尝试无主键里
#关
connection.close()