# Scrapy settings for play4data project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'play4data'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['play4data.spiders']
NEWSPIDER_MODULE = 'play4data.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

SPIDER_PSQL_DB = {
    'host': 'localhost',
    'user': 'postgres',
    'passward': '123456',
    'dbname': 'play4data'
}

ITEM_PIPELINES = ['play4data.pipelines.Play4DataPipeline']
