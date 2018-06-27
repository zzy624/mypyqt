# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './skin/main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setAcceptDrops(False)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        self.file = QtWidgets.QMenu(self.menuBar)
        self.file.setObjectName("file")
        self.window = QtWidgets.QMenu(self.menuBar)
        self.window.setObjectName("window")
        self.help = QtWidgets.QMenu(self.menuBar)
        self.help.setObjectName("help")
        mainWindow.setMenuBar(self.menuBar)
        self.actionKeyStore = QtWidgets.QAction(mainWindow)
        self.actionKeyStore.setCheckable(False)
        self.actionKeyStore.setChecked(False)
        self.actionKeyStore.setEnabled(True)
        self.actionKeyStore.setObjectName("actionKeyStore")
        self.action_windowMin = QtWidgets.QAction(mainWindow)
        self.action_windowMin.setObjectName("action_windowMin")
        self.action_node = QtWidgets.QAction(mainWindow)
        self.action_node.setObjectName("action_node")
        self.action_windowMax = QtWidgets.QAction(mainWindow)
        self.action_windowMax.setObjectName("action_windowMax")
        self.file.addAction(self.actionKeyStore)
        self.window.addAction(self.action_windowMin)
        self.window.addAction(self.action_windowMax)
        self.help.addAction(self.action_node)
        self.menuBar.addAction(self.file.menuAction())
        self.menuBar.addAction(self.window.menuAction())
        self.menuBar.addAction(self.help.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "阳光链开发调试工具"))
        self.file.setTitle(_translate("mainWindow", "导入"))
        self.window.setTitle(_translate("mainWindow", "窗口"))
        self.help.setTitle(_translate("mainWindow", "帮助"))
        self.actionKeyStore.setText(_translate("mainWindow", "keyStore"))
        self.action_windowMin.setText(_translate("mainWindow", "最小化"))
        self.action_node.setText(_translate("mainWindow", "阳光链节点"))
        self.action_windowMax.setText(_translate("mainWindow", "进入全屏"))

