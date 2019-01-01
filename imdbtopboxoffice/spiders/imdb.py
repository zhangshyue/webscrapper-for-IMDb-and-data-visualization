# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from imdbtopboxoffice.items import *
import logging
import re

class ImdbSpider(CrawlSpider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/boxoffice']

    rules = (Rule(LinkExtractor(allow='imdb.com',restrict_xpaths="//td[@class='titleColumn']//a"), callback='parse_item'),
    )

    def parse_item(self, response):
        if response.status==200:
            item=ImdbtopboxofficeItem()
            name = response.xpath('//div[@class="title_wrapper"]//h1/text()').extract_first().strip()
            item['name']=name
            item['url']= response.url
            item['user_rating'] = response.xpath('//div[@class="ratings_wrapper"]//span[@itemprop="ratingValue"]/text()').extract_first()
            num=response.xpath('//div[@class="ratings_wrapper"]//span[@class="small"]/text()').extract_first()
            num=num[:len(num)-4]+num[len(num)-3:]
            item['num_of_user'] = num
            item['metascore'] = response.xpath('//div[@class="titleReviewBarItem"]//div[contains(@class,"metacriticScore")]//span/text()').extract_first()
            item['popularity'] = response.xpath('//div[@class="titleReviewBarSubItem"]//span[@class="subText"]/text()').extract()[2].strip()[0:1]
            txts=response.xpath('//div[@class="article"]//div[@class="txt-block"]').extract()
            for txt in txts:
                if re.search('.*?Budget.*?',txt,re.S):
                    item['budget'] = re.search('.*?(\d+,\d+,\d+).*?',txt,re.S).group(1).replace(',','')
            item['length'] = response.xpath('//div[@class="title_wrapper"]//time/text()').extract_first().strip()
            yield item
