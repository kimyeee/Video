# -*- coding: utf-8 -*-
import bs4
import requests
import scrapy
import time

from scrapy_q.santi.santi.items import SantiItem


class TianyashukuSpider(scrapy.Spider):
    name = 'tianyashuku'
    allowed_domains = ['tianyashuku.com']
    start_urls = ['http://www.tianyashuku.com/kehuan/1440/']
    file = open('三体.txt', 'w')

    def parse(self, response):
        url_list = response.xpath('//li/a')
        index = 0
        for url in url_list:
            # title = url.xpath('text()')[0].extract()
            content_url = url.xpath('@href')[0].extract()
            # yield scrapy.Request(url='http://www.tianyashuku.com' + content_url, callback=self.content_parse)
            res = requests.get('http://www.tianyashuku.com' + content_url)
            soup = bs4.BeautifulSoup(res.content)
            title = soup.find('h1', class_='h11').text
            self.file.write(title + '\r\n\r\n')
            content = soup.find('div', class_='articleContent').text
            for i in content.split('\u3000\u3000')[1:]:
                print(i)
                self.file.write(i + '\r\n')
            self.file.write('\r\n\r\n')
            # return

    def content_parse(self, response):
        content = response.xpath('//div[contains(@class, "articleContent")]/text()')
        title = response.xpath('//h1[contains(@class, "h11")]/text()').extract()[0]
        string = ''
        for cont in content:
            string += cont.extract().strip() + '\r\n'
        # item = SantiItem(title=title, content='\r\n\r\n' + string)
        self.file.write(title + string + '\r\n\r\n')
        # return item
