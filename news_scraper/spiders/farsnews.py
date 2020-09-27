import scrapy


class FarsnewsSpider(scrapy.Spider):
    name = 'farsnews'
    allowed_domains = ['www.farsnews.ir']
    start_urls = ['http://www.farsnews.ir/']

    def parse(self, response):
        pass
