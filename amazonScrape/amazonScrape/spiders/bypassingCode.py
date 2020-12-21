import scrapy
from ..items import AmazonscrapeItem

class amazonSpider(scrapy.Spider):
    name ="amazon"
    page_number=2
    start_urls = [
    "https://www.amazon.in/s?k=books&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&qid=1608484611&rnid=2684818031&ref=sr_nr_p_n_publication_date_1"
    ]
    def parse(self, response):
                items=AmazonscrapeItem()
                name=response.css(".a-color-base.a-text-normal::text").extract()
                price=response.css(".a-spacing-top-small .a-price-whole").css('::text').extract()
                author=response.css(".a-color-secondary .a-size-base+ .a-size-base").css('::text').extract()
                image_link=response.css(".s-image::attr(src)").extract ()

                items['name']=name
                items['price']=price
                items['author']=author
                items['image_link']=image_link

                yield items
                next_page="https://www.amazon.in/s?k=books&i=stripbooks&rh=n%3A976389031&dc&page="+str(amazonSpider.page_number)+"&qid=1608489602&rnid=2684818031&ref=sr_pg_4"
                if amazonSpider.page_number <=75:
                    amazonSpider.page_number+=1
                    yield response.follow(next_page,callback=self.parse)