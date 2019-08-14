# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addfriend.ui'
#
# Created: Thu Jun 20 17:22:45 2019
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
        Form.resize(432, 107)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.addUsername = QtGui.QLineEdit(Form)
        self.addUsername.setGeometry(QtCore.QRect(120, 20, 191, 21))
        self.addUsername.setObjectName(_fromUtf8("addUsername"))
        self.btn_searchfriend = QtGui.QPushButton(Form)
        self.btn_searchfriend.setGeometry(QtCore.QRect(320, 20, 93, 28))
        self.btn_searchfriend.setObjectName(_fromUtf8("btn_searchfriend"))
        self.show_search = QtGui.QLabel(Form)
        self.show_search.setGeometry(QtCore.QRect(120, 60, 191, 21))
        self.show_search.setText(_fromUtf8(""))
        self.show_search.setObjectName(_fromUtf8("show_search"))
        self.btn_add = QtGui.QPushButton(Form)
        self.btn_add.setGeometry(QtCore.QRect(320, 60, 93, 28))
        self.btn_add.setObjectName(_fromUtf8("btn_add"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "添加好友", None))
        self.label.setText(_translate("Form", "请输入用户名", None))
        self.btn_searchfriend.setText(_translate("Form", "搜索", None))
        self.btn_add.setText(_translate("Form", "添加", None))

