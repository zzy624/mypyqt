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

class TradeInfo(QDialog, Ui_tradeinfo):
    ethClient = pyqtSignal(object)
    finishedWork = pyqtSignal()



    def __init__(self):
        super(TradeInfo, self).__init__()
        # super(Yglian, self).__init__(None, Qt.Dialog | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        self.setupUi(self)


    @pyqtSlot()
    def on_pushButtonSearch_clicked(self):
        self.pushButtonSearch.setFocus()
        host = eth.get_host()
        if host == "" or (":" not in host):
            QMessageBox.information(self, "Information", "请输入有效节点地址")
            return
        client = eth.get_ethclient(host)
        if not client:
            QMessageBox.warning(self, "Warning", "请先链接节点")
            return
        txhash = self.lineEdit_txHash.text()
        if not is_hex(txhash) or len(txhash) != 66:
            QMessageBox.warning(self, "Warning", "请输入有效的交易Hash")
            return

        if client and txhash:
            resp = client.eth_getTransactionByHash(txhash)
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
