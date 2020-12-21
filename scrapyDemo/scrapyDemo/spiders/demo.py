import scrapy
from ..items import ScrapydemoItem
from scrapy.http import FormRequest
class Scrapydemo(scrapy.Spider):
    name = 'login'
    start_urls = [
        "http://quotes.toscrape.com/login"
    ]
    def parse(self, response):
        token=response.css("form input::attr(value)").extract_first()
        #print(token)
        return FormRequest.from_response(response, formdata={
            'csrf-token':token,
            'username' : 'iamArnab',
            'password' : 'amIArnab'
        }, callback=self.start_scraping)


    def start_scraping(self,response):
        items = ScrapydemoItem()
        div_entry = response.css('div.quote')
        for data in div_entry:
            quotes = data.css('span.text::text').extract()
            author = data.css('.author::text').extract()
            tags = data.css('.tag::text').extract()
            items['title'] = quotes
            items['author'] = author
            items['tags'] = tags

            yield items
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.start_scraping)