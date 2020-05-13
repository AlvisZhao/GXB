# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
#-*- coding:utf-8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import choice


class GxbSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class SeleniumMiddleware(object):
    def process_request(self,request,spider):
        print("翻页中间件被调用")
        click_page_url = ["http://www.miit.gov.cn/n1146290/n1146392/index.html",
                          "http://www.miit.gov.cn/n1146290/n1146402/n7039597/index.html",
                          "http://www.miit.gov.cn/n1146290/n1146402/n1146440/index.html",
                          "http://www.miit.gov.cn/n1146290/n1146402/n1146450/index.html",
                          "http://www.miit.gov.cn/n1146290/n1146402/n1146445/index.html",
                          "http://www.miit.gov.cn/n1146290/n1146407/index.html",
                          "http://www.miit.gov.cn/n1146290/n1718621/index.html",
                          "http://www.miit.gov.cn/n1146290/n4337866/index.html"]
        for click_url in click_page_url:
            if request.url == click_url:
                driver = webdriver.PhantomJS()
                try:
                    driver.get(request.url)
                    driver.implicitly_wait(3)
                    time.sleep(5)

                    look_more = ".//td[@id='pag_5790085']/a[contains(text(), '下页')]"
                    # for n in range(4):
                    #     driver.find_element_by_xpath(look_more).click()  # 数据由js来控制,点击后加载数据
                    #     time.sleep(5)
                    while(True):
                        if not look_more:
                            driver.find_element_by_xpath(look_more).click()  # 数据由js来控制,点击后加载数据
                            time.sleep(5)
                        else:
                            break

                    true_page = driver.page_source
                    driver.close()

                    return HtmlResponse(request.url, body=true_page, encoding='utf-8', request=request, )

                except:
                    print
                    "get news data failed"
            else:
                return None
