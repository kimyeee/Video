# import requests
# import sys
#
# file = open('video.txt', 'rb').readlines()
# a, c = 0, 0
# f = open('error.txt', 'w')
# sum_count = len(file)
# for txt in file:
#     try:
#         file_list = txt.decode('gbk', errors='ignore').split('----')
#         a += 1
#         video_name = file_list[3].replace(r'\n', '').replace('?', '')
#         video_url = file_list[-1].strip()
#         add_user_index = video_name.find('@')
#         if not add_user_index == -1:
#             video_name = video_name[:add_user_index]
#         if not video_url[0] == 'h':
#             continue
#         if video_name == '...' or not video_name:
#             video_name = '没有名字' + str(a)
#         res = requests.get(video_url)
#         open(video_name + '.mp4', 'wb').write(res.content + b'####&&&&')
#         progress = int(a / sum_count * 100)
#         print('\r数量: %s/%s \t进度:%s  %s%%' % (a, sum_count, '#' * progress + ' ' * (100 - progress), progress), end='',
#               file=sys.stdout, flush=True)
#     except Exception as e:
#         f.write('error----%s----%s----%s\r' % (str(a), video_name, video_url))
#         continue
import random

import requests, bs4
import time

url = 'http://txt.vxeee.com/%s_%s/'
c = 0
for i in range(1, 5999):
    args = (str(random.randint(1, 8)), str(i))
    purl = url % args
    # purl = url % ('5', '5651')
    print(purl)
    res = requests.get(purl)
    soup = bs4.BeautifulSoup(res.content)
    if '无线小说' in soup.find('title').text:
        c += 1
        if c == 999:
            break
    # time.sleep(1)
