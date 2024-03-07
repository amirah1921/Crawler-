import scrapy
from newspaper import Article

class RansomtheregisterSpider(scrapy.Spider):
    name = "ransomtheregister"
    allowed_domains = ["www.theregister.com"]
    start_urls = ["https://www.theregister.com/Tag/ransomware"]

    def parse(self, response):
        news_items = response.xpath('//*[@id="tag"]/div/div[2]/div[1]/div/article')
        urlList = []
        for news_item in news_items:
            title = news_item.css('h4::text').get()
            url = news_item.css('a.story_link').attrib['href']
            posted_date = news_item.xpath('//*[@id="tag"]/div/div[2]/div[1]/div/article[1]/a/div[2]/div[2]/span[2]/text()').getall()

            yield response.follow(url, callback=self.parse_article, meta={
                'title': title,
                'url': url,
                'postedDate': posted_date,
            })
            urlList.append(url)

        for url in urlList:
            yield response.follow(url, callback=self.parse_article)

        # Follow the pagination link if available
        next_page = response.css('div.more_link a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse) 

    def parse_article(self, response):
        article = Article(response.url, language="en")
        article.download()
        article.parse()

        yield {
            'title': response.meta['title'],
            'url': response.url,
            'postedDate': response.meta['postedDate'],
            'author': article.authors,
            'articleText': article.text,
        }
