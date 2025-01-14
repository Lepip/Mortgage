# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class SpiderCianPipeline:
    def open_spider(self, spider):
        if 'City' in spider.name:   
            self.file = open('items.csv', 'w',encoding='utf-8',newline='')
            self.writer = csv.writer(self.file)
            self.writer.writerow(['name','id'])
        else:
            self.file = open('items.csv', 'r',encoding='utf-8')

    def close_spider(self, spider): 
        self.file.close()

    def process_item(self, item, spider):
        if 'City' in spider.name:
            if item['name'] != None:
                line = [item["name"],item["id"]]
                self.writer.writerow(line)
        else:
            print(item)
        return item
