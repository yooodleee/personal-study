# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikispiderItem(scrapy.Item):

    url=scrapy.Field()
    title=scrapy.Field()
    text=scrapy.Field()
    lastUpdated=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
