#--coding='utf-8'--

import scrapy
from lagouspider.items import LagouspiderItem
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log

class lagouspider(scrapy.Spider):
    def __init__(self):
        pass

    download_delay = 2
    name = 'lagouspider'
    allowed_domains = 'https://www.lagou.com/jobs'
    start_urls = ['https://www.lagou.com/zhaopin/Python/?labelWords=label']

    def parse(self, response):
        sel = Selector(response)
        item = LagouspiderItem()
        item['address'] = sel.xpath('li[@data-index=0]/h3/text()').extract()

        return item

