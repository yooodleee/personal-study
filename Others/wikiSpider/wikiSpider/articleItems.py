from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from wikiSpider.items import Article

class ArticleSpider(CrawlSpider):
    name='article'
    allowed_domains=['wikipedia.org']
    start_urls=['http://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    rules=[
        Rule(LinkExtractor(allow='ebd.wikipedia.org/wiki/(?!:).)*$'),
             callback='parse_items', follow=True),
    ]

    def parse_items(self, response):
        article=Article()
        article['url']=response.url
        article['title']=response.css('h1::text').extract_first()
        article['text']=response.xpath('//div[@id="mx-content-text"]//text()').extract()
        
        lastUpdated=response.css('li#footer-info-lastmod::text').extract_first()
        article['lastUpdated']=lastUpdated.replace('This page was last edited on ', '')

        return article