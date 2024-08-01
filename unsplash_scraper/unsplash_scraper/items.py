# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnsplashScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UnsplashImage(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
