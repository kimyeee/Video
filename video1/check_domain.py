import requests
import time

url = 'https://my.fastcomet.com/domainchecker.php?search=single'
headers = {
    'Cookie': '__cfduid=d29292bdb1fe9a4940908e57e666e85131540798909; _ga=GA1.2.979470130.1540798912; _gid=GA1.2.555137036.1540798912; __zlcmid=p7hkf6AOBLpxd7; fc_cookie_consent=agreed; _ceg.s=phe5i5; _ceg.u=phe5i5; WHMCSfEEFlk7rYvp2=b64e419a8ce773b87e715a6ecf5fc77c',
    'Host': 'my.fastcomet.com',
    'Origin': 'https://my.fastcomet.com',
    'Referer': 'https://my.fastcomet.com/domainchecker.php?search=single&type=first&domain=880ys',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}

for i in range(999):
    data = {
        'domain': '%sys' % str(i),
        'tld': '.com',
        'isMainDomain': '1'
    }
    res = requests.post(url=url, headers=headers, json=data)
    text = eval(res.text)
    if text['status'] == 'available':
        print("==" * 66)
        print(data['domin'] + data['tld'])
    print(data['domain'] + data['tld'])

    # time.sleep(2)
