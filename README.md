自定义 scrapy 爬虫
======

## 准备工作

在 Mac 上安装 scrapy 参照博客: [mac安装scrapy实践](https://homuralovelive.com/sddtc/tech/2015/11/03/mac-install-scrapy.html)
为什么要参照这篇博客呢？ 因为我用 scrapy 官网的命令不得劲儿哇 `pip install scrapy`

## catchYou

**通过用户 ID 范围围脖找人**  

通过 API 抓取数据, 因为围脖爬取数据的限制较多, 例如: `weibo.com` 是无法爬取内容, 因此使用当前围脖移动端并且是 `cn` 站点的 API:  

#### 个人页面

```
https://m.weibo.cn/api/container/getIndex?type=uid&value={usr_id}
```

从这个结果页面能拿到两个 containerid 的 ID, 作为下面两个 API 的 URL 的输入  

#### 个人信息 `profile` 页面

```
https://m.weibo.cn/api/container/getIndex?containerid={oid}&type=uid&value={uid}&page={page}
```

#### 个人的围脖 `tweets` 页面

```
https://m.weibo.cn/api/container/getIndex?containerid={oid}&type=uid&value={uid}&page={page}
```

命令:  

```
cd catchYou/catchYou/spiders

scrapy crawl catchYouSpider
```

这样可以爬取到用户的 ID, Nickname, Profile ContainerID, Tweets ContainerID  
抓取频率 DELAY 1s

## doubanImageBeta

实现了读取豆瓣电影海报下图片的下载爬虫  

## play4data

这个是个稍微大的爬虫  
目前实现了豆瓣实验室API读取BUBS的存储  
使用Postgresql  
scrapy0.14+postgresql9.3  

