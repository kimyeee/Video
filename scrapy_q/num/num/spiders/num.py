# -*- coding: utf-8 -*-
# 文本编辑器编码要设置对，最好为UTF-8无BOM编码
import scrapy


class Num1Spider(scrapy.Spider):
    name = "num"  # 爬虫命名，在项目中有用
    allowed_domains = ["jianshu.com"]  # 允许爬取的域名
    domain = 'http://jianshu.com'  # 自己设置的基础域名变量

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    }  # 请求头
    base_url = 'http://www.jianshu.com/collections/16/notes?order_by=added_at&page=%d'
    # 关于此处url，参看新手向爬虫（一）
    num = 0  # 页数

    def start_requests(self):  # 默认的开始函数，用于提供要爬取的链接
        # url = self.base_url % self.num
        while self.num < 4000:  # 程序员专题总页数小于4000，共花费212.975027秒
            self.num += 1
            yield scrapy.Request(self.base_url % self.num,
                                 headers=self.headers,
                                 callback=self.parse)

    def parse(self, response):  # 默认的回调函数，用于链接下载完毕后调用来处理数据

        for index, i in enumerate(response.css(".title a::text").extract()):
            if "爬虫" in i or "爬取" in i:
                like = response.css("a + span::text").extract()[index].replace(' · 喜欢 ', '')
                url = self.domain + response.css('.title a::attr(href)').extract()[index]
                yield {"title": i, "like": like, "url": url}

######################## Debug ###############################
#        from scrapy.shell import inspect_response
#        inspect_response(response, self)
# 将以上两句插入回调函数中任意位置，即可在运行过程中中断打开交互命令行，用于调试查看响应内容
######################## Run   ###############################
# scrapy runspider num1.py -o 1.json
