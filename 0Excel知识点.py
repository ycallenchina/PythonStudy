#excel的竖向导入
import xlwings as xw
def 新建表():
    app = xw.App()
    wb = app.books.add()
    ws = wb.sheets[0]
    F=list(A)
    #竖向写入
    ws.range('B2').options(transpose=True).value =F
    wb.save('E:\pyNote\调用资料/43class.xlsx')
    wb.close()
    app.quit()

def 读取表():
    app = xw.App()
    wb=app.books.open('E:\pyNote\调用资料/43class.xlsx')
    工资=wb.sheets[0].range('c6:e9').value

    wb.save('E:\pyNote\调用资料/43class.xlsx')
    wb.close()
    app.quit()
    return 工资

def 写入表格(k):
    app = xw.App()
    wb=app.books.add()
    wb.sheets[0].range('b10').value=k
    # 写入新的文件地址
    wb.save('E:\pyNote\调用资料/44class.xlsx')
    wb.close()
    app.quit()

a=读取表()
print(a)
b=写入表格(a)


