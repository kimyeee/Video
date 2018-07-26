import random
import requests
import threadpool
import time


class MyNetworkSpider:

    def __init__(self, page_num, init_url, thread_num=1, parse_device='html.parser'):
        """
        :param page_num:
        :param init_url:        初始页面
        :param thread_num:      线程数
        :param parse_device:    解析器
        """
        self.page_num = page_num
        self.init_url = init_url
        self.pool = threadpool.ThreadPool(thread_num)
        self.parse_device = parse_device

    def downloader(self, url):
        # wait_time = random.uniform(0, 4)
        # time.sleep(wait_time)
        file = requests.get(url)
        return file

    def geter(self, url):
        # print('get:', url)
        # wait_time = random.uniform(0, 5)
        # time.sleep(wait_time)
        page_html = requests.get(self.init_url)
        if url % 100 == 0:
            print(url)
        return page_html

    def poster(self, url, data):
        page_data = requests.post(url, data=data)
        return page_data

    def thread_pool(self, function, queryset):
        tasks = threadpool.makeRequests(function, queryset)
        for task in tasks:
            self.pool.putRequest(task)
        return

    def start(self, count):
        piano.thread_pool(piano.geter, list(range(count)))
        piano.pool.wait()


init_url = 'http://192.168.1.169:8888'
piano = MyNetworkSpider(151, init_url, 300)
piano.start(99999)
