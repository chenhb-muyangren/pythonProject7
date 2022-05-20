# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Filepath import Filepath
from Qt_dialog2 import TableWidget

from Thread_Pool import Paddleocr
from queue import Queue

# 继承QWidget
class TableWidget1(QWidget):
    '''
    展示文件夹路径
    '''
    sendmsg=pyqtSignal(list)

    def __init__(self,URL):
        super(TableWidget1,self).__init__()
        self.URL=URL
        self.init_ui()

    def init_ui(self):

        layout = QHBoxLayout()
        self.Filepath=Filepath(self.URL)
        self.True_filepaths=self.Filepath.True_filepath()
        self.producer()

        len1=len(self.True_filepaths)

        self.table_widget = QTableWidget(len1, 3)
        self.table_widget.setHorizontalHeaderLabels(['文件地址'])


        for x,item in zip(range(len(self.True_filepaths)),self.True_filepaths):
            #self.table_widget.setItem(x, 0, QTableWidgetItem(x))
            self.table_widget.setItem(x,0,QTableWidgetItem(item))
            self.table_widget.resizeColumnToContents(0)
        #print(self.table_widget.columnWidth(1))
        #print(self.table_widget.hideColumn(1))
        self.button1=QPushButton()
        self.button1.setText('确认')
        self.button1.clicked.connect(self.onClick1)
        self.button1.clicked.connect(self.onClick2)
        self.button1.clicked.connect(self.close)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.button1)
        self.setLayout(layout)
        self.resize(800,500)
    def producer(self):

        self.Filepath_queue=Queue(500)

        for filepath in self.True_filepaths:

            self.Filepath_queue.put(filepath)

    def onClick1(self):

        self.window2=TableWidget()
        self.window2.init_ui()
        self.window2.show()

    def onClick2(self):

        for x in range(4):
            r1=Paddleocr(filepaths=self.Filepath_queue)
            r1.start()


if __name__ == "__main__":
    URL='/Users/mac/Desktop/test_data/day2'
    app = QApplication(sys.argv)
    w = TableWidget1(URL)
    w.show()
    sys.exit(app.exec_())



