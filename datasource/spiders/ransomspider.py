import scrapy
from dateutil.parser import parse as parse_date
from datasource.items import DatasourceItem

class RansomspiderSpider(scrapy.Spider):
    name = "ransomspider"
    allowed_domains = ["packetstormsecurity.com"]
    start_urls = ["https://packetstormsecurity.com/search/%20news/?q=ransomware"]

    def parse(self, response):
        cont = True
        news = response.css('dl.file')
		
        for n in news:
            yield {
                'title': n.css('dt a::text').get(),
                'url': 'https://packetstormsecurity.com'+n.css('dt a::attr(href)').get(),
                'postedDate': n.css('dd.datetime a::text').get(),
                'author' : n.css('dd.refer a::text').get(),
                'articleText' : n.xpath('./dd[3]/p/text()').getall(), 
            }
        
        next_page = response.xpath('//div[@id="nv"]/a[contains(text(),"Next")]/@href').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
