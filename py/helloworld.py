# -*-coding:utf-8-*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,QApplication
from mypyqt.ui.helloworld import Ui_Dialog

class HelloWorld(QDialog,Ui_Dialog):

    def __init__(self):
        super(HelloWorld, self).__init__(None, Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        # self.setWindowFlags(Qt.WindowCloseButtonHint)

        # self.setWindowFlags(Qt.W)

    @pyqtSlot()
    def on_helloworld_clicked(self):
        self.textBrowser.append("Hello World")

    @pyqtSlot()
    def on_clear_clicked(self):
        self.textBrowser.clear()

    @pyqtSlot()
    def on_quit_clicked(self):
        self.window().close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = HelloWorld()
    dlg.show()
    app.exec_()

