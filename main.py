# -*-coding:utf-8-*-

import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication
from ui.ui_hello import Ui_Dialog

class HelloWorld(QDialog,Ui_Dialog):

    def __init__(self):
        super(HelloWorld, self).__init__(None, Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        # self.setWindowFlags(Qt.WindowCloseButtonHint)

        # self.setWindowFlags(Qt.W)
        self.work = WorkThread()
        self.work.trigger.connect(self.hello)
        self.button = True

    @pyqtSlot()
    def on_helloworld_clicked(self):
        if self.button:
            self.helloworld.setText("stop")
            self.button = False
            self.work.start()
        else:
            self.helloworld.setText("start")
            self.button = True
            self.work.terminate()

    @pyqtSlot(str)
    def hello(self,string):
        self.textBrowser.append(string)

    @pyqtSlot()
    def on_clear_clicked(self):
        self.textBrowser.clear()

    @pyqtSlot()
    def on_quit_clicked(self):
        self.close()

class WorkThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self):
        super(WorkThread,self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(100):
            time.sleep(1)
            self.trigger.emit("test2")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = HelloWorld()
    dlg.show()
    app.exec_()

