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
            return scrapy.Request('http://www.kehuan.net.cn' + url, callback=self.book_parse1)
        print(url_list)

    def book_parse1(self, response):
        book = response.xpath('//div[contains(@class, "book")]/dl')
        name = response.xpath('//h1/text()').extract()[0]
        for bk in book:
            content_list = bk.xpath('dd/a/@href').extract()
            part = bk.xpath('dt/text()').extract()[0]
            for content in content_list:
                url = 'http://www.kehuan.net.cn' + content
                item = BookItem(name=name, part=part)
                return scrapy.Request(url, callback=self.content_parse, meta={'item': item})
        pass

    def content_parse(self, response):
        item = response.meta['item']
        title = response.xpath('//h1/text()').extract()[0]

        content = response.xpath('//div[contains(@class, "text")]/p/text()')
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
