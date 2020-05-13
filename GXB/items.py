# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GxbItem(scrapy.Item):
    ##标题
    title = scrapy.Field()
    ##时间
    time = scrapy.Field()
    ##来源
    source = scrapy.Field()
    ##正文
    content = scrapy.Field()
