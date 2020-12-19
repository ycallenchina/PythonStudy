# 转换qrc资源文件,命令行里输入:当前文件所在路径>pyrcc5 文件名.qrc -o 转换后的文件名.py

# 转换qtDesign的UI文件,命令行里输入:当前文件所在路径>pyuic5 文件名.ui -o 转换后的文件名.py


'''
转换后在所转换后的py文件里面添加以下执行代码打开
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''