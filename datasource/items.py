# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DatasourceItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()
    postedDate = scrapy.Field()
    author = scrapy.Field()
    articleText = scrapy.Field()
