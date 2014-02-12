from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import json

from facewords.items import FacewordsItem

class FaceWordsSpider(BaseSpider):
    name="facewords"
    
    start_urls = []
    for i in range(1,2):
        start_urls.append('file:////home/sddtc/py/scrapy/facewords/cateid_15/page_%d.html' %i)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        sites = hxs.select('//div[@class="facemoodItemText"]/text()').extract()
        clearSites = []
        for text in sites:
            text = "".join(text.split())
            if text != "":
                clearSites.append(text)
        
        for site in clearSites:
            item = FacewordsItem()
            item['faceText'] = site
            items.append(item)
        return items        
