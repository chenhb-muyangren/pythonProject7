# coding=utf-8

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\WorkSpace\Pyqt5_eric6\hello_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread

# 继承QWidget
class TableWidget(QWidget):

    table_widget = None

    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        # 设置布局
        layout = QHBoxLayout()
        # 数据层次结构，10行5列
        self.table_widget = QTableWidget(5, 5)
        # 输入内容
        # for (row, customer) in enumerate(self.customer_list):
        #     for column in range(len(customer)):
        #         self.table_widget.setItem(
        #             row, column, QTableWidgetItem(
        #                 customer[column]))
        layout.addWidget(self.table_widget)

        self.botton=QPushButton(self)
        self.botton.setText('确认')
        layout.addWidget(self.botton)

        # 选择单行
        self.table_widget.setSelectionBehavior(QAbstractItemView
                                               .SelectRows)
        # # 单击事件
        # self.table_widget.cellClicked.connect(self.table_click)
        # 双击事件
        # self.table_widget.cellDoubleClicked.connect(self.double_click)

        self.setLayout(layout)

        # 内容修改
        # self.table_widget.cellChanged.connect(self.wordchange)


        # 调整窗口大小
        self.resize(700, 400)
        # 窗口居中

        # 窗口标题
        self.setWindowTitle("QTableWidget应用")
        # 显示窗口
        self.show()

    def wordchange(self):
         data=self.table_widget.currentItem()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TableWidget()
    w.show()
    sys.exit(app.exec_())