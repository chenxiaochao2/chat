# coding:utf8
import socket, sys, time
import threading, json, struct
reload(sys)
sys.setdefaultencoding("utf-8")

sock = []
userlist = []
AllUser = []
dataBuffer = bytes()
headerSize = 12
dict2 = {}
dict = {"zhangsan": "111", "lisi": "222", "wangwu": "333", "李四": "444"}


def readyread(server_socket, adrr):
    global mysocket
    global sock
    while True:
        try:
            data = server_socket.recv(1024)
        except:
            if not mysocket:
                p = sock.index(mysocket)
                del AllUser[p]
        else:
            mysocket = server_socket
            data = json.loads(data)
            print data
            global name

            if data["flag"] == "login":
                body = data["body"]
                name = body["username"]
                dict3 = {mysocket: name}
                dict2.update(dict3)
                sendtologin(data["body"], mysocket, sock)
                continue
            if data["flag"] == "register":
                sendtologin2(data["content"])               # {"flag": "sendText", "content": shows}
                continue
            if data["flag"] == "sendText":
                sendtomainWin1(data["content"], mysocket, sock)               # {"flag": "sendText", "content": shows}
                continue
            if data["flag"] == "Give_gift":
                sendtomainWin2(data["gifts"], mysocket, sock)               # {"flag": "Give_gift", "gifts": self.gift}
                continue
            if data["flag"] == "search":
                if data["name"] in dict:
                    sendtologin3(data["name"])
                    continue
                else:
                    sendtologin3("noUser")
            if data["flag"] == "addfriend":
                    sendtologin4(data["name"])
            if data["flag"] == "exit":
                sendtomainWin3(mysocket, sock)
                try:
                    p = sock.index(mysocket)
                except:
                    pass
                else:
                    del sock[p]
                    del AllUser[p]
                    continue


# 定义发送给登录框的数据包
def sendtologin(data, mysocket1, sock1):
    password = data["password"]
    if name in AllUser:
        data = "relogin"
    elif name not in dict:
        data = "noUser"
    elif password != dict[name]:
        data = "passwordError"
    else:
        data = "success"
        AllUser.append(name)
        sock.append(mysocket)
        # global userlist
        # for user in dict:
        #     userlist.append(user)
        body2 = {"flag": "mianWin", "body": {"flag": "welcome", "content": name}}
        body3 = {"flag": "mianWin", "body": {"flag": "members", "content": AllUser}}
        body4 = {"flag": "mychat", "body": {"flag": "members", "content": AllUser}}
        body2 = json.dumps(body2)
        body3 = json.dumps(body3)
        body4 = json.dumps(body4)
        sendtoclient2(body2, mysocket1, sock1)
        sendtoclient3(body3, mysocket1, sock1)
        sendtoclient3(body4, mysocket1, sock1)
        print sock
    body = {"flag": "login", "body": data}
    body = json.dumps(body)
    sendtoclient(body)


def sendtologin2(data):
    name = data["name"]
    password = data["password"]
    if name in dict:
        data = "rename"
    else:
        data = "success"
        dict3 = {name: password}
        dict.update(dict3)
    body = {"flag": "register", "body": data}
    body = json.dumps(body)
    sendtoclient(body)

def sendtologin3(data):
    body = {"flag": "searchResult", "body": data}
    body = json.dumps(body)
    sendtoclient(body)

def sendtologin4(data):
    body = {"flag": "mychat", "body": {"flag": "add", "name": data}}
    body = json.dumps(body)
    sendtoclient(body)

# 定义发送给聊天室框的文本数据包
def sendtomainWin1(data, mysocket1, sock1):
    body = {"flag": "mianWin", "body": {"flag": "text", "content": data, "name": dict2[mysocket1]}}
    body = json.dumps(body)
    for server_socket in sock1:
        print sock1
        if server_socket != mysocket1:
            sendtoclient2(body, mysocket1, sock1)


# 定义发送给聊天室框的礼物数据包
def sendtomainWin2(data, mysocket1, sock1):
    for item in data:
        body = {"flag": "mianWin", "body": {"flag": "gift", "content": item, "name": dict2[mysocket1]}}
        body = json.dumps(body)
        for server_socket in sock1:
            print sock1
            if server_socket != mysocket1:
                    sendtoclient2(body, mysocket1, sock1)
                    time.sleep(2)
                    continue
            continue


# 定义发送给聊天室框的exit数据包
def sendtomainWin3(mysocket1, sock1):
    body = {"flag": "mianWin", "body": {"flag": "exit", "name": dict2[mysocket1]}}
    body = json.dumps(body)
    for server_socket in sock1:
        print sock1
        if server_socket != mysocket1:
            sendtoclient2(body, mysocket1, sock1)


# 定义协议包
def sendtoclient(body):
    ver = 1
    print(body)
    cmd = 101
    header = [ver, body.__len__(), cmd]
    headPack = struct.pack("!3I", *header)
    sendData = headPack + body.encode()
    server_socket.sendall(sendData)


def sendtoclient2(body, mysocket1, sock1):
    ver = 1
    print(body)

    cmd = 101
    header = [ver, body.__len__(), cmd]
    headPack = struct.pack("!3I", *header)
    sendData = headPack + body.encode()
    for server_socket in sock1:
        if server_socket != mysocket1:
            try:
                server_socket.sendall(sendData)
            except:
                pass

def sendtoclient3(body, mysocket1, sock1):
    ver = 1
    print(body)
    cmd = 101
    header = [ver, body.__len__(), cmd]
    headPack = struct.pack("!3I", *header)
    sendData = headPack + body.encode()
    for server_socket in sock1:
        if server_socket == mysocket1:
            server_socket.sendall(sendData)


sv_ipport = ('127.0.0.1', 8888)
sv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sv_socket.bind(sv_ipport)
sv_socket.listen(5)
print "启动服务器，等待客服端连接"

while True:
    server_socket, addr = sv_socket.accept()
    print "连接成功"
    t = threading.Thread(target=readyread, args=(server_socket, addr))
    t.start()