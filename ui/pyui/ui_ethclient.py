# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './skin/ethclient.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ethclient(object):
    def setupUi(self, ethclient):
        ethclient.setObjectName("ethclient")
        ethclient.resize(613, 60)
        self.gridLayout = QtWidgets.QGridLayout(ethclient)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ethclient)
        self.label.setMinimumSize(QtCore.QSize(91, 21))
        self.label.setMaximumSize(QtCore.QSize(91, 21))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditWeb3No = QtWidgets.QLineEdit(ethclient)
        self.lineEditWeb3No.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEditWeb3No.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditWeb3No.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEditWeb3No.setText("")
        self.lineEditWeb3No.setObjectName("lineEditWeb3No")
        self.horizontalLayout.addWidget(self.lineEditWeb3No)
        self.pushButtonConnect = QtWidgets.QPushButton(ethclient)
        self.pushButtonConnect.setMinimumSize(QtCore.QSize(68, 32))
        self.pushButtonConnect.setMaximumSize(QtCore.QSize(68, 32))
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.horizontalLayout.addWidget(self.pushButtonConnect)
        self.label_3 = QtWidgets.QLabel(ethclient)
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_blockNumber = QtWidgets.QLabel(ethclient)
        self.label_blockNumber.setMinimumSize(QtCore.QSize(100, 20))
        self.label_blockNumber.setObjectName("label_blockNumber")
        self.horizontalLayout.addWidget(self.label_blockNumber)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(ethclient)
        QtCore.QMetaObject.connectSlotsByName(ethclient)

    def retranslateUi(self, ethclient):
        _translate = QtCore.QCoreApplication.translate
        ethclient.setWindowTitle(_translate("ethclient", "Dialog"))
        self.label.setText(_translate("ethclient", "阳光链节点地址"))
        self.pushButtonConnect.setText(_translate("ethclient", "连接"))
        self.label_3.setText(_translate("ethclient", "区块高度"))
        self.label_blockNumber.setText(_translate("ethclient", "null"))

