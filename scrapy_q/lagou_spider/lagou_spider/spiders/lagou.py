# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.cookies import CookieJar
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    url_list = []
    start = [
        'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false'
    ]

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        browser.get("https://www.lagou.com")
        browser.get("https://www.lagou.com/jobs/list_Python?px=new&city=%E6%AD%A6%E6%B1%89#order")

        ii = browser.find_elements(By.CLASS_NAME, 'position_link')
        for i in ii:
            url = i.get_attribute('href')
            self.url_list.append(url)
            yield self.parse(url)


    def parse(self, url):
        print(url)

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
