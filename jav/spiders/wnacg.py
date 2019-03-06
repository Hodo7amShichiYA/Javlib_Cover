import scrapy
import urllib.request
class GoAcg(scrapy.Spider):
    name = "GoAcg"  # 定义蜘蛛名
    title = 1
    def start_requests(self):
        # cookie = {
            # 'Cookie': '__cfduid=d3fd4a3b41a04c141fa40bc9c8b3e6d7b1551684132; timezone=-480; __qca=P0-67177064-1551758802220; over18=18'}
        headers = {
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        }
        for i in range(1, 220):
            url1 = "https://www.wnacg.org/photos-index-page-%s-aid-70527.html" % i
            print(url1)
            yield scrapy.Request(
                url=url1,
                headers=headers,
                # cookies=cookie,
                callback=self.parse
            )
    def parse(self, response):
        # cookie = {
            # 'Cookie': '__cfduid=d3fd4a3b41a04c141fa40bc9c8b3e6d7b1551684132; timezone=-480; __qca=P0-67177064-1551758802220; over18=18'}
        headers = {
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        }
        links = response.xpath('//a[starts-with(@href,"/photos-view-id")]/@href').extract()
        for link in links:
            url = link.split("/")[1]
            url2 = 'https://www.wnacg.org/'+url
            yield scrapy.Request(
                url=url2,
                headers=headers,
                # cookies=cookie,
                callback=self.parse_2
            )
    def parse_2(self, response):
        global title
        # titles = response.xpath('// *[ @ id = "bread"] / div[3] / text()').extract()
        image_urls = response.xpath('//img[@id="picarea"]/@src').extract()
        f = open("E:/00 Python/Project/Scrapy Project/01/%s.jpg" % title, 'wb')
        f.write((urllib.request.urlopen("http:"+image_urls[0])).read())
        print(titles[0]+"http:"+image_urls[0])
        f.close()
        title += 1

