# -*-coding:utf-8-*-

import json
import os
import random
import string
import sys
import time

import bitcoin
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog
from eth_utils.hexadecimal import decode_hex
from ethereum.utils import encode_hex
from ethereum.utils import privtoaddr

# from ethereum.tools import keys
from common import keys,encoder
from mypyqt.ui.pyui.ui_account import Ui_account

class MyAccount(QDialog, Ui_account):
    setPassWordAndPrivateKey = pyqtSignal(str,str)

    def __init__(self):
        super(MyAccount, self).__init__()
        self.setupUi(self)

        self.work = WorkThreadCreateAccountKeyStore()
        self.thread = QThread()
        self.setPassWordAndPrivateKey.connect(self.work.SetPassWordAndPrivateKey)
        self.work.moveToThread(self.thread)
        self.thread.started.connect(self.work.run)
        self.work.response.connect(self.keystore_show)
        self.PubKey = ''


    @pyqtSlot()
    def on_pushButton_genAddress_clicked(self):
        passWord = self.lineEdit_pass.text()
        if not passWord:
            QMessageBox.information(self,"Warning", "请输入密码或者点击【生成密码】")
            return
        self.pushButton_genAddress.setEnabled(False)
        self.textBrowser_keyStore.clear()
        key = os.urandom(32)
        private_key = encode_hex(key)
        public_key = encode_hex(bitcoin.privkey_to_pubkey(key))
        address = '0x' + encode_hex(privtoaddr(key))
        account = {"private_key":private_key,"public_key":public_key,"address":address}
        self.account_show(account)
        self.setPassWordAndPrivateKey.emit(passWord,private_key)
        self.thread.start()

    @pyqtSlot()
    def on_pushButton_genPass_clicked(self):
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        self.lineEdit_pass.setText(salt)

    @pyqtSlot()
    def on_pushButton_copyPass_clicked(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.lineEdit_pass.text())

    @pyqtSlot()
    def on_pushButton_copyAddress_clicked(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.label_address.text())

    @pyqtSlot()
    def on_pushButton_copyPubKey_clicked(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.PubKey)

    @pyqtSlot()
    def on_pushButton_copyPrivateKey_clicked(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.label_priKey.text())

    @pyqtSlot()
    def on_pushButton_copyKeyStore_clicked(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.textBrowser_keyStore.toPlainText())

    @pyqtSlot()
    def on_pushButton_exportKeyStore_clicked(self):
        filename=QFileDialog.getSaveFileName(self,'keyStore','./' + time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()) + '-' + self.label_address.text())
        if filename[0]:
            with open(filename[0],'w') as f:
                my_text=self.textBrowser_keyStore.toPlainText()
                f.write(my_text)
        else:
            return


    def account_show(self,account):
        self.label_address.setText(account["address"])
        self.label_pubKey.setText(account["public_key"][:40] + "...")
        self.PubKey = account["public_key"]
        self.label_priKey.setText(account["private_key"])
        self.pushButton_genAddress.setEnabled(True)
        self.pushButton_copyAddress.setEnabled(True)
        self.pushButton_copyPubKey.setEnabled(True)
        self.pushButton_copyPrivateKey.setEnabled(True)

    def keystore_show(self,keystore):
        self.textBrowser_keyStore.setText(json.dumps(keystore,cls=encoder.BytesEncoder))
        self.pushButton_copyKeyStore.setEnabled(True)
        self.pushButton_exportKeyStore.setEnabled(True)
        self.thread.quit()

class WorkThreadCreateAccountKeyStore(QObject):
    response = pyqtSignal(dict)
    finished = pyqtSignal()

    def __init__(self):
        super(WorkThreadCreateAccountKeyStore, self).__init__()
        self.passWord = ""
        self.privateKey = ""

    def SetPassWordAndPrivateKey(self, pass_word,private_key):
        self.passWord = pass_word
        self.privateKey = private_key

    def quit(self):
        self.thread.quit()

    def run(self):
        keyStore = keys.make_keystore_json(decode_hex(self.privateKey), str(self.passWord))
        self.response.emit(keyStore)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MyAccount()
    dlg.show()
    try:
        app.exec_()
    except Exception as e:
        print(e)
