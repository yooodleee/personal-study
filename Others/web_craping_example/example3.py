from scrapy import linkextractors
from scrapy import spiders


class ExtractWantedSpider(spiders):
    name = 'wanted_data'
    allowed_domains = ['wanted.co.kr']
    start_urls = ['https://wanted.co.kr/']
    rules = [spiders(linkextractors(allow=r'.*'), callback='parse_items', follow=True)]


    def parse_items(self, response):
        url = response.url
        compan_name = response.xpath('//*[@id="__next"]/div[3]/div[2]/div/div[1]/div[1]/div[1]/h1').extract()
        company_hire = response.xpath('//*[@id="__next"]/div[3]/div[2]/div/div[2]/section[6]/h2/div').extract()
        tech_stack = response.xpath('//*[@id="__next"]/div[3]/div[2]/div/div[2]/section[2]/h2/div').extract()
        wage = response.xpath('//*[@id="__next"]/div[3]/div[2]/div/div[2]/section[4]/h2/div').extract()
        employee = response.xpath('//*[@id="__next"]/div[3]/div[2]/div/div[2]/section[4]/h2/div').extract()
        sales = response.xpath('//*[@id="__next"]/div[3]/div[2]/div/div[2]/section[6]/h2/div').extract()
        company_info = response.xpath('//*[@id="__next"]/div[3]/div[2]/div/div[2]/section[6]/h2/div').extract()