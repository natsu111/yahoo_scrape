# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooJapanItem(scrapy.Item):
    content = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
