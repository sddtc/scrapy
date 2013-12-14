from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from doubanImageBeta.items import DoubanimageBetaItem

class DownloadImg(BaseSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ['http://movie.douban.com/subject/1760828/photos']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li/div/a/img/@src').extract()
        items = []
        for site in sites:
            site = site.replace('thumb','raw')
            item = DoubanimageBetaItem()
            item['image_urls'] = [site]
            
            items.append(item)
        return items
