import requests
import bs4, re

# res = requests.get('https://static.youku.com/paymentcenter/vip-pc/build/js/libs/config-build.js?version=1531712125266')
# res = requests.get('https://vip.youku.com/vips/cms/235346.shtml')
# res_str = res.content.decode('utf8')
import time

res_str = open('youku1.js', 'r', encoding='utf8').read()
ret = re.search('hot_movie:.+shtml', res_str)
ret2 = re.findall('week_swing:.+shtml', res_str)
ret3 = re.findall('high_score:.+shtml', res_str)
ret4 = re.findall('dazzle:.+shtml', res_str)
ret5 = re.findall('burn:.+shtml', res_str)
# open('235346.html','wb').write(res.content)
print(ret[0])
print(ret2[0])
print(ret3[0])
print(ret4[0])
print(ret5[0])
print(ret[0][14:])
print(ret2[0][15:])
print(ret3[0][15:])
print(ret4[0][11:])
print(ret5[0][9:])
print()
sss = open('235346.html', 'r', encoding='utf8').read()
ss = eval(sss)
print(ss)
print(type(ss))


class VideoSpider:
    youku_url = 'https://static.youku.com/paymentcenter/vip-pc/build/js/libs/config-build.js?version=1531712125266'

    def get_youku(self):
        response = requests.get(self.youku_url)
        cms = response.content.decode('utf8')
        hot_movie = re.findall('hot_movie:.+shtml', cms)[0][14:]
        week_swing = re.findall('week_swing:.+shtml', cms)[0][15:]
        high_score = re.findall('high_score:.+shtml', cms)[0][15:]
        dazzle = re.findall('dazzle:.+shtml', cms)[0][11:]
        burn = re.findall('burn:.+shtml', cms)[0][9:]
        for url in [hot_movie, week_swing, high_score, dazzle, burn]:
            movie_response = requests.get(url)
            movie_dict = eval(movie_response.content.decode('utf8'))
            for movie in movie_dict:
                online_time = movie['onlinetime']
                reputation = movie['reputation']
                name = movie['showname']
                show_subtitle = movie['showsubtitle']
                thumb_url = movie['thumburl'].replace('\\', '')
                movie_url = movie['show_vurl'].replace('\\', '')
