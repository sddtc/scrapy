from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from doubanImageBeta.items import DoubanimageBetaItem

class DownloadImg(BaseSpider):
    name = "doubanalbum"
    allowed_domains = ["douban.com"]
    start_urls = []
    for startIndex in range(0,90,18):
        url = 'http://www.douban.com/photos/album/65355143/?start=%d' %startIndex
        start_urls.append(url)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select("//div/div/div/div[@class='photo_wrap']/a/img/@src").extract()
        items = []
        for site in sites:
            site = site.replace('thumb','photo')
            item = DoubanimageBetaItem()
            item['image_urls'] = [site]
            
            items.append(item)
        return items
