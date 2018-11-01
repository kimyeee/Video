import requests
import time, bs4

# url = 'https://my.fastcomet.com/domainchecker.php?search=single'
url = 'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=%s'
headers = {
    'Cookie': '__cfduid=d29292bdb1fe9a4940908e57e666e85131540798909; _ga=GA1.2.979470130.1540798912; _gid=GA1.2.555137036.1540798912; __zlcmid=p7hkf6AOBLpxd7; fc_cookie_consent=agreed; _ceg.s=phe5i5; _ceg.u=phe5i5; WHMCSfEEFlk7rYvp2=b64e419a8ce773b87e715a6ecf5fc77c',
    'Host': 'my.fastcomet.com',
    'Origin': 'https://my.fastcomet.com',
    'Referer': 'https://my.fastcomet.com/domainchecker.php?search=single&type=first&domain=880ys',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
registered_list = []
unregistered_list = []
for i in range(130000, 140000):
    domain = str(i) + '.com'
    res = requests.get(url % str(domain))
    soup = bs4.BeautifulSoup(res.content)
    if soup.find('returncode').text == '200':
        if soup.find('original').text[0:3] == '210':
            unregistered_list.append(domain)
        #     print('__未注册__')
        # else:
        #     registered_list.append(domain)
        # print(domain)

with open('unregistered2.txt', 'a') as f:
    c = 0
    for d in unregistered_list:
        if c % 5 == 0:
            f.write('\n')
        f.write(d + '\t')
        c += 1

print('已注册：')
print(registered_list)
print('未注册：')
print(unregistered_list)
