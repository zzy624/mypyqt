# -*-coding:utf-8-*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QApplication,QMainWindow,QAction,qApp,QFileDialog
from mypyqt.ui.pyui.ui_main import Ui_mainWindow
from ui.tradeinfo import TradeInfo
from ui.permission import Permission
from ui.account import MyAccount


class UIMainWindow(QMainWindow,Ui_mainWindow):

    def __init__(self):
        super(UIMainWindow, self).__init__()
        self.setupUi(self)
        self.tabWidget.clear()
        self.account = MyAccount()
        self.tradeInfo = TradeInfo()
        self.permission = Permission()
        tabs = [self.account,self.tradeInfo,self.permission]
        for t in tabs:
            self.addTab(t)
        self.actionKeyStore.triggered.connect(self.OpenKeyStore)
        self.actionKeyStore.setShortcut('Ctrl+O')
        self.action_windowMin.triggered.connect(self.ShowMinimized)
        self.action_windowMin.setShortcut('Ctrl+M')
        self.action_windowMax.triggered.connect(self.ShowMaximized)
        self.action_windowMax.setShortcut('Shift+Ctrl+f')
        self.statusBar().showMessage('Go')

    def addTab(self,widget):
        self.tabWidget.addTab(widget,widget.windowTitle())

    def OpenKeyStore(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,"选取文件","./","All Files (*);;Text Files (*.txt)")
        print(fileName1, filetype)

    def ShowMinimized(self):
        self.setWindowState(Qt.WindowMinimized)
        if self.isMinimized():
            self.action_windowMin.setEnabled(False)
            self.action_windowMin.setChecked(True)
            self.action_windowMax.setEnabled(True)
            self.action_windowMax.setChecked(False)
    def ShowMaximized(self):
        self.action_windowMin.setEnabled(True)
        self.action_windowMin.setChecked(False)
        if self.isFullScreen():
            self.setWindowState(Qt.WindowNoState)
        if not self.isFullScreen():
            self.setWindowState(Qt.WindowFullScreen)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = UIMainWindow()
    dlg.show()
    app.exec_()

