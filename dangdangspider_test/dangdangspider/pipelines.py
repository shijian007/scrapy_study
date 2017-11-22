# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangspiderPipeline(object):
    def process_item(self, item, spider):
        name = item['title'][0]
        comment_number = item['comment_num'][0]
        price = item['price'][0]
        img_url = item['img_url'][0]
        print(u'商品名:'+name)
        print(u'评论数目:'+comment_number)
        print(u'价格:'+price)
        print(u'图片url:'+img_url)
        print('--------------------------')
        return item