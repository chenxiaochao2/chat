# coding:utf-8
import sys
from PyQt4 import QtCore, QtGui
import Chatclient
import json
from myui import register

reload(sys)
sys.setdefaultencoding( "utf-8" )


class myRegisterWin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(myRegisterWin, self).__init__()
        self.myui3 = register.Ui_Form()
        self.myui3.setupUi(self)
        self.connect(self.myui3.btn_submit, QtCore.SIGNAL('clicked()'), self.Submit)

    def Submit(self):
        self.name = str(self.myui3.line_username.text())
        self.sex = str(self.myui3.line_sex.text())
        self.PWord = str(self.myui3.line_password.text())
        self.PWord2 = str(self.myui3.line_corretp.text())

        if self.name == "":
            QtGui.QMessageBox.warning(self, u"警告！", u"用户名不能为空！", QtGui.QMessageBox.Yes)
            self.myui3.line_username.clear()
            self.myui3.line_sex.clear()
            self.myui3.line_password.clear()
            self.myui3.line_corretp.clear()
            self.myui3.line_username.setFocus()
            return
        elif self.sex != "男" and self.sex != "女":
            QtGui.QMessageBox.warning(self, u"警告！", u"性别输入错误，请重新输入！", QtGui.QMessageBox.Yes)
            self.myui3.line_sex.clear()
            self.myui3.line_sex.setFocus()
            return
        elif self.PWord == "":
            QtGui.QMessageBox.warning(self, u"警告！", u"密码不能为空！", QtGui.QMessageBox.Yes)
            self.myui3.line_password.setFocus()
            return
        elif self.PWord != self.PWord2:
            QtGui.QMessageBox.warning(self, u"警告！", u"密码不一致，请重新输入！", QtGui.QMessageBox.Yes)
            self.myui3.line_corretp.clear()
            self.myui3.line_corretp.setFocus()
            return
        else:
            body = {"flag": "register", "content": {"name": self.name, "sex": self.sex, "password": self.PWord}}
            body = json.dumps(body).encode("utf8")
            Chatclient.client_socket.sendall(body)



    def outText(self, text):
        if text == "sameUser":
            QtGui.QMessageBox.warning(self, u"警告！", u"用户名重复，请重新输入！", QtGui.QMessageBox.Yes)
            self.myui3.line_username.clear()
            self.myui3.line_username.setFocus()
        elif text == "correct":
            QtGui.QMessageBox.warning(self, u"成功！", u"恭喜您！注册成功，现在登录？", QtGui.QMessageBox.Yes)
            self.main1.close()
            self.main4.close()
            self.Loginafterregister()