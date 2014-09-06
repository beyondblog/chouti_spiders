# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs  
import json


class ChoutiPipeline(object):
    def __init__(self):
        self.file = codecs.open('chouti.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print '----------------------------------------------------------'
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line.decode("utf-8"))
        return item

    def spider_closed(self, spider):
        self.file.close()
