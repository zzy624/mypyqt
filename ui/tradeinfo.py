# -*-coding:utf-8-*-

import sys, time
# import cgitb
# cgitb.enable( format = 'text')
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread, QObject
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from mypyqt.ui.pyui.ui_tradeinfo import Ui_tradeinfo
from mypyqt.ui.pyui.ui_ethclient import Ui_ethclient
from mypyqt.common import eth
from eth_utils.hexadecimal import is_hex
from ethjsonrpc import EthJsonRpc


host = ""
def set_host(h):
    host = h

class TradeInfo(QDialog, Ui_tradeinfo):
    ethClient = pyqtSignal(object)
    finishedWork = pyqtSignal()



    def __init__(self):
        super(TradeInfo, self).__init__()
        # super(Yglian, self).__init__(None, Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        self.setupUi(self)
        # self.ethClient = Ethclient()
        # self.ethClient.ethClientHost.connect(self.set_host)
        # self.setFixedSize(self.width(),self.height())
        # self.setWindowFlags(Qt.WindowCloseButtonHint)
        # self.setWindowFlags(Qt.W)
        # self.work = WorkThreadEthConnect()
        # self.thread = QThread()
        self.host = ""


    @pyqtSlot()
    def on_pushButtonSearch_clicked(self):
        print(host)
        if host == "":
            QMessageBox.information(self, "Information", "请输入节点地址")
            return
        client = eth.get_ethclient(host)
        if not client:
            QMessageBox.warning(self, "Warning", "请先链接节点")
            return
        txhash = self.lineEdit_txHash.text()
        if not is_hex(txhash) or len(txhash) != 66:
            QMessageBox.warning(self, "Warning", "请输入有效的交易Hash")
            return

        if self.client and txhash:
            print(txhash)
            resp = client.eth_getTransactionByHash("0x40a2ef1ada432257e06678ff97f19c93c0794653223bd8d22e3881cf4ad064e5")
            print(resp)
            print(client.eth_blockNumber())
            if resp:
                self.label_txHash.setText(resp['hash'])
                self.label_status.setText(client.eth_getTransactionReceipt(txhash)['status'])
                self.label_blockTxHash.setText(resp['blockHash'])
                self.label_from.setText(resp['from'])
                self.label_to.setText(resp['to'])
                self.label_nonce.setText(str(int(resp['nonce'], 16)))
                self.textBrowser_data.setText(resp['input'])
                return
            else:
                QMessageBox.information(self, "Information", "无交易信息")

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
