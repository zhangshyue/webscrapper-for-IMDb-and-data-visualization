# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbtopboxofficeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    url=scrapy.Field()
    user_rating=scrapy.Field()
    num_of_user=scrapy.Field()
    metascore=scrapy.Field()
    popularity=scrapy.Field()
    budget=scrapy.Field()
    cumulative_gross=scrapy.Field()
    length=scrapy.Field()
    pass
