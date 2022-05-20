
# -*- coding: utf-8 -*-
import sys


from PyQt5.QtWidgets import *


from Directory_UI import TableWidget1

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle('主窗口')

        laout=QHBoxLayout()

        self.button1=QPushButton()
        self.button1.clicked.connect(self.selectPath)
        self.button1.setText('文件地址')
        self.button2=QPushButton()
        self.button2.clicked.connect(self.onButton)
        self.button2.clicked.connect(self.close)
        self.button2.setText('提交')
        self.lineidt=QLineEdit()
        laout.addWidget(self.button1)
        laout.addWidget(self.lineidt)
        laout.addWidget(self.button2)
        self.setLayout(laout)

    def selectPath(self):
        self.path = QFileDialog.getExistingDirectory(self, '请选择保存目录', './',)
        if self.path[0]:
            self.lineidt.setText('选择的目录为：{}'.format(self.path))
            self.lineidt.adjustSize()


    def onButton(self):
        # self.Filepath = Filepath(self.URL)
        # self.True_filepaths = self.Filepath.True_filepath()
        # r1=PreventFastClickThreadMutex(filepaths=self.True_filepaths)
        # r1.start()

        self.tablewidget = TableWidget1(URL=self.path)
        self.tablewidget.init_ui()
        self.tablewidget.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())











