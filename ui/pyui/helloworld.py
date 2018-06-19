# -*-coding:utf-8-*-

import sys,time,os
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog,QApplication
# from ..ui_remix import Ui_Dialog
from mypyqt.ui.ui_remix import Ui_Dialog
from ethjsonrpc import EthJsonRpc

class HelloWorld(QDialog,Ui_Dialog):
    ethworker = pyqtSignal(object)

    def __init__(self):
        super(HelloWorld, self).__init__(None, Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        # self.setWindowFlags(Qt.WindowCloseButtonHint)

        # self.setWindowFlags(Qt.W)
        self.work = WorkThread()
        self.work.trigger.connect(self.hello)
        self.ethworker.connect(self.work.EthClient)
        self.button = True

    @pyqtSlot()
    def on_lianjie_clicked(self):
        if self.button:
            # self.helloworld.setText("stop")
            # self.button = False
            self.ethworker.emit(EthJsonRpc(host=self.dizhi.text(),port=443,tls=True))
            self.work.start()
        else:
            self.helloworld.setText("start")
            self.button = True
            self.work.terminate()

    @pyqtSlot(str)
    def hello(self,string):
        self.zhanshi.append(string)

    @pyqtSlot()
    def on_clear_clicked(self):
        self.zhanshi.clear()

    @pyqtSlot()
    def on_quit_clicked(self):
        self.close()

class WorkThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self):
        super(WorkThread,self).__init__()
        self.ethClient = None

    def __del__(self):
        self.wait()

    @pyqtSlot(object)
    def EthClient(self,C):
        self.ethClient = C

    def run(self):
        resp = self.ethClient.eth_blockNumber()
        print(resp)
        self.trigger.emit(str(resp))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = HelloWorld()
    dlg.show()
    app.exec_()

