# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from selenium import webdriver
from scrapy.linkextractors import LinkExtractor
import json

class Huanqiu1Spider(Spider):
    name = 'huanqiu_1'
    allowed_domains = ['mil.huanqiu.com']
    start_urls = ['https://mil.huanqiu.com/article/3wdZtOY6w2M']

    def parse(self, response):
        print("爬取新闻的标题和正文的链接")
        txt = response.xpath('/html/body/div[3]/div/div[3]/div[1]/h3/text()').get()
        print(txt)







    '''''

    def __int__(self):
        self.browser() = webdriver.Chrome()
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("spider closed")

    def start_requests(self):
        start_urls = ['https://mil.huanqiu.com/article/3wYbJbLznbv']
        yield Request(url=start_urls,callback=self.parse)

    

        
        links = response.xpath('//*[@id="recommend"]/li[1]/a/@href').extract_first()
        text = response.text
        print(text)
        print(links)
        k = 0
        for link in links:
            next_link = link.xpath('.//a/@href').get()
            print(next_link)
            k = k + 1
            if k == 10:
                break
        '''

