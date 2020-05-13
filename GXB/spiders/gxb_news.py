# -*- coding: utf-8 -*-
import scrapy
from ..items import GxbItem


class GxbNewsSpider(scrapy.Spider):
    name = "gxb_news"
    start_urls = [
        'http://www.miit.gov.cn//n1146290//n1146402//n1146445//index.html'
    ]

    def parse(self, response):
        title = response.xpath('//dl/dt/a/@href').getall()
        title += response.xpath('//dl/dd/a/@href').getall()
        for url in title:
            newsUrl=url.replace("../../..","http://www.miit.gov.cn")
            yield scrapy.Request(url=newsUrl,callback=self.parse_url)

    def parse_url(self,response):
        newUrls = response.xpath('//div[@class="clist_con"]/ul/li/a/@href').getall()
        articlesUrl = []
        for url in newUrls:
            if '../../..' in url:
                newUrl = url.replace("../../..", "http://www.miit.gov.cn")
            elif '../..' in url:
                newUrl = url.replace("../..", "http://www.miit.gov.cn")
            else:
                newUrl = "http://www.miit.gov.cn" + url
            if newUrl not in articlesUrl:
                articlesUrl.append(newUrl)
        for article in articlesUrl:
            yield scrapy.Request(url=article,callback=self.parse_page)
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_url)


    def parse_page(self,response):
        title = response.xpath("//h1/text()").get()
        time = response.xpath('//div[@class="cinfo center"]/span[last()-1]/text()').get()
        source = response.xpath('//div[@class="cinfo center"]/span[last()]/text()').get()
        contentList = response.xpath('//div[@class="ccontent center"]/p/text()').extract()
        content = ""
        for con in contentList:
            if con != '\\xa0':
                content += con
        item = GxbItem()
        item['title'] = title
        item['time'] = time
        item['source'] = source
        item['content'] = content
        yield item



