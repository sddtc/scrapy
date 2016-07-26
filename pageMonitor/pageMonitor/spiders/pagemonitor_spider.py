# -*- coding: utf-8 -*-
import scrapy
from pageMonitor.items import PagemonitorItem

class PagemonitorSpider(scrapy.spiders.Spider):
    name = "pagemonitor"
    allowed_domains = ["zara.cn"]
    start_urls = ['http://www2.hm.com/zh_cn/productpage.0373764011.html']
                    #'https://detail.tmall.com/item.htm?spm=a1z10.4-b.w4007-14252748703.1.06pqbA&id=530545346188&rn=a9af89d7bee15111279bf6b04e840a85&abbucket=5',
                    #'http://www.zara.cn/cn/zh/%E6%89%93%E6%8A%98/trf/%E5%A4%96%E5%A5%97%E5%92%8C%E4%B8%8A%E8%A1%A3/%E9%92%A9%E9%92%88%E5%BC%80%E8%A5%9F%E8%A1%AB-c436441p3351008.html']

    def parse(self, response):
        for sel in response.xpath('/html'):
            item = PagemonitorItem()
            item['title'] = sel.xpath('//h1[@class="product-item-headline"]/text()').extract()
            item['price'] = sel.xpath('//section[contains(@class,"product-detail-meta")]//span[@class="price-value"]/text()').extract()
            item['oriprice'] = sel.xpath('//section[contains(@class,"product-detail-meta")]//small[@class="price-value-original"]/text()').extract()
            yield item

