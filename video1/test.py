import os
import requests
# res = requests.get('https://code.jquery.com/jquery-3.3.1.min.js')
# open(r'C:\Users\admin\PycharmProjects\Video\static\js\jquery-3.3.1.min.js','wb').write(res.content)
#
# ss = [{"showname":"\u76d1\u72f1\u72ac\u8ba1\u5212","showsubtitle":"\u90dd\u857e\u8054\u624b\"\u9a74\u5f97\u6c34\"\u8bad\u840c\u72ac","thumburl":"http:\/\/r1.ykimg.com\/051600005B2E18E508B80DE47F05752B","onlinetime":"2018-06-24","online_status":false,"show_vurl":"http:\/\/v.youku.com\/v_show\/id_XMzY4MTk4MzA0NA==.html","iku_vurl":"iku:\/\/|play|buildin|videoid|origin|XMzY4MTk4MzA0NA==|fid=|","reputation":"7.100","fee_type":1,"fee_desc":"\u4f1a\u5458\u514d\u8d39"},{"showname":"\u73af\u592a\u5e73\u6d0b\uff1a\u96f7\u9706\u518d\u8d77","showsubtitle":"\u673a\u7532\u9738\u6c14\u5f52\u6765\u5bf9\u6297\u5de8\u517d","thumburl":"http:\/\/r1.ykimg.com\/051600005A7BADCCADBA1F26C302AC81","onlinetime":"2018-06-23","online_status":false,"show_vurl":"http:\/\/v.youku.com\/v_show\/id_XMzY0NzIwODI3Ng==.html","iku_vurl":"iku:\/\/|play|buildin|videoid|origin|XMzY0NzIwODI3Ng==|fid=|","reputation":"8.100","fee_type":1,"fee_desc":"\u4f1a\u5458\u514d\u8d39"},{"showname":"\u540e\u6765\u7684\u6211\u4eec","showsubtitle":"\u5468\u51ac\u96e8\u4e95\u67cf\u7136\u5341\u5e74\u8650\u604b","thumburl":"http:\/\/r1.ykimg.com\/051600005ADD4934859B5E03FD0C9179","onlinetime":"2018-06-22","online_status":false,"show_vurl":"http:\/\/v.youku.com\/v_show\/id_XMzY3NTIxMjgwOA==.html","iku_vurl":"iku:\/\/|play|buildin|videoid|origin|XMzY3NTIxMjgwOA==|fid=|","reputation":"8.200","fee_type":1,"fee_desc":"\u4f1a\u5458\u514d\u8d39"},{"showname":"\u53e4\u5893\u4e3d\u5f71\uff1a\u6e90\u8d77\u4e4b\u6218","showsubtitle":"\u574e\u59b9\u5434\u5f66\u7956\u71c3\u7206\u63a2\u53e4\u5893","thumburl":"http:\/\/r1.ykimg.com\/051600005A780CAFADBC096CC50DA77F","onlinetime":"2018-06-16","online_status":false,"show_vurl":"http:\/\/v.youku.com\/v_show\/id_XMzY2MjA4MTkwNA==.html","iku_vurl":"iku:\/\/|play|buildin|videoid|origin|XMzY2MjA4MTkwNA==|fid=|","reputation":"8.100","fee_type":1,"fee_desc":"\u4f1a\u5458\u514d\u8d39"},{"showname":"\u4f4e\u538b\u69fd\uff1a\u6b32\u671b\u4e4b\u57ce","showsubtitle":"\u5f20\u5bb6\u8f89\u5f90\u9759\u857e\u6b63\u90aa\u5bf9\u5cd9","thumburl":"http:\/\/r1.ykimg.com\/051600005AB1F7B4859B5D06CA00BA23","onlinetime":"2018-06-13","online_status":false,"show_vurl":"http:\/\/v.youku.com\/v_show\/id_XMzY1ODIyODA4OA==.html","iku_vurl":"iku:\/\/|play|buildin|videoid|origin|XMzY1ODIyODA4OA==|fid=|","reputation":"7.700","fee_type":1,"fee_desc":"\u4f1a\u5458\u514d\u8d39"},{"showname":"\u6e6e\u706d","showsubtitle":"\u70ed\u8840\u6562\u6b7b\u961f\u95ef\u7981\u533a\u68ee\u6797","thumburl":"http:\/\/r1.ykimg.com\/051600005AB1CD18859B5C05CE020179","onlinetime":"2018-06-06","online_status":false,"show_vurl":"http:\/\/v.youku.com\/v_show\/id_XMzY0NTI1ODI4OA==.html","iku_vurl":"iku:\/\/|play|buildin|videoid|origin|XMzY0NTI1ODI4OA==|fid=|","reputation":"7.900","fee_type":1,"fee_desc":"\u4f1a\u5458\u514d\u8d39"},{"showname":"\u5df4\u970d\u5df4\u5229\u738b2\uff1a\u7ec8\u7ed3","showsubtitle":"\u5370\u5ea6\u738b\u5b50\u590d\u4ec7\u4e89\u593a\u738b\u4f4d","thumburl":"http:\/\/r1.ykimg.com\/051600005B14ED91ADBAC3873306784F","onlinetime":"2018-06-05","online_status":false,"show_vurl":"http:\/\/v.youku.com\/v_show\/id_XMzYzOTUwNzE5Ng==.html","iku_vurl":"iku:\/\/|play|buildin|videoid|origin|XMzYzOTUwNzE5Ng==|fid=|","reputation":"7.900","fee_type":1,"fee_desc":"\u4f1a\u5458\u514d\u8d39"},{"showname":"\u593a\u547d\u6765\u7535","showsubtitle":"\u624b\u673a\u58f0\u6ce2\u8bf1\u53d1\u60ca\u609a\u53d8\u5f02","thumburl":"http:\/\/r1.ykimg.com\/051600005ABC7540AD881A05B9064326","onlinetime":"2018-06-04","online_status":false,"show_vurl":"http:\/\/v.youku.com\/v_show\/id_XMzY0MjQ3MzkwOA==.html","iku_vurl":"iku:\/\/|play|buildin|videoid|origin|XMzY0MjQ3MzkwOA==|fid=|","reputation":"6.400","fee_type":1,"fee_desc":"\u4f1a\u5458\u514d\u8d39"}]
# s = requests.get('https://detail.1688.com/offer/570686977108.html?spm=b26110380.sw1688.mof001.20.571a3808TUctkM&sk=consign')
# open(r'ali.html','wb').write(s.content)
# s = requests.get('http://ncy.bxbgsc.com/ksspcjq.zip')
# open(r'ksspcjq.zip','wb').write(s.content)
import sys
import sys
import time

total_size = 10212
recv_size = 0


def progress(percent, width=50):
    if percent > 1:  # 如果百分比大于1的话则取1
        percent = 1
    show_str = ('[%%-%ds]' % width) % (int(percent * width) * '#')
    # 一共50个#，%d 无符号整型数,-代表左对齐，不换行输出，两个% % 代表一个单纯的%，对应的是后面的s，后面为控制#号的个数
    # print(show_str)  #[###############               ] show_str ，每次都输出一次
    print('\r%s %s%%' % (show_str, int(percent * 100)), end='', file=sys.stdout, flush=True)
    # \r 代表调到行首的意思，\n为换行的意思，fiel代表输出到哪，flush=True代表无延迟，立马刷新。第二个%s是百分比


while recv_size < total_size:  # 当接收的大小小于总大小时
    time.sleep(0.2)  # 1024
    recv_size += 1024  # 每次接收1024
    percent = recv_size / total_size  # 计算百分比 0.10027418723070897
    progress(percent, width=30)  # 调用进度条函数，将百分比传进去
for i in range(3333):
    s = i / 3333 * 100
    print('\r%s  %s%%' % ('#' * int(s) + '_' * (100 - int(s)), int(s)), end='', file=sys.stdout, flush=True)
    time.sleep(0.001)
# print('\r%s  %s%%' % ('#' * 100, 100), end='', file=sys.stdout, flush=True)

d = {1: 3, 3: 4}
print()