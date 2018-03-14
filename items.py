# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InfoPipeline(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    person_part_1= scrapy.Field()
    person_part_2=scrapy.Field()
    pic_url = scrapy.Field()


