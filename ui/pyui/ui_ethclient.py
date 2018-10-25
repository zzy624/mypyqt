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
        ethclient.resize(613, 58)
        self.gridLayout_2 = QtWidgets.QGridLayout(ethclient)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(ethclient)
        self.label.setMinimumSize(QtCore.QSize(91, 21))
        self.label.setMaximumSize(QtCore.QSize(91, 21))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_webNo = QtWidgets.QComboBox(ethclient)
        self.comboBox_webNo.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_webNo.setMaximumSize(QtCore.QSize(250, 16777215))
        self.comboBox_webNo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_webNo.setEditable(True)
        self.comboBox_webNo.setObjectName("comboBox_webNo")
        self.gridLayout.addWidget(self.comboBox_webNo, 0, 1, 1, 1)
        self.pushButtonConnect = QtWidgets.QPushButton(ethclient)
        self.pushButtonConnect.setMinimumSize(QtCore.QSize(68, 32))
        self.pushButtonConnect.setMaximumSize(QtCore.QSize(68, 32))
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.gridLayout.addWidget(self.pushButtonConnect, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(ethclient)
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_blockNumber = QtWidgets.QLabel(ethclient)
        self.label_blockNumber.setMinimumSize(QtCore.QSize(100, 20))
        self.label_blockNumber.setObjectName("label_blockNumber")
        self.gridLayout.addWidget(self.label_blockNumber, 0, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(ethclient)
        QtCore.QMetaObject.connectSlotsByName(ethclient)

    def retranslateUi(self, ethclient):
        _translate = QtCore.QCoreApplication.translate
        ethclient.setWindowTitle(_translate("ethclient", "Dialog"))
        self.label.setText(_translate("ethclient", "阳光链节点地址"))
        self.pushButtonConnect.setText(_translate("ethclient", "连接"))
        self.label_3.setText(_translate("ethclient", "区块高度"))
        self.label_blockNumber.setText(_translate("ethclient", "null"))

