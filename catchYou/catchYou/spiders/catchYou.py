# -*- coding: utf-8 -*-
import scrapy
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time


class CatchYouSpider(scrapy.Spider):
    name = 'catchYouSpider'

    def start_requests(self):
        id_start = 6647189999
        # id_end = 6647215000
        id_end = 6647190000

        urls = []
        for id in range(id_start, id_end):
            url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=%s' % id
            urls.append(url)

        self.log("*******************************")
        self.log('Collect URLs count: %s' % len(urls))
        self.log("*******************************")

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        userBaseProfile = json.loads(response.body)

        isOK = userBaseProfile['ok']
        if isOK == 1:
            weiboCounts = userBaseProfile['data']['userInfo']['statuses_count']
            if weiboCounts > 0 and weiboCounts < 1000:
                userId = userBaseProfile['data']['userInfo']['id']
                userNickname = userBaseProfile['data']['userInfo']['screen_name']
                userTabs = userBaseProfile['data']['tabsInfo']['tabs']

                for tab in userTabs:
                    if tab['tab_type'] == 'profile':
                        profileContainerId = tab['containerid']
                    elif tab['tab_type'] == 'weibo':
                        weiboContainerId = tab['containerid']

                catchYouBaseInfo = 'catchYouBaseInfo2'
                with open(catchYouBaseInfo, 'a') as f:
                    f.write('%s\t%s\t%s\t%s\t%s\n' % (userId, userNickname.encode(
                        'utf-8'), weiboCounts, profileContainerId, weiboContainerId))
            else:
                self.log("*******************************")
                self.log('weiboCounts > 1000 or <0')
                self.log("*******************************")
        else:
            self.log("*******************************")
            self.log("User no content: %s" % response)
            self.log("*******************************")
