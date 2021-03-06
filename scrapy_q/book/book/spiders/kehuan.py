# -*- coding: utf-8 -*-
import os
import scrapy

from scrapy_q.book.book.items import BookItem
from scrapy_q.book.book.settings import MEDIA_ROOT


class KehuanSpider(scrapy.Spider):
    name = 'kehuan'
    allowed_domains = ['www.kehuan.net.cn']
    start_urls = ['http://www.kehuan.net.cn/book.html']

    def parse(self, response):
        url_list = response.xpath('//table//a/@href').extract()
        for url in url_list[::2]:
            # if url.startwith('/book'):
            yield scrapy.Request('http://www.kehuan.net.cn' + url, callback=self.book_parse1)

    def book_parse1(self, response):
        index = 0
        book = response.xpath('//div[contains(@class, "book")]/dl')
        name = response.xpath('//h1/text()').extract()[0]
        auther = response.xpath('//h2/a/text()').extract()[0]
        description = response.xpath('//div[contains(@class, "description")]/p/text()').extract()
        if not os.path.exists(os.path.join(MEDIA_ROOT, name)):
            os.mkdir(os.path.join(MEDIA_ROOT, name))
        f = open(r'%s\%s.%s-简介.txt' % (os.path.join(MEDIA_ROOT, name), index, name), 'w')
        f.write('书名：%s\r\n作者：%s\r\n简介：%s' % (name, auther, description[0] if description else None))
        f.close()
        if not description:
            content_list = response.xpath('//div[contains(@class, "text")]/p/text()').extract()
            file = open(r'%s\%s.txt' % (os.path.join(MEDIA_ROOT, name), name), 'w')
            file.write(name + '\r\n\r\n')
            for content in content_list:
                file.write(content + '\r\n')
            file.close()
            return

        for bk in book:
            content_list = bk.xpath('dd/a/@href').extract()
            part = bk.xpath('dt/text()').extract()[0]
            item = BookItem(name=name, part=part)

            for content in content_list:
                index += 1
                url = 'http://www.kehuan.net.cn' + content
                # return scrapy.Request(url, callback=self.content_parse2,
                #                       meta={'item': item, 'file': file})
                yield scrapy.Request(url, callback=self.content_parse,
                                     meta={'item': item, 'index': index, 'file_path': os.path.join(MEDIA_ROOT, name)})

    def content_parse(self, response):
        item = response.meta['item']
        index = response.meta['index']
        file_path = response.meta['file_path']
        title = response.xpath('//h1/text()').extract()[0]

        content_list = response.xpath('//div[contains(@class, "text")]/p/text()').extract()
        with open('%s\%s.《%s》%s-%s.txt' % (file_path, index, item['name'], item['part'], title), 'w') as file:
            file.write(title + '\r\n\r\n')
            for content in content_list:
                file.write(content + '\r\n')

    def content_parse2(self, response):
        book = response.xpath('//div[contains(@class, "book")]/dl')
        for bk in book:
            name = response.xpath('//h1/text()').extract()[0]
            content_list = bk.xpath('dd/a/@href').extract()
            for content in content_list:
                url = 'http://www.kehuan.net.cn' + content
