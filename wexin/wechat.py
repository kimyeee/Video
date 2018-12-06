import itchat
from itchat.content import *

itchat.auto_login(hotReload=True, enableCmdQR=0)


@itchat.msg_register()
def reply(msg):
    if msg['MsgType'] == 1:
        return
