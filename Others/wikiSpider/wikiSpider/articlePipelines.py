#Pipelines

'''
스크레이퍼가 빠르다는 것은 스크랩하려는 사이트의 웹 서버가 각 요청을 빠르게 처리해야 한다
스크레이피의 파이프라인을 사용하면 이전 요청의 데이터 처리가 완료되는 것을 기다리는 것이 아니라\
응답을 기다리는 동안 데이터를 처리할 수 있으므로 스크레이퍼 속도를 더 빠르게 할 수 있다.

파이프라인 클래스를 추가하고, 스파이더는 데이터 수집만 담당하고,\
데이터 처리는 파이프라인에서 담당하도록 기존 스파이더를 수정해야 한다.
스파이더가 응답을 반환하고 파이프라인에서 Article 객체를 만드는 방법이 떠오를 것이다.
'''
# def parse(items, response):
#     return response

'''
Item(Item을 상속하는 Article 같은)객체를 반환해야 한다.
-> parse_items의 리팩토링 목표는 원시 데이터를 추출해서 파이프 라인에 전달하되\
데이터 처리는 최소한으로 줄이는 것이다.
'''
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from wikiSpider.items import Article

class Article(CrawlSpider):
    name='articlePipeliens' #스크레피 이름은 고유함
    allowed_domians=['wikipedia.org']
    start_urls=['http://en.wikipeida.org/wiki/Benevolent_dictator_for_life']
    rules=[
        Rule(LinkExtractor(allow='en.wikipedia.org/wiki/((?!:).)*$'), callback='parse_itmes', follow=True)
    ]
    
    def parse_itmes(self, response):
        article=Article()   #Article 클래스의 객체 생성
        article['url']=response.url
        article['title']=response.css('h1::text').extract_first()
        article['text']=response.xpath('//div[@id="mw-content-text"]//text()').extract_first()
        article['lastUpdated']=response.css('li#footer-info-lastUpdated::text').extract_first()
        return article