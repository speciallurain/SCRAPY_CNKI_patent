# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class InfoPipeline(object):
   def process_item(self, item, spider):
       return item

# class InfoPipeline(object):
#     def __init__(self):
#         self.csvwriter = csv.writer(open('pkeecs.csv', 'w'))
#         self.csvwriter.writerow(['姓名', '照片', '信息'])
#     def process_item(self, item, spider):
#         self.csvwriter.writerow([item['name'], item["pic_url"], item['info']])
#         return item


