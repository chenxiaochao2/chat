# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created: Mon Jun 17 16:27:20 2019
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
        self.btn_submit = QtGui.QPushButton(Form)
        self.btn_submit.setGeometry(QtCore.QRect(130, 240, 61, 31))
        self.btn_submit.setObjectName(_fromUtf8("btn_submit"))
        self.btn_cancel = QtGui.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(230, 240, 61, 31))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_username = QtGui.QLineEdit(Form)
        self.line_username.setGeometry(QtCore.QRect(130, 40, 181, 31))
        self.line_username.setObjectName(_fromUtf8("line_username"))
        self.line_sex = QtGui.QLineEdit(Form)
        self.line_sex.setGeometry(QtCore.QRect(130, 90, 181, 31))
        self.line_sex.setObjectName(_fromUtf8("line_sex"))
        self.line_password = QtGui.QLineEdit(Form)
        self.line_password.setGeometry(QtCore.QRect(130, 140, 181, 31))
        self.line_password.setObjectName(_fromUtf8("line_password"))
        self.line_corretp = QtGui.QLineEdit(Form)
        self.line_corretp.setGeometry(QtCore.QRect(130, 190, 181, 31))
        self.line_corretp.setObjectName(_fromUtf8("line_corretp"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 72, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 72, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "注册窗口", None))
        self.btn_submit.setText(_translate("Form", "确定", None))
        self.btn_cancel.setText(_translate("Form", "取消", None))
        self.label.setText(_translate("Form", "用户名", None))
        self.label_2.setText(_translate("Form", "性别", None))
        self.label_3.setText(_translate("Form", "密码", None))
        self.label_4.setText(_translate("Form", "确认密码", None))

