#coding = 'utf-8'

import scrapy
from dangdangspider.items import DangdangspiderItem
from scrapy.http import Request

class dangdangspiderman(scrapy.Spider):
    name = 'dangdangspider'
    allowed_domins = ['dangdang.com']
    start_urls = ['http://3c.dangdang.com/pc']

    def parse(self,response):   #解析商品品类页
        categroy = response.xpath('//div[@class="level_one "]/dl/dd/a/@href').extract()
        for url1 in categroy:
            yield Request(url1,callback=self.parse_detail)

    def parse_detail(self,response):  #解析商品展示目录页
        link = response.xpath('//a[@class="pic"]/@href').extract()
        next_link = response.xpath('//li[@class="next"]/a/@href')[0].extract()
        if next_link:
            yield scrapy.Request('http://category.dangdang.com' + next_link, callback=self.parse_detail)

        for detail_url in link:
            yield Request(detail_url,callback=self.parse_price)


    def parse_price(self,response): #解析商品详情页
        item = DangdangspiderItem()
        item['title'] = response.xpath('//div[@class="name_info"]/h1/@title').extract()

        item['comment_num'] = response.xpath('//a[@id="comm_num_down"]/text()').extract()
        item['price'] = response.xpath('//p[@id="dd-price"]/text()').extract()
        item['img_url'] = response.xpath('//img[@id="largePic"]/@src').extract()
        yield item
