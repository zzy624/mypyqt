# -*-coding:utf-8-*-

import sys,time
# import cgitb
# cgitb.enable( format = 'text')
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
from mypyqt.ui.pyui.ui_permission import Ui_permission
from ethjsonrpc import EthJsonRpc


class Permission(QDialog, Ui_permission):
    ethClient = pyqtSignal(object)
    finishedWork = pyqtSignal()

    def __init__(self):
        super(Permission, self).__init__()
        # super(Yglian, self).__init__(None, Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Permission()
    dlg.show()
    try:
        app.exec_()
    except Exception as e:
        print(e)
