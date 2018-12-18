# -*- coding: utf-8 -*-
import scrapy

from scrapy_q.book.book.items import BookItem


class KehuanSpider(scrapy.Spider):
    name = 'kehuan'
    allowed_domains = ['www.kehuan.net.cn']
    start_urls = ['http://www.kehuan.net.cn/book.html']

    def parse(self, response):
        url_list = response.xpath('//table//a/@href').extract()
        for url in url_list[::2]:
            # if url.startwith('/book'):
            yield scrapy.Request('http://www.kehuan.net.cn' + url, callback=self.book_parse1)
        print(url_list)

    def book_parse1(self, response):
        book = response.xpath('//div[contains(@class, "book")]/dl')
        for bk in book:
            name = response.xpath('//h1/text()').extract()[0]
            content_list = bk.xpath('dd/a/@href').extract()
            for content in content_list:
                url = 'http://www.kehuan.net.cn' + content
                yield scrapy.Request(url, callback=self.book_parse1)
        pass

    def content_parse(self, response):
        item = BookItem()
        content = response.xpath('div')
        yield item

    def book_parse2(self, response):
        book = response.xpath('//div[contains(@class, "book")]/dl')
        for bk in book:
            name = response.xpath('//h1/text()').extract()[0]
            content_list = bk.xpath('dd/a/@href').extract()
            for content in content_list:
                url = 'http://www.kehuan.net.cn' + content
                yield scrapy.Request(url, callback=self.book_parse2)
        pass
