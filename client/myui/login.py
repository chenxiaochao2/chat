# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sat Jun 15 21:33:02 2019
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
        Form.resize(400, 300)
        self.btn_login = QtGui.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(140, 210, 61, 28))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.btn_regist = QtGui.QPushButton(Form)
        self.btn_regist.setGeometry(QtCore.QRect(260, 210, 61, 28))
        self.btn_regist.setObjectName(_fromUtf8("btn_regist"))
        self.line_user = QtGui.QLineEdit(Form)
        self.line_user.setGeometry(QtCore.QRect(140, 40, 191, 31))
        self.line_user.setObjectName(_fromUtf8("line_user"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_password = QtGui.QLineEdit(Form)
        self.line_password.setGeometry(QtCore.QRect(140, 130, 191, 31))
        self.line_password.setObjectName(_fromUtf8("line_password"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "登录", None))
        self.btn_login.setText(_translate("Form", "登录", None))
        self.btn_regist.setText(_translate("Form", "注册", None))
        self.label.setText(_translate("Form", "用户名", None))
        self.label_2.setText(_translate("Form", "密码", None))

