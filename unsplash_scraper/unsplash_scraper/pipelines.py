# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class UnsplashScraperPipeline:
#     def process_item(self, item, spider):
#         return item
#--------------------------------------------------------    

# import csv

# class CsvPipeline(object):

#     def open_spider(self, spider):
#         self.file = open('images.csv', 'w', newline='')
#         self.writer = csv.writer(self.file)
#         self.writer.writerow(['image_url', 'local_path', 'title', 'category'])

#     def close_spider(self, spider):
#         self.file.close()

#     def process_item(self, item, spider):
#         image_path = item['images'][0]['path'] if 'images' in item else ''
#         self.writer.writerow([item['image_urls'][0], image_path, item['title'], item['category']])
#         return item
#--------------------------------------------------------  

import csv
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class CustomImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None, *, item=None):
        title = item['title']
        return f'{title}.jpg'

class CsvPipeline(object):

    def open_spider(self, spider):
        self.file = open('images.csv', 'w', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['title', 'category'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow([item['title'], item['category']])
        return item
