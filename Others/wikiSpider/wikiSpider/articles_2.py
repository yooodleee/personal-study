from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):   #CrawlSpider를 확장한 ArticleSpider
    name='article'  #spider 이름(고유)
    allowed_domains=['wikipedia.org']   #크롤링 시작점
    start_urls=['http://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules=[
        Rule(LinkExtractor(allow='en.wikipedia.org/wiki/((?!:).)*$'),callback='parse_items'\
                ,follow=True, cb_kwargs={'is_article':True}),
        Rule(LinkExtractor(allow='.*'), callback='parse_items', cb_kwargs={'is_article':False})
            ]
    #Rule-> 정의하는 리스트를 모두 찾는 검사하는 Rule 객체 리스트
    #매개변수:allow(따르거나 무시할 도메인), callback(페이지 내용 구문 분석), follow(향후 크롤링 여부), cb_kwargs(콜백 함수에 전달할 매개변수 딕셔너리)


    def parse_items(self, response, is_article):    #문서 페이지(/wiki/로 시작하고 콜론을 포함하지 않는 페이지-> 텍스트)를 기본 매개변수(is_article=True)
        #그러면 나머지는 모두 비문서 페이지이므로 is_article=False 매개변수와 함께 parse_items 함수에 보낸다.
    #스크레이피가 웹 사이트를 크롤링할 때 사용하는 Request 객체를 생성하는 프로그램을 스크레이피가 정의하는 진입점

        print(response.url)
        title=response.css('h1::text').extract_first()  #css:하위 태그의 텍스트 모두 무시

        if is_article:
            url=response.url
            text=response.xpath('//div[@id="mw-content-text"]//text()').extract()   #모든 태그의 텍스트 
            lastUpdated=response.css('li#footer-info-lastmod::text').extract_fisrt()
            lastUpdated=lastUpdated.replace('This page was last edited on ', '')

            print('Title is: {}'.format(title))
            print('last updated: {}'.format(lastUpdated))
            print('text is: {}'.format(text))
        
        else:
            print('This is not an article: {}'.format(title))
    
    def parse_items(self, response, is_article):
        print(response.url)
        title=response.css('h1::text').extract()

        if is_article:
            url=response.url
            text_rule='//div[@id="mw-content-text"]//text()'
            text=response.xpath(text_rule).extract_first()
            update_rule='li#footer-content-lastmod::text'
            update_delete='This page was last edited on '
            lastUpdated=response.css(update_rule).extract_first()
            lastUpdated=lastUpdated.replace(update_delete, '')

            print('Title is: {}'.format(title))
            print('last updated: {}'.format(lastUpdated))
        else:
            print('This is not an artice: {}'.format(title))

'''
규칙은 리스트 순서 그대로 각 링크에 적용된다.

'''