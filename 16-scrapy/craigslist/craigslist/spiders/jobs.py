import scrapy
from itemadapter import ItemAdapter
from pymongo import MongoClient, errors

class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            yield {"quote": quote.xpath('.//*[@class="text"]/text()').get(),  # Pour être resilien au changement on met des * et non le nom des balises
                   "author": quote.xpath('.//*[@class="author"]/text()').get()}
        relative_urls = response.xpath('//*[@class="next"]/a/@href')
        yield from response.follow_all(relative_urls, self.parse)
 

