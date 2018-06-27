# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication, \
    QPropertyAnimation
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QPushButton, \
    QApplication, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 681)
        MainWindow.setMinimumSize(QtCore.QSize(0, 651))
        MainWindow.setStyleSheet("background-image: url(:/新前缀/backpic.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -580, 195, 631))
        self.widget.setObjectName("widget")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 195, 581))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 178, 681))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(177, 681))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -10, 181, 691))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setGeometry(QtCore.QRect(50, 580, 61, 32))
        self.closeButton.setStyleSheet("border-image: url(:/新前缀/v.png);")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(50, 0, 61, 32))
        self.openButton.setStyleSheet("border-image: url(:/新前缀/xia.png);")
        self.openButton.setText("")
        self.openButton.setObjectName("openButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 801, 641))
        self.graphicsView.setObjectName("graphicsView")
        self.widget.raise_()
        self.graphicsView.raise_()
        self.openButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "人脑架构分析"))

        self.action.setText(_translate("MainWindow", "导入矩阵"))
        self.action_2.setText(_translate("MainWindow", "退出系统"))
        self.action_3.setText(_translate("MainWindow", "开发者信息"))


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)


        self.setupUi(self)
        self.outani = QPropertyAnimation(self.widget, b"geometry")  # 背后隐藏的控件
        self.outani.setDuration(1000)  # 1s
        self.outani.setEndValue(QRect(0, 30, 178, 681))  # 只是x坐标变化

        # 移进去动画
        self.inani = QPropertyAnimation(self.widget, b"geometry")  # 背后隐藏的控件
        self.inani.setDuration(1000)  # 1s
        self.inani.setEndValue(QRect(0, -580, 178, 681))
        self.inani.finished.connect(self.onFinish)

        # 绑定打开关闭事件
        self.openButton.clicked.connect(self.onOpen)
        self.closeButton.clicked.connect(self.onClose)

        #打开文件
        self.action.triggered.connect(self.openFile)
        self.action.setStatusTip('导入矩阵')
        self.action.setShortcut('Ctrl+Q')

        #退出系统
        self.action_2.triggered.connect(self.close)
        self.action_2.setStatusTip('退出系统')
        self.action_2.setShortcut('Ctrl+E')

        #开发者信息
        self.action_3.setStatusTip('唐伟泽 谢家柯 2016.12.3')

    def onOpen(self):
        # 设置按钮不可见
        self.openButton.setVisible(False)
        self.widget.setVisible(True)  # 背后的待拉出来的控件可见
        self.graphicsView.setGeometry(QtCore.QRect(195, 1, 611, 641))
        self.outani.start()  # 开启动画效果

    def onClose(self):
        self.outani.stop()  # 如果移动到一半则停止
        self.inani.start()  # 退回去

    def onFinish(self):  # 关闭动画结束
        self.widget.setVisible(False)
        self.openButton.setVisible(True)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 801, 641))

    def openFile(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,"选取文件","/Users/Kelisiya/Desktop","All Files (*);;Text Files (*.txt)")
        print(fileName1, filetype)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

