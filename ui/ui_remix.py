# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './skin/remix.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(644, 522)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dizhi = QtWidgets.QLineEdit(Dialog)
        self.dizhi.setObjectName("dizhi")
        self.gridLayout.addWidget(self.dizhi, 0, 1, 1, 1)
        self.lianjie = QtWidgets.QPushButton(Dialog)
        self.lianjie.setObjectName("lianjie")
        self.gridLayout.addWidget(self.lianjie, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dizhi_2 = QtWidgets.QLineEdit(Dialog)
        self.dizhi_2.setObjectName("dizhi_2")
        self.gridLayout.addWidget(self.dizhi_2, 1, 1, 1, 1)
        self.chaxun = QtWidgets.QPushButton(Dialog)
        self.chaxun.setObjectName("chaxun")
        self.gridLayout.addWidget(self.chaxun, 1, 2, 1, 1)
        self.zhanshi = QtWidgets.QTextBrowser(Dialog)
        self.zhanshi.setObjectName("zhanshi")
        self.gridLayout.addWidget(self.zhanshi, 2, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "web3No"))
        self.lianjie.setText(_translate("Dialog", "连接"))
        self.label_2.setText(_translate("Dialog", "TxHash"))
        self.chaxun.setText(_translate("Dialog", "查询"))

