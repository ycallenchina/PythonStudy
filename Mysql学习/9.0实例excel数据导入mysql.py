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
# 执行mysql语句
# cursor = connection.cursor()
# cursor.execute("alter table 杨老师python学习 add primary key (内容)")

# excel读取
import xlwings as xw
app=xw.App(visible=True,add_book=False)
app.display_alerts=True
app.screen_updating=True
#文件位置：filepath，读取,然后保存，关闭，结束程序
filepath=r'E:\pyNote\调用资料/pystudy.xlsx'
wb=app.books.open(filepath)
sht=wb.sheets['sheet1']

# 读取excel表sheet1内所有数据(expand用法不明,A2有起始列的意思,有自动识别内容意思)
a=sht.range('A2').expand().value
print(a)
# mysql插入语句
cursor = connection.cursor()
for i in a:
    cursor.execute(f"INSERT INTO persons3 VALUES ('{i[0]}','{i[1]}')")
    # print(i[0])

# 关闭excel,mysql
wb.save()
wb.close()
app.quit()
connection.close()