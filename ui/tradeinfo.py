# -*-coding:utf-8-*-

import sys,time
# import cgitb
# cgitb.enable( format = 'text')
from PyQt5.QtCore import pyqtSlot,pyqtSignal,QThread,QObject
from PyQt5.QtWidgets import QDialog, QApplication,QMessageBox
from mypyqt.ui.pyui.ui_tradeinfo import Ui_tradeinfo
from ethjsonrpc import EthJsonRpc


class TradeInfo(QDialog, Ui_tradeinfo):
    ethClient = pyqtSignal(object)
    finishedWork = pyqtSignal()

    def __init__(self):
        super(TradeInfo, self).__init__()
        # super(Yglian, self).__init__(None, Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        self.setupUi(self)
        # self.setFixedSize(self.width(),self.height())
        # self.setWindowFlags(Qt.WindowCloseButtonHint)

        # self.setWindowFlags(Qt.W)
        self.work = WorkThreadEthConnect()
        self.thread = QThread()

        self.finishedWork.connect(self.work.Finished)
        self.ethClient.connect(self.work.EthClient)

        self.work.moveToThread(self.thread)
        self.work.finished.connect(self.thread.quit)
        self.thread.started.connect(self.work.run)

        self.work.response.connect(self.connect_show)
        self.pushButtonConnectButton = True

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
                self.textBrowserBlockNumber.clear()
            else:
                QMessageBox.warning(self,"Warning", "节点链接失败，请检查节点")
            self.ethClient.emit(self.client)
            self.thread.start()
        else:
            try:
                self.finishedWork.emit()
                self.textBrowserBlockNumber.clear()
                self.pushButtonConnectButton = True
                self.pushButtonConnect.setText("连接")
            except BaseException as e:
                print(e)
                self.pushButtonConnectButton = True
                self.textBrowserBlockNumber.clear()
                self.pushButtonConnect.setText("连接")
    def Close(self):
        self.pushButtonConnectButton = True
        self.textBrowserBlockNumber.clear()
        self.pushButtonConnect.setText("连接")

    @pyqtSlot(str)
    def connect_show(self, string):
        self.textBrowserBlockNumber.setText(string)
        if self.pushButtonConnectButton:
            self.textBrowserBlockNumber.clear()

    @pyqtSlot()
    def on_pushButtonSearch_clicked(self):
        txhash = self.lineEdit_txHash.text()
        if not self.client:
            QMessageBox.warning(self,"Warning", "请先链接节点")
            return
        if self.client and txhash:
            resp = self.client.eth_getTransactionByHash(txhash)
            if resp:
                self.label_txHash.setText(resp['hash'])
                self.label_status.setText(self.client.eth_getTransactionReceipt(txhash)['status'])
                self.label_blockTxHash.setText(resp['blockHash'])
                self.label_from.setText(resp['from'])
                self.label_to.setText(resp['to'])
                self.label_nonce.setText(str(int(resp['nonce'], 16)))
                self.textBrowser_data.setText(resp['input'])

    @pyqtSlot()
    def on_quit_clicked(self):
        self.close()


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
    dlg = TradeInfo()
    dlg.show()
    try:
        app.exec_()
    except Exception as e:
        print(e)
