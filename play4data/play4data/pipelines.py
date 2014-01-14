# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import psycopg2
from settings import SPIDER_PSQL_DB

class Play4DataPipeline(object):
    def __init__(self):
        try:
            self.conn = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['passward']))
            self.cursor = self.conn.cursor()
        except:
            print "Unable to connect to the database"

    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into db_bubs(id,content,album,artist,cover,song_id,song_name,mark_time) values (%s,%s,%s,%s,%s,%s,%s,%s)",(item['id'],item['content'],item['album'],item['artist'],item['cover'],item['song_id'],item['song_name'],item['mark_time']))
#            self.cursor.execute("inser into db_bubs(id) values(%s)",item['id'])

            self.conn.commit()
        except psycopg2.DatabaseError, e:
             print "Error %s" % e
             exit(1)

#        print item['content']+"***************"

        return item
