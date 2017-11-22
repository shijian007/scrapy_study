#coding = 'utf-8'

import scrapy
from xueqiuspider.items import XueqiuspiderItem
from scrapy.http import Request

class xueqiuspider(scrapy.Spider):
    name = 'xueqiuspider'
    allowed_domins = ['www.douban.com']
    start_urls = ['https://www.douban.com/']

    def start_requests(self):
        yield  Request(url=self.start_urls[0],cookies={'_pk_ses.100001.8cb4': '*', '__utma': '30149280.1974293481.1501811468.1508911865.1510822557.7', '_vwo_uuid_v2': 'EC81E09DCFD65BA420C05E7153EB0641|9dcec41b732aa3d2b0261bd79c785c3a', '__utmz': '30149280.1510822557.7.6.utmcsr', '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1510822553%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DRnjmYw4gF87kqfN3H1QFAcgHVkBbmLvF27Rnv3Mc2yO%26wd%3D%26eqid%3Dd2d5579500007b67000000045a0d5291%22%5D', '_pk_id.100001.8cb4': '5e6ebd81ac2ccf1a.1505357356.4.1510822740.1508911861.', '__yadk_uid': '8vUuH1lQ85hVBodtj2HQbpyiqpnoXTHX', 'dbcl2': '157454657:mjhZn2hpZkU', 'ue': 'xiezj2010@foxmail.com', 'ps': 'y', 'push_noty_num': '0', 'push_doumail_num': '0', 'ck': 'Dpd0', '_ga': 'GA1.2.1974293481.1501811468', '_gid': 'GA1.2.924921817.1510822566', '__utmv': '30149280.15745', 'bid': 'LoRoPlqY-xE', '__utmb': '30149280.7.10.1510822557', '__utmc': '30149280', 'll': '108296', '__utmt': '1'})

    def parse(self, response):
        title = response.xpath('//div[@class="text"]/a/text()').extract()
        # brand = response.xpath('//div[@class="avatar__name"]/a/@data-screenname').extract()
        # title = response.xpath('//article[@class="article__bd"]/h1/text()').extract()
        print(title)




