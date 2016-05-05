# coding=utf8

import scrapy
from scrapy.http import Request, FormRequest
from scrapy.contrib.spiders import CrawlSpider

# from lagou.items import LagouItem

class LagouSpider(CrawlSpider):
    name = "example"
    allowed_domains = ['example.com']
    start_urls = [
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        # 'http://www.example.com/1.html',
        # 'http://www.example.com/2.html',
        # 'http://www.example.com/3.html',
    ]


    def parse(self, response):
        # import time
        # with open("page_{0}".format(time.time()), "wb") as fp:
        #     fp.write(response)
        #
        # print "****"
        # yield scrapy.Request("http://www.taobao.com", callback=self.parse)

        sel = scrapy.Selector(response)
        for h3 in response.xpath('//title').extract():
            print h3
            # print "*** {0} ".format(h3)

        for url in response.xpath('//a/@href').extract():
            print url
            #yield scrapy.Request(url, callback=self.parse)
        yield scrapy.Request("http://tieba.baidu.com", callback=self.parse)