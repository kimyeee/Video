# -*- coding: utf-8 -*-
import scrapy


class KehuanSpider(scrapy.Spider):
    name = 'kehuan'
    allowed_domains = ['kehuan.net.cn']
    start_urls = ['http://kehuan.net.cn/']

    def parse(self, response):
        pass
