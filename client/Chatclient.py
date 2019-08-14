# coding:utf-8
import socket, sys, time
from PyQt4 import QtCore, QtGui
import json, struct, threading
from myui import login, userlist, register, mainWindow, privateChat, addfriend
from PyQt4.QtCore import *
reload(sys)
sys.setdefaultencoding( "utf-8" )

dataBuffer = bytes()
headerSize = 12
package = []               # 用来存放QThread传递的数据
aaa = ""                   # 用来存放package元素组成的字符串
members = []
friends = []

# 登录窗口
class myloginWin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(myloginWin, self).__init__()
        self.myui = login.Ui_Form()
        self.myui.setupUi(self)
        self.myui.line_user.setFocus()
        self.myui.line_password.setEchoMode(self.myui.line_password.Password)
        self.connect(self.myui.btn_login, QtCore.SIGNAL('clicked()'), self.click_login)
        self.connect(self.myui.btn_regist, QtCore.SIGNAL('clicked()'), self.click_register)
        self.setFixedSize(self.width(), self.height())
        self.myui.btn_login.setShortcut('Key_Enter')

    def outText(self, text):
        text = str(text)
        if text == "noUser":
            QtGui.QMessageBox.warning(self, u"警告", u"用户不存在！", QtGui.QMessageBox.Yes)
            self.myui.line_user.clear()
            self.myui.line_password.clear()
            self.myui.line_user.setFocus()
            return
        elif text == "relogin":
            QtGui.QMessageBox.warning(self, u"警告", u"已登录，请勿重复登录！", QtGui.QMessageBox.Yes)
            self.myui.line_user.clear()
            self.myui.line_password.clear()
            self.myui.line_user.setFocus()
            aaa = ""
            return
        elif text == "passwordError":
            QtGui.QMessageBox.warning(self, u"警告", u"密码错误！", QtGui.QMessageBox.Yes)
            self.myui.line_password.clear()
            self.myui.line_password.setFocus()
            aaa = ""
            return
        else:
            QtGui.QMessageBox.question(self, u"警告", u"成功！", QtGui.QMessageBox.Yes)
            mythread.main1.close()
            mythread.main3.show()
            # app.exec_()
            return

    def click_login(self):
        username = str(self.myui.line_user.text())
        password = str(self.myui.line_password.text())
        if username == "":
            QtGui.QMessageBox.warning(self, u"警告", u"用户名不能为空！", QtGui.QMessageBox.Yes)
        elif password == "":
            QtGui.QMessageBox.warning(self, u"警告", u"密码不能为空！", QtGui.QMessageBox.Yes)
        else:
            body = {"flag": "login", "body": {"username": username, "password": password}}
            body = json.dumps(body)
            try:
                client_socket.sendall(body)
            except:
                QtGui.QMessageBox.warning(self, u"警告", u"无法连接服务器！", QtGui.QMessageBox.Yes)

    def click_register(self):
        mythread.main4.show()



class mymainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(mymainWin, self).__init__()
        self.myui2 = mainWindow.Ui_MainWindow()
        self.myui2.setupUi(self)
        self.myui2.showname.setText(u"激情聊天室")
        self.connect(self.myui2.btn_send, QtCore.SIGNAL('clicked()'), self.send)
        self.connect(self.myui2.btn_sure, QtCore.SIGNAL('clicked()'), self.send_gift)
        self.connect(self.myui2.checkBox_flower, QtCore.SIGNAL('clicked()'), self.setstatu)
        self.connect(self.myui2.checkBox_arrow, QtCore.SIGNAL('clicked()'), self.setstatu)
        self.connect(self.myui2.checkBox_beauty, QtCore.SIGNAL('clicked()'), self.setstatu)
        self.connect(self.myui2.checkBox_car, QtCore.SIGNAL('clicked()'), self.setstatu)
        self.myui2.outputArea.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.myui2.members.itemClicked.connect(self.openPrivateWin)

    def openPrivateWin(self, item):
        name = str(item.text())
        if name:
            T = mythread
            T.creatWin()
            mythread.main5.show()
            content = {"flag": "item", "name": name}
            content = json.dumps(content)




    def setstatu(self):                               # 获取礼物选择状态
        self.gift = []
        if self.myui2.checkBox_flower.isChecked():
            self.gift.append("flower")
        if self.myui2.checkBox_arrow.isChecked():
            self.gift.append("arrow")
        if self.myui2.checkBox_beauty.isChecked():
            self.gift.append("beauty")
        if self.myui2.checkBox_car.isChecked():
            self.gift.append("car")


    def send_gift(self):
        body1 = {"flag": "Give_gift", "gifts": self.gift}             # 创建赠送礼物包
        body = json.dumps(body1).encode("utf8")
        self.myui2.checkBox_car.setChecked(False)
        self.myui2.checkBox_beauty.setChecked(False)
        self.myui2.checkBox_flower.setChecked(False)
        self.myui2.checkBox_arrow.setChecked(False)
        try:
            client_socket.sendall(body)
            QtGui.QMessageBox.question(self, u"通知", u"礼物已成功送出！", QtGui.QMessageBox.Yes)
        except:
            pass

    def send(self):
        shows = str(self.myui2.inputArea.toPlainText()).encode('utf8')
        if not shows:
            pass
        else:
            body = {"flag": "sendText", "content": shows}
            datas = json.dumps(body)

            if datas:
                try:
                    client_socket.sendall(datas)
                except:
                    pass
                data3 = json.loads(datas)["content"]
                self.myui2.outputArea.addItem(u"我：" + data3 )
                # self.myui2.outputArea.moveCursor(self.myui2.outputArea.textCursor().End)
                self.myui2.inputArea.clear()
                self.myui2.inputArea.setFocus()

    def outText(self, text):
        text = str(text)
        text = json.loads(text)
        if text["flag"] == "text":
            talk = text["content"]
            a = self.myui2.outputArea
            a.addItem(text["name"].decode() + "：" + talk.decode())
        elif text["flag"] == "welcome":
            talk = text["content"]
            a = self.myui2.outputArea
            b = self.myui2.members
            a.addItem("系统消息：" + talk.decode() + "加入聊天室")
            aaa = str(talk.decode())
            b.addItem(aaa)
        elif text["flag"] == "members":
            talk = text["content"]
            for item in talk:
                a = self.myui2.members
                a.addItem(item)
        elif text["flag"] == "gift":
            gift = text["content"]
            giftshow = self.myui2.gift_notice
            giftshowphoto = self.myui2.gift_show
            # for item in gift:
            if gift == "flower":
                giftshow.setText(u"感谢" + text["name"] + u"送来的鲜花")
                pixmap = QtGui.QPixmap("E:/Python项目/我的聊天/client/img/flower.png")
                giftshowphoto.setPixmap(pixmap)
                         # 图片自适应

            if gift == "car":
                giftshow.setText(u"感谢" + text["name"] + u"送来的豪车")
                pixmap2 = QtGui.QPixmap("/img/gift_car.png").scaled(30, 30)
                giftshowphoto.setPixmap(pixmap2)

            if gift == "arrow":
                giftshow.setText(u"感谢" + text["name"] + u"送来的穿云箭")
                pixmap3 = QtGui.QPixmap(r"E:/Python项目/我的聊天/client/img/flower.png")
                giftshowphoto.setPixmap(pixmap3)

            if gift == "beauty":
                giftshow.setText(u"感谢" + text["name"] + u"送来的美女")
                pixmap4 = QtGui.QPixmap("E:/Python项目/我的聊天/client/img/flower.png")
                giftshowphoto.setPixmap(pixmap4)

        if text["flag"] == "exit":
            talk = u"系统消息：" + text["name"].decode() + u"已下线"
            a = self.myui2.outputArea
            a.addItem(talk)
            # a.moveCursor(a.textCursor().End)

class PrivateWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(PrivateWin, self).__init__()
        self.myui5 = privateChat.Ui_MainWindow()
        self.myui5.setupUi(self)
        self.connect(self.myui5.btn_send, QtCore.SIGNAL('clicked()'), self.send)
        self.connect(self.myui5.btn_sure, QtCore.SIGNAL('clicked()'), self.send_gift)
        self.connect(self.myui5.checkBox_flower, QtCore.SIGNAL('clicked()'), self.setstatu)
        self.connect(self.myui5.checkBox_arrow, QtCore.SIGNAL('clicked()'), self.setstatu)
        self.connect(self.myui5.checkBox_beauty, QtCore.SIGNAL('clicked()'), self.setstatu)
        self.connect(self.myui5.checkBox_car, QtCore.SIGNAL('clicked()'), self.setstatu)

    def setstatu(self):                               # 获取礼物选择状态
        self.gift = []
        if self.myui5.checkBox_flower.isChecked():
            self.gift.append("flower")
        if self.myui5.checkBox_arrow.isChecked():
            self.gift.append("arrow")
        if self.myui5.checkBox_beauty.isChecked():
            self.gift.append("beauty")
        if self.myui5.checkBox_car.isChecked():
            self.gift.append("car")


    def send_gift(self):
        body1 = {"flag": "Give_gift", "gifts": self.gift}             # 创建赠送礼物包
        body = json.dumps(body1).encode("utf8")
        self.myui5.checkBox_car.setChecked(False)
        self.myui5.checkBox_beauty.setChecked(False)
        self.myui5.checkBox_flower.setChecked(False)
        self.myui5.checkBox_arrow.setChecked(False)
        try:
            client_socket.sendall(body)
            QtGui.QMessageBox.question(self, u"通知", u"礼物已成功送出！", QtGui.QMessageBox.Yes)
        except:
            pass

    def send(self):
        shows = str(self.myui5.inputArea.toPlainText()).encode('utf8')
        if not shows:
            pass
        else:
            body = {"flag": "sendText", "content": shows}
            datas = json.dumps(body)

            if datas:
                try:
                    client_socket.sendall(datas)
                except:
                    pass
                data3 = json.loads(datas)["content"]
                self.myui5.outputArea.addItem(u"我：" + data3 )
                # self.myui2.outputArea.moveCursor(self.myui2.outputArea.textCursor().End)
                self.myui5.inputArea.clear()
                self.myui5.inputArea.setFocus()

    def outText(self, text):
        text = str(text)
        text = json.loads(text)
        if text["flag"] == "text":
            talk = text["content"]
            a = self.myui5.outputArea
            a.addItem(text["name"].decode() + "：" + talk.decode())
        elif text["flag"] == "item":
            a = self.myui5.showname
            a.setText(text["name"].decode())
        elif text["flag"] == "gift":
            gift = text["content"]
            giftshow = self.myui5.gift_notice
            giftshowphoto = self.myui5.gift_show
            # for item in gift:
            if gift == "flower":
                giftshow.setText(u"感谢" + text["name"] + u"送来的鲜花")
                pixmap = QtGui.QPixmap("/img/flower.png")
                giftshowphoto.setPixmap(pixmap)
                         # 图片自适应

            if gift == "car":
                giftshow.setText(u"感谢" + text["name"] + u"送来的豪车")

            if gift == "arrow":
                giftshow.setText(u"感谢" + text["name"] + u"送来的穿云箭")

            if gift == "beauty":
                giftshow.setText(u"感谢" + text["name"] + u"送来的美女")

        if text["flag"] == "exit":
            talk = u"系统消息：" + text["name"].decode() + u"已下线"
            a = self.myui5.outputArea
            a.addItem(talk)
            # a.moveCursor(a.textCursor().End)

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
            client_socket.sendall(body)

    def outText(self, text):
        text = str(text)
        if text == "rename":
            QtGui.QMessageBox.warning(self, u"警告！", u"用户名重复，请重新输入！", QtGui.QMessageBox.Yes)
            self.myui3.line_username.clear()
            self.myui3.line_username.setFocus()
        elif text == "success":
            QtGui.QMessageBox.warning(self, u"成功！", u"恭喜您！注册成功，现在登录？", QtGui.QMessageBox.Yes)
            mythread.main4.close()



class myChatWin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(myChatWin, self).__init__()
        self.myui4 = userlist.Ui_Form()
        self.myui4.setupUi(self)
        self.connect(self.myui4.btn_Chatroom, QtCore.SIGNAL('clicked()'), self.show_Chatroom)
        self.connect(self.myui4.list_lianxiren, QtCore.SIGNAL('clicked()'), self.show_members)
        self.connect(self.myui4.btn_addFriend, QtCore.SIGNAL('clicked()'), self.addFriend)

    def addFriend(self):
        mythread.main6.show()

    def show_Chatroom(self):
        mythread.main2.show()
        # app.exec_()

    def show_members(self):
        print "wo"

    def closeEvent(self, event):                         # 截取关闭窗口事件
        res = QtGui.QMessageBox.question(self, u'info',
                                         u"你要确定退出吗？", QtGui.QMessageBox.Yes |
                                         QtGui.QMessageBox.No,
                                         QtGui.QMessageBox.No)
        if res == QtGui.QMessageBox.Yes:
            body3 = {"flag": "exit"}
            body = json.dumps(body3).encode("utf8")
            try:
                client_socket.sendall(body)
            except:
                pass
            event.accept()
        else:
            event.ignore()

    def outText(self, text):
        text = str(text)
        text = json.loads(text)
        if text["flag"] == "members":
            a = self.myui4.list_lianxiren
            member = text["content"]
            for item in member:
                a.addItem(item)
                global friends
                friends.append(item)
        elif text["flag"] == "add":
            a = self.myui4.list_lianxiren
            member = text["name"]
            a.addItem(member)
            friends.append(member)

    def fileNew(self):
        pass

class addFriend(QtGui.QWidget):
    def __init__(self, parent=None):
        super(addFriend, self).__init__()
        self.myui6 = addfriend.Ui_Form()
        self.myui6.setupUi(self)
        self.connect(self.myui6.btn_searchfriend, QtCore.SIGNAL('clicked()'), self.searchUser)
        self.connect(self.myui6.btn_add, QtCore.SIGNAL('clicked()'), self.addfriend)
        self.myui6.btn_add.setVisible(False)

    def searchUser(self):
        name = str(self.myui6.addUsername.text())
        body = {"flag": "search", "name": name}
        body = json.dumps(body).encode("utf8")
        client_socket.sendall(body)

    def addfriend(self):
        name = str(self.myui6.show_search.text())
        print friends
        if name in friends:
            QtGui.QMessageBox.warning(self, u"警告！", u"对方已经是您的好友", QtGui.QMessageBox.Yes)
        else:
            body = {"flag": "addfriend", "name": name}
            body = json.dumps(body).encode("utf8")
            client_socket.sendall(body)
            QtGui.QMessageBox.question(self, u"成功！", u"添加成功", QtGui.QMessageBox.Yes)



    def outText(self, text):
        text = str(text)
        if text == "noUser":
            self.myui6.show_search.setText(text)
        else:
            self.myui6.btn_add.setVisible(True)
            self.myui6.show_search.setText(text)

class mythread(QThread):
    sinOut1 =pyqtSignal(str)
    sinOut2 = pyqtSignal(str)
    sinOut3 = pyqtSignal(str)
    sinOut4 = pyqtSignal(str)
    sinOut5 = pyqtSignal(str)
    sinOut6 = pyqtSignal(str)
    def __init__(self):
        super(mythread, self).__init__()
        self.main1 = myloginWin()
        self.sinOut1.connect(self.main1.outText)
        self.main2 = mymainWin()
        self.sinOut2.connect(self.main2.outText)
        self.main3 = myChatWin()
        self.sinOut3.connect(self.main3.outText)
        self.main4 = myRegisterWin()
        self.sinOut4.connect(self.main4.outText)
        self.main5 = PrivateWin()
        self.sinOut5.connect(self.main5.outText)
        self.main6 = addFriend()
        self.sinOut6.connect(self.main6.outText)
        self.identity = None

    def creatWin(self):

        self.main5 = PrivateWin()
        self.sinOut5.connect(self.main5.outText)

    def dataHandle(self, headPack, body):       # 对服务器传来的数据进行相应处理
        bodys = json.loads(body)
        t = bodys["body"]
        if bodys["flag"] == "login":
            self.sinOut1.emit(t)
        elif bodys["flag"] == "mianWin":
            t = json.dumps(t)
            self.sinOut2.emit(t)
        elif bodys["flag"] == "mychat":
            t = json.dumps(t)
            self.sinOut3.emit(t)
        elif bodys["flag"] == "register":
            self.sinOut4.emit(t)
        elif bodys["flag"] == "privateWin":
            self.sinOut5.emit(t)
        elif bodys["flag"] == "searchResult":
            self.sinOut6.emit(t)

    def run(self):
        global dataBuffer
        while True:
            try:
                data = client_socket.recv(1024)
            except:
                pass
            else:
                if data:
                    # 把数据存入缓冲区，类似于push数据
                    dataBuffer += data
                    # while True:
                    if len(dataBuffer) < headerSize:
                        break

                    # 读取包头
                    # struct中:!代表Network order，3I代表3个unsigned int数据
                    headPack = struct.unpack('!3I', dataBuffer[:headerSize])
                    bodySize = headPack[1]

                    # 分包情况处理，跳出函数继续接收数据
                    if len(dataBuffer) < headerSize + bodySize:
                        break
                    # 读取消息正文的内容
                    body = dataBuffer[headerSize:headerSize + bodySize]
                    # 数据处理
                    mythread.dataHandle(headPack, body)

                    # 粘包情况的处理
                    dataBuffer = dataBuffer[headerSize + bodySize:]  # 获取下一个数据包，类似于把数据pop出



ip_port = ("127.0.0.1", 8888)
client_socket = socket.socket()
try:
    client_socket.connect(ip_port)
except:
    print "服务器异常"
app = QtGui.QApplication(sys.argv)
mythread = mythread()
mythread.start()
mythread.main1.show()
app.exec_()

