#--coding='utf-8'--

import scrapy
from lagouspider.items import LagouspiderItem
from scrapy.selector import Selector
from scrapy.http import Request
# from scrapy import log

class lagouspider(scrapy.Spider):

    def __init__(self):
        self.headers = {
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding':'gzip, deflate',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    name = 'lagouspider'
    # allowed_domains = 'https://www.lagou.com/jobs'
    # start_urls = ['https://www.lagou.com/zhaopin/Python/?labelWords=label']
    # allowed_domains = 'http://dangdang.com/'
    # start_urls = ['http://book.dangdang.com/']
    allowed_domains = 'http://www.pm25.com'
    start_urls = ['http://www.pm25.com/hangzhou']


    def parse(self, response):
        item = LagouspiderItem()

        # link = response.xpath('//div[@class="level_one "]/dl/dd/a/@href').extract()
        # print(link)

        # categroy = response.xpath('//div[@class="level_one "]/dl/dd/a/@href').extract()
        # print(categroy)

        categroy = response.xpath('//div[class="bi_location"]/h2/text()').extract()
        print(categroy)

        print("7777777777777777777777777")



        # def parse(self, response):
    #     sel = Selector(response)
    #     item = LagouspiderItem()
    #     job_list= response.xpath('//div[@class="position"]/div[@class="p_top"]/a/@href').extract()
    #     print("7777777777777777777777777")
    #     print(job_list)
    #     for jobs in job_list:
    #         #job = jobs.xpath('//li[class="con_list_item default_list"]/@data-positionname').extract()
    #         print("88888888888888888888888888")
    #         print(jobs)
    #
    #     return item

