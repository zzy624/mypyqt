# -*-coding:utf-8-*-

import sys
from PyQt5.QtCore import pyqtSlot,pyqtSignal,QThread,Qt,QObject
from PyQt5.QtWidgets import  QApplication,QMainWindow,QAction,qApp,QFileDialog,QMessageBox
from ethjsonrpc import EthJsonRpc
from mypyqt.ui.pyui.ui_main import Ui_mainWindow
from ui.tradeinfo import TradeInfo
from ui.permission import Permission
from ui.account import MyAccount


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
        self.work = WorkThreadEthConnect()
        self.thread = QThread()

        self.finishedWork.connect(self.work.Finished)
        self.ethClient.connect(self.work.EthClient)

        self.work.moveToThread(self.thread)
        self.work.finished.connect(self.thread.quit)
        self.thread.started.connect(self.work.run)

        self.work.response.connect(self.connect_show)
        self.pushButtonConnectButton = True
        self.client = None

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

    @pyqtSlot()
    def on_pushButtonConnect_clicked(self):
        if self.pushButtonConnectButton:
            host = self.lineEditWeb3No.text()
            if "https" in host:
                _port = 443
                _host = host.split(':')[1].split('//')[1]
            else:
                _port = host.split(':')[2]
                _host = host.split(':')[1].split('//')[1]
            try:
                self.client = EthJsonRpc(host=_host, port=_port, tls=True)
            except Exception as e:
                QMessageBox.information(self,"Information",str(e))
                return
            if self.client.net_listening():
                self.pushButtonConnectButton = False
                self.pushButtonConnect.setText("断开")
                self.label_blockNumber.clear()
            else:
                QMessageBox.warning("Warning", "节点链接失败，请检查节点")
            self.ethClient.emit(self.client)
            self.thread.start()
        else:
            try:
                self.finishedWork.emit()
                self.label_blockNumber.clear()
                self.pushButtonConnectButton = True
                self.pushButtonConnect.setText("连接")
            except BaseException as e:
                print(e)
                self.pushButtonConnectButton = True
                self.label_blockNumber.clear()
                self.pushButtonConnect.setText("连接")

    @pyqtSlot(str)
    def connect_show(self, string):
        self.label_blockNumber.setText(string)
        if self.pushButtonConnectButton:
            self.label_blockNumber.clear()

class WorkThreadEthConnect(QObject):
    response = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self):
        super(WorkThreadEthConnect, self).__init__()
        self.client = None
        self.call = None
        self.value = ""
        self.WorkState = True


    def EthClient(self, Client):
        self.client = Client
        self.WorkState = True

    def Finished(self):
        print("Finished")
        self.WorkState = False
        self.finished.emit()

    def run(self):
        while self.WorkState:
            resp = self.client.eth_blockNumber()
            self.response.emit(str(resp))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = UIMainWindow()
    dlg.show()
    app.exec_()

