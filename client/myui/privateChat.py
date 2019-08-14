# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'privateChat.ui'
#
# Created: Mon Jun 17 23:29:07 2019
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(934, 628)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_send = QtGui.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(490, 460, 141, 71))
        self.btn_send.setObjectName(_fromUtf8("btn_send"))
        self.btn_sure = QtGui.QPushButton(self.centralwidget)
        self.btn_sure.setGeometry(QtCore.QRect(660, 300, 93, 28))
        self.btn_sure.setObjectName(_fromUtf8("btn_sure"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(630, 0, 261, 201))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gift_notice = QtGui.QLabel(self.frame)
        self.gift_notice.setGeometry(QtCore.QRect(30, 20, 211, 31))
        self.gift_notice.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: 75 14pt \"Aharoni\";"))
        self.gift_notice.setText(_fromUtf8(""))
        self.gift_notice.setObjectName(_fromUtf8("gift_notice"))
        self.gift_show = QtGui.QLabel(self.frame)
        self.gift_show.setGeometry(QtCore.QRect(30, 80, 191, 131))
        self.gift_show.setText(_fromUtf8(""))
        self.gift_show.setObjectName(_fromUtf8("gift_show"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(660, 230, 151, 61))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.checkBox_arrow = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox_arrow.setObjectName(_fromUtf8("checkBox_arrow"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox_arrow)
        self.checkBox_flower = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox_flower.setObjectName(_fromUtf8("checkBox_flower"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkBox_flower)
        self.checkBox_beauty = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox_beauty.setObjectName(_fromUtf8("checkBox_beauty"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.checkBox_beauty)
        self.checkBox_car = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox_car.setObjectName(_fromUtf8("checkBox_car"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.checkBox_car)
        self.label_show = QtGui.QLabel(self.centralwidget)
        self.label_show.setGeometry(QtCore.QRect(30, 480, 331, 41))
        self.label_show.setText(_fromUtf8(""))
        self.label_show.setObjectName(_fromUtf8("label_show"))
        self.showname = QtGui.QLabel(self.centralwidget)
        self.showname.setGeometry(QtCore.QRect(240, 0, 151, 21))
        self.showname.setText(_fromUtf8(""))
        self.showname.setObjectName(_fromUtf8("showname"))
        self.outputArea = QtGui.QListWidget(self.centralwidget)
        self.outputArea.setGeometry(QtCore.QRect(20, 30, 611, 321))
        self.outputArea.setObjectName(_fromUtf8("outputArea"))
        self.inputArea = QtGui.QTextEdit(self.centralwidget)
        self.inputArea.setGeometry(QtCore.QRect(20, 360, 611, 87))
        self.inputArea.setObjectName(_fromUtf8("inputArea"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_send, self.checkBox_arrow)
        MainWindow.setTabOrder(self.checkBox_arrow, self.checkBox_beauty)
        MainWindow.setTabOrder(self.checkBox_beauty, self.checkBox_flower)
        MainWindow.setTabOrder(self.checkBox_flower, self.checkBox_car)
        MainWindow.setTabOrder(self.checkBox_car, self.btn_sure)
        MainWindow.setTabOrder(self.btn_sure, self.outputArea)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "畅聊", None))
        self.btn_send.setText(_translate("MainWindow", "发送", None))
        self.btn_sure.setText(_translate("MainWindow", "赠送礼物", None))
        self.checkBox_arrow.setText(_translate("MainWindow", "穿云箭", None))
        self.checkBox_flower.setText(_translate("MainWindow", "鲜花", None))
        self.checkBox_beauty.setText(_translate("MainWindow", "美女", None))
        self.checkBox_car.setText(_translate("MainWindow", "豪车", None))

