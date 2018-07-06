# -*-coding:utf-8-*-

import sys,time
# import cgitb
# cgitb.enable( format = 'text')
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
from mypyqt.ui.pyui.ui_ethclient import Ui_ethclient
from mypyqt.ui import tradeinfo
from mypyqt.common import eth
from ethjsonrpc import EthJsonRpc

class Ethclient(QDialog, Ui_ethclient):
    ethClient = pyqtSignal(object)
    finishedWork = pyqtSignal()
    ethClientHost = pyqtSignal(str)


    def __init__(self):
        super(Ethclient, self).__init__()
        # super(Yglian, self).__init__(None, Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        self.setupUi(self)

        self.work = WorkThreadEthConnect()
        self.thread = QThread()

        self.finishedWork.connect(self.work.Finished)
        self.ethClient.connect(self.work.EthClient)
        self.ethClientHost.connect(self.set_host)
        self.work.moveToThread(self.thread)
        self.work.finished.connect(self.thread.quit)
        self.thread.started.connect(self.work.run)

        self.work.response.connect(self.connect_show)
        self.lineEditWeb3No.setText("请输入节点")
        # self.lineEditWeb3No.focusOutEvent(,self.post_tradeinfo)
        self.lineEditWeb3No.installEventFilter(self)
        self.pushButtonConnectButton = True
        self.client = None

    @pyqtSlot()
    def on_pushButtonConnect_clicked(self):
        if self.pushButtonConnectButton:
            host = self.lineEditWeb3No.text()
            if host == "":
                QMessageBox.information(self,"Information","请输入节点地址")
                return
            self.client = eth.get_ethclient(host)
            if self.client:
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

    def get_ethclient(self):
        host = self.lineEditWeb3No.text()
        if host == "":
            return None
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
            return self.client
        else:
            QMessageBox.warning("Warning", "节点链接失败，请检查节点")

    def eventFilter(self,widget,event):
        if event.type()== QEvent.FocusIn:
            # self.inp_text_signal.emit("已进")
            if self.lineEditWeb3No.text().strip() == '请输入节点':
                self.lineEditWeb3No.clear()
            print("ok1")
        elif event.type()== QEvent.FocusOut:
            if self.lineEditWeb3No.text().strip() == '':
                self.lineEditWeb3No.setText("请输入节点")
            print("ok2")
            host = self.lineEditWeb3No.text()
            self.ethClientHost.emit(host)
        else:
            pass
        return False

    @pyqtSlot(str)
    def set_host(self,host):
        tradeinfo.set_host(host)
        # print(host)

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
        self.WorkState = False
        self.finished.emit()

    def run(self):
        while self.WorkState:
            resp = self.client.eth_blockNumber()
            self.response.emit(str(resp))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Ethclient()
    dlg.show()
    try:
        app.exec_()
    except Exception as e:
        print(e)
