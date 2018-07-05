# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './skin/ethclient.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(613, 60)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(91, 21))
        self.label.setMaximumSize(QtCore.QSize(91, 21))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditWeb3No = QtWidgets.QLineEdit(Dialog)
        self.lineEditWeb3No.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEditWeb3No.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditWeb3No.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditWeb3No.setObjectName("lineEditWeb3No")
        self.horizontalLayout.addWidget(self.lineEditWeb3No)
        self.pushButtonConnect = QtWidgets.QPushButton(Dialog)
        self.pushButtonConnect.setMinimumSize(QtCore.QSize(68, 32))
        self.pushButtonConnect.setMaximumSize(QtCore.QSize(68, 32))
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.horizontalLayout.addWidget(self.pushButtonConnect)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_blockNumber = QtWidgets.QLabel(Dialog)
        self.label_blockNumber.setMinimumSize(QtCore.QSize(100, 20))
        self.label_blockNumber.setObjectName("label_blockNumber")
        self.horizontalLayout.addWidget(self.label_blockNumber)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "阳光链节点地址"))
        self.lineEditWeb3No.setText(_translate("Dialog", "https://web3.yglian.com"))
        self.pushButtonConnect.setText(_translate("Dialog", "连接"))
        self.label_3.setText(_translate("Dialog", "区块高度"))
        self.label_blockNumber.setText(_translate("Dialog", "null"))

