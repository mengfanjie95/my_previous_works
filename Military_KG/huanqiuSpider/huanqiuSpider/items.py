# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HuanqiuspiderItem(scrapy.Item):
    title = scrapy.Field() # 新闻标题
    summary = scrapy.Field # 新闻摘要/总结
    link = scrapy.Field # 新闻链接
    content = scra.Field # 新闻正文

