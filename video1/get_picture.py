import re
import requests, bs4

# res = requests.get('https://detail.1688.com/offer/570686977108.html?spm=b26110380.sw1688.mof001.20.571a3808TUctkM&sk=consign')
res = open('ali.html', 'r').read()
soup = bs4.BeautifulSoup(res, 'html.parser')
imgs = soup.find_all('img')
s = 0
for img in imgs:
    s += 1
    img_url = img.get('src')
    if img_url[0] == '/':
        img_url = 'http:' + img_url
    img_file = requests.get(img_url)
    open(r'E:\SOME\Ali\\' + str(s) + '.jpg', 'wb').write(img_file.content)
    continue

imgs = re.findall('//.+jpg', res)
for img1 in imgs:
    s1 = 1
    url = img1[7:-1]

    continue
