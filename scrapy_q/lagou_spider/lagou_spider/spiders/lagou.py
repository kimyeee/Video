# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = [
        'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        yield scrapy.FormRequest(
            url='https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false',
            formdata={
                'first': 'true',  # 这里不能给bool类型的True，requests模块中可以
                'pn': '1',  # 这里不能给int类型的1，requests模块中可以
                'kd': 'python'
            },
            callback=self.parse
        )

    def parse(self, response):
        print(response)

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
