# -*-coding:utf-8-*-

import sys

from PyQt5.QtWidgets import QApplication

from mypyqt.ui.yglian import Yglian


class MainWindow(Yglian):

    def __init__(self):
        super(MainWindow, self).__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    app.exec_()

