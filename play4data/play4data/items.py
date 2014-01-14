# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Play4DataItem(Item):
    id = Field()
    content = Field()
    album = Field()
    artist = Field()
    cover = Field()
    song_id = Field()
    song_name = Field()
    mark_time = Field()
