# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helloworld.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 137)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.quit = QtWidgets.QPushButton(Dialog)
        self.quit.setAutoFillBackground(False)
        self.quit.setCheckable(False)
        self.quit.setAutoDefault(False)
        self.quit.setObjectName("quit")
        self.gridLayout_2.addWidget(self.quit, 1, 2, 1, 1)
        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setAutoDefault(False)
        self.clear.setObjectName("clear")
        self.gridLayout_2.addWidget(self.clear, 1, 1, 1, 1)
        self.helloworld = QtWidgets.QPushButton(Dialog)
        self.helloworld.setAutoDefault(False)
        self.helloworld.setObjectName("helloworld")
        self.gridLayout_2.addWidget(self.helloworld, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setCursorWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.quit.setText(_translate("Dialog", "quit"))
        self.clear.setText(_translate("Dialog", "clear"))
        self.helloworld.setText(_translate("Dialog", "helloworld"))

