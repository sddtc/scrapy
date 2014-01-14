from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import json

from play4data.items import Play4DataItem

class BubsSpider(BaseSpider):
    name = "bubs"
    allowed_domains = ["douban.com"]
    start_urls = [
    '''please replace id with :id you want'''
    "http://api.douban.com/labs/bubbler/user/:id/bubs"
    ]

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        sites = jsonresponse["result"]
        items = []
        for site in sites:
            item = Play4DataItem()
            item["id"] = site["id"]
            item["content"] = site["content"]
            item["album"] = site["song"]["album"]
            item["artist"] = site["song"]["artist"]
            item["song_id"] = site["song"]["sid"]
            item["song_name"] = site["song"]["song_name"]
            item["cover"] = site["song"]["cover"]
            item["mark_time"] = site["time"]
            
            items.append(item)
        return items
