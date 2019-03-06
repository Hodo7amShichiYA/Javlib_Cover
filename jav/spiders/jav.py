import scrapy
import urllib.request
class javrun(scrapy.Spider):
    name = "javrun"  # 定义蜘蛛名
    def start_requests(self):
        cookie = {
            'Cookie': '__cfduid=d3fd4a3b41a04c141fa40bc9c8b3e6d7b1551684132; timezone=-480; __qca=P0-67177064-1551758802220; over18=18'}
        headers = {
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        }
        start_url = 'http://p26y.com/cn/vl_maker.php?&mode=2&m=oq&page=1'
        for i in range(1, 50):
            url1 = "http://p26y.com/cn/vl_maker.php?&mode=2&m=oq&page=%s" % i
            print(url1)
            yield scrapy.Request(
                url=url1,
                headers=headers,
                cookies=cookie,
                callback=self.parse
            )
    def parse(self, response):
        cookie = {
            'Cookie': '__cfduid=d3fd4a3b41a04c141fa40bc9c8b3e6d7b1551684132; timezone=-480; __qca=P0-67177064-1551758802220; over18=18'}
        headers = {
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        }
        links = response.xpath('//a[starts-with(@href,"./?v=javl")]/@href').extract()
        for link in links:
            url = link.split("/")[1]
            url2 = 'http://p26y.com/cn/'+url
            print('http://p26y.com/cn/'+url2)

            yield scrapy.Request(
                url=url2,
                headers=headers,
                cookies=cookie,
                callback=self.parse_2
            )
    def parse_2(self, response):
        titles = response.xpath('//a[starts-with(@href,"/cn/")]/text()').extract()
        image_urls = response.xpath('//img[@id="video_jacket_img"]/@src').extract()
        f = open('./img02/' + titles[0] + ".jpg", 'wb')
        f.write((urllib.request.urlopen("http:"+image_urls[0])).read())
        print(titles[0]+"http:"+image_urls[0])
        f.close()