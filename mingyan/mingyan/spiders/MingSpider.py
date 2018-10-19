import scrapy


class MingSpider(scrapy.Spider):
    name = 'mingyan'

    start_urls = [
        'http://www.scrapyd.cn/',
    ]

    def parse(self, response):
        # mingyans = response.css('div.quote')
        #
        # for mingyan in mingyans:
        #     text = mingyan.css('.text::text').extract_first()
        #     author = mingyan.css('.author::text').extract_first()
        #     tags = mingyan.css('.tags .tag::text').extract()
        #     tags = ','.join(tags)
        #
        #     filename = '%s - 语录.txt' % author
        #     with open(filename, 'a+') as file:
        #         file.write(text)
        #         file.write('\n')
        #         file.write('标签：%s' % tags)
        #         file.write('\n')
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page)
        urls = response.css('a::attr(href)').extract()
        print(urls)
