import random

import requests
import threadpool

get_res = requests.get('http://wwb.faxya.cn/index.php')
open('wwb.html', 'wb').write(get_res.content)
headers = get_res.headers
cookies = get_res.cookies
headers1 = {
    'Host': 'www.admin333.com',
    'Connection': 'keep-alive',
    'Content-Length': '190',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://www.admin333.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://www.admin333.com/shop-2018980317.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'ASP.NET_SessionId=q2z50rign4jw112omapafg3r',
}
data = {
    'orderNO': 'KE180825460710110084',
    'productId': '198609',
    'totalCount': '10',
    'email': ' ',
    'contact': '11111111',
    'buyPassword': ' ',
    'buyRemark': ' ',
    'paymentType': '56',
    'userPaymentId': '5108079',
    'cardMoneyRule': '[]',
    'submitButton': 'btnPayOrder',
}
proxie = {
    'http': 'http://219.141.153.3'
}

cc = 1
res = requests.post('http://www.admin333.com/shop-2018980317.html', headers=headers1, data=data, proxies=proxie)


def post(c):
    while 1:
        c += 1
        print(c)
        try:
            # res = requests.post('http://www.admin333.com/shop-2018980317.html', headers=headers1, data=data,
            #                     proxies=proxie)
            a = 0
            requests.get('https://fxd2.pahys.com/health-circle/index.html?channel=weixin&source=pajk&business=friends&position=text_link&userId=43732400509#/share/2683069')

        except Exception as e:
            continue


# l = range(999999)
# pool = threadpool.ThreadPool(555)
# tasks = threadpool.makeRequests(post, list(l))
# for task in tasks:
#     pool.putRequest(task)
# pool.wait()
post(0)
