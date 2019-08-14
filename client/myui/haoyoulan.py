# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'haoyoulan.ui'
#
# Created: Tue Jun 11 19:37:01 2019
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(257, 543)
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, -40, 321, 161))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 311, 661))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Chatroom = QtGui.QWidget()
        self.Chatroom.setObjectName(_fromUtf8("Chatroom"))
        self.btn_Chatroom = QtGui.QPushButton(self.Chatroom)
        self.btn_Chatroom.setGeometry(QtCore.QRect(0, 0, 251, 51))
        self.btn_Chatroom.setObjectName(_fromUtf8("btn_Chatroom"))
        self.tabWidget.addTab(self.Chatroom, _fromUtf8(""))
        self.members = QtGui.QWidget()
        self.members.setObjectName(_fromUtf8("members"))
        self.list_lianxiren = QtGui.QListWidget(self.members)
        self.list_lianxiren.setGeometry(QtCore.QRect(0, 0, 256, 521))
        self.list_lianxiren.setObjectName(_fromUtf8("list_lianxiren"))
        self.tabWidget.addTab(self.members, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_Chatroom.setText(_translate("Form", "激情聊天室", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Chatroom), _translate("Form", "群聊", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.members), _translate("Form", "联系人", None))

