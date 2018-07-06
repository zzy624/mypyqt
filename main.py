# -*-coding:utf-8-*-

import sys
from PyQt5.QtCore import pyqtSlot,pyqtSignal,QThread,Qt,QObject
from PyQt5.QtWidgets import  QApplication,QMainWindow,QAction,qApp,QFileDialog,QMessageBox
from ethjsonrpc import EthJsonRpc
from mypyqt.ui.pyui.ui_main import Ui_mainWindow
from ui.tradeinfo import TradeInfo
from ui.permission import Permission
from ui.account import MyAccount
from ui.ethclient import Ethclient


class UIMainWindow(QMainWindow,Ui_mainWindow):
    ethClient = pyqtSignal(object)
    finishedWork = pyqtSignal()

    def __init__(self):
        super(UIMainWindow, self).__init__()
        self.setupUi(self)
        self.tabWidget.clear()
        self.account = MyAccount()
        self.tradeInfo = TradeInfo()
        self.permission = Permission()
        self.ethclient = Ethclient()
        self.addWidget(self.ethclient)
        tabs = [self.tradeInfo,self.account,self.permission]
        for t in tabs:
            self.addTabWidget(t)
        self.actionKeyStore.triggered.connect(self.OpenKeyStore)
        self.actionKeyStore.setShortcut('Ctrl+O')
        self.action_windowMin.triggered.connect(self.ShowMinimized)
        self.action_windowMin.setShortcut('Ctrl+M')
        self.action_windowMax.triggered.connect(self.ShowMaximized)
        self.action_windowMax.setShortcut('Shift+Ctrl+f')
        self.statusBar().showMessage('Go')


    def addWidget(self,widget):
        self.gridLayout_widget.addWidget(widget)
        # widget.show()

    def addTabWidget(self,Tab_widget):
        self.tabWidget.addTab(Tab_widget,Tab_widget.windowTitle())

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

