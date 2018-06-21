# -*-coding:utf-8-*-

import sys, time, os
import json
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QApplication
# from ..ui_remix import Ui_Dialog
from mypyqt.ui.ui_yglian import Ui_yglian
from ..ui_yglian import Ui_yglian
from ethjsonrpc import EthJsonRpc


class Yglian(QDialog, Ui_yglian):
    ethClient = pyqtSignal(object)
    call = pyqtSignal(str, str)

    def __init__(self):
        super(Yglian, self).__init__()
        # super(Yglian, self).__init__(None, Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        self.setupUi(self)
        # self.setFixedSize(self.width(),self.height())
        # self.setWindowFlags(Qt.WindowCloseButtonHint)

        # self.setWindowFlags(Qt.W)
        self.work = WorkThread()
        self.work.response.connect(self.connect_show)
        self.ethClient.connect(self.work.EthClient)
        self.call.connect(self.work.Call)
        self.pushButtonConnectbutton = True
        self.client = None

    @pyqtSlot()
    def on_pushButtonConnect_clicked(self):
        if self.pushButtonConnectbutton:
            host = self.lineEditWeb3No.text()
            if "https" in host:
                _port = 443
                _host = host.split(':')[1].split('//')[1]
            else:
                _port = host.split(':')[2]
                _host = host.split(':')[1].split('//')[1]
            self.client = EthJsonRpc(host=_host, port=_port, tls=True)
            self.ethClient.emit(self.client)
            self.work.start()
        else:
            try:
                self.work.terminate()
                self.pushButtonConnectbutton = True
                self.textBrowserBlockNumber.clear()
                self.pushButtonConnect.setText("连接")
            except BaseException as e:
                print(e)
                self.pushButtonConnectbutton = True
                self.textBrowserBlockNumber.clear()
                self.pushButtonConnect.setText("连接")

    @pyqtSlot(str)
    def connect_show(self, string):
        self.textBrowserBlockNumber.setText(string)
        if string:
            self.pushButtonConnectbutton = False
            self.pushButtonConnect.setText("断开")

    @pyqtSlot()
    def on_pushButtonSearch_clicked(self):
        txhash = self.lineEditTxHash.text()
        if self.client and txhash:
            resp = self.client.eth_getTransactionByHash(txhash)
            # print(resp)
            if resp:
                self.textBrowserTxHash.setText(resp['hash'])
                self.textBrowserStatus.setText(self.client.eth_getTransactionReceipt(txhash)['status'])
                self.textBrowserBlockHash.setText(resp['blockHash'])
                self.textBrowserForm.setText(resp['from'])
                self.textBrowserTo.setText(resp['to'])
                self.textBrowserNonce.setText(str(int(resp['nonce'], 16)))
                self.textBrowserData.setText(resp['input'])

    @pyqtSlot()
    def on_quit_clicked(self):
        self.close()


class WorkThread(QThread):
    response = pyqtSignal(str)

    def __init__(self):
        super(WorkThread, self).__init__()
        self.ethClient = None
        self.call = None
        self.value = ""

    def __del__(self):
        self.wait()

    @pyqtSlot(object)
    def EthClient(self, Client):
        self.ethClient = Client

    @pyqtSlot(str, str)
    def Call(self, call, value):
        self.call = call
        self.value = value

    def run(self):
        while True:
            resp = self.ethClient.eth_blockNumber()
            self.response.emit(str(resp))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Yglian()
    dlg.show()
    app.exec_()
