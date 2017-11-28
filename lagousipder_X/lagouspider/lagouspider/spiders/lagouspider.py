#--coding='utf-8'--

import scrapy
from lagouspider.items import LagouspiderItem
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log

class lagouspider(scrapy.Spider):
    download_delay = 2
    name = 'lagouspider'
    allowed_domains = 'https://www.lagou.com/jobs'
    start_urls = ['https://www.lagou.com/zhaopin/Python/?labelWords=label']

    def parse(self, response):
        sel = Selector(response)
        item = LagouspiderItem()
        job_list= sel.xpath('//ul[@s_position_list"]/ul/li/@data-positionname').extract()
        print("7777777777777777777777777")
        for jobs in job_list:
            #job = jobs.xpath('//li[class="con_list_item default_list"]/@data-positionname').extract()
            print("88888888888888888888888888")
            print(jobs)

        return item

