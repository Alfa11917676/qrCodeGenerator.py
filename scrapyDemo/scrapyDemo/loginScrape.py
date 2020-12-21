import scrapy
from scrapyDemo.scrapyDemo.items import ScrapydemoItem

class Scrapydemo(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]
    def parse(self, response):
            items=ScrapydemoItem()
            div_entry= response.css('div.quote')
            for data in div_entry:
                quotes = data.css('span.text::text').extract()
                author = data.css('.author::text').extract()
                tags = data.css('.tag::text').extract()
                items['title']=quotes
                items['author'] = author
                items['tags'] = tags

                yield items
            next_page=response.css("li.next a::attr(href)").get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)