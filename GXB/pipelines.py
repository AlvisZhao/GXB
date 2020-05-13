# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import happybase

class GxbPipeline(object):
    def __init__(self):
       self.host = "192.168.118.134"
       self.connection = happybase.Connection(self.host)

    def process_item(self, item, spider):
        data = [item['title'],item['time'],item['source'],item['content']]
        self.putData(data)

    def putData(self, data):
        self.connection.open()
        # put操作
        table = self.connection.table("ChinaNews")

        table.put(data[0].encode('utf-8'),{
            b'gxb:title': data[0].encode('utf-8'),
            b'gxb:time': data[1].encode('utf-8'),
            b'gxb:source': data[2].encode('utf-8'),
            b'gxb:content': data[3].encode('utf-8')
        })
        self.connection.close()


