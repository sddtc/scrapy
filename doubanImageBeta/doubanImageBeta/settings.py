# Scrapy settings for doubanImage project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'doubanImageBeta'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['doubanImageBeta.spiders']
NEWSPIDER_MODULE = 'doubanImageBeta.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
IMAGES_STORE = 'images'
# 90 days of delay for image expiration
IMAGES_EXPIRES = 90
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110
