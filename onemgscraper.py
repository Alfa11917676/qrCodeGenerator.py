import scrapy


class OnemgscraperSpider(scrapy.Spider):
    name = 'onemgscraper'
    allowed_domains = ['1mg.com']
    start_urls = ['http://1mg.com/']

    def parse(self, response):
        pass
