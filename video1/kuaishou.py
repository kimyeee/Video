import requests
import time

import sys

headers = {
    'Host': 'bdmov.a.yximgs.com',
    'Connection': 'keep - alive',
    'Cache-Control': 'max - age = 0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla / 5.0(Windows,NT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 66.0.3359.181Safari / 537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
file = open('kuai.txt', 'rb').readlines()
a, c = 0, 0
f = open('error.txt', 'w')
sum_count = len(file)
for txt in file:
    try:
        file_list = txt.decode('gbk', errors='ignore').split('----')
        a += 1
        video_name = file_list[3].replace(r'\n', '').replace('?', '')
        video_url = file_list[-1].strip()
        add_user_index = video_name.find('@')
        if not add_user_index == -1:
            video_name = video_name[:add_user_index]
        if not video_url[0] == 'h':
            continue
        if video_name == '...' or not video_name:
            video_name = '没有名字' + str(a)
        # print(video_name)
        # print(file_list[-1])
        res = requests.get(video_url, headers=headers)
        open(r'G:\video' + '\\' + video_name + '.mp4', 'wb').write(res.content + b'####&&&&')
        progress = int(a / sum_count * 100)
        print('\r数量: %s/%s \t进度:%s  %s%%' % (a, sum_count, '#' * progress + ' ' * (100 - progress), progress), end='',
              file=sys.stdout, flush=True)
    except Exception as e:
        f.write('error----%s----%s----%s\r' % (str(a), video_name, video_url))
        continue
