from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):   #wikispider는 ArticleSpider보다 더 넓은 범주-> 다른 페이지 유형을 검색
    name='articles' #스파이더 이름(고유)
    allowed_domians=['wikipedia.org']   #어디에서 크롤링을 시작할지
    start_urls=['http://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules=[Rule(LinkExtractor(allow='.*'), callback='parse_items', follow=True)]
    #allow-> 링크를 따르거나 무시해야 하는 도메인을 기반으로 알려줌
    #규칙 리스트(Rule)-> 무시할 링크에 대한 자세한 지침(allow), 정규표현식 .*(모든 URL 허용)
    #Rule: 정의하는 리스트는 찾은 링크를 모두 검사하는 Rule 객체 리스트/순서대로 검사됨
    #LinkExtractor-> 필수 매개변수인 LinkExtractor 객체.(유일)
    #callback-> 페이지 내용 구문 분석
    #cb_kwargs-> 콜백 함수에 전달할 매개변수 딕셔너리, {arg_name1:arg_value1, arg_name2:arg_value2}
    #follow-> 현 페이지의 링크를 향후 크롤링에 포함할지 여부, 콜백 함수가 없으면 기본 True, 있다면 기본 False

    def parse_items(self, response):
    #스크레이피가 웹 사이트를 크롤링할 때 사용하는 Request 객체를 생성하는 프로그램을 스크레이피가 정의하는 진입점

        url=response.url
        title=response.css('h1::text').extract_first()  #css 방식
        text=response.xpath('//div[@id="mw-content-text"]//text()').extract()   #xpath 방식
        lastUpdated=response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated=lastUpdated.replace('This page was last edited on ', '')

        print('URL is: {}'.format(url))
        print('title is: {}'.format(title))
        print('text is: {}'.format(text))
        print('Last updated: {}'.format(lastUpdated))
    
    def parse_items(self, response):
        url=response.url
        title=response.css('h1::text').extract_first()  #css:하위 태그 내의 텍스트는 모두 무시
        text_rule='//div[@id="mw-content-text"]//text()'    #xpath:텍스트 컨텐츠를 검색
        text=response.xpath(text_rule).extract()

        update_rule='li#footer-info-lastmod::text()'    #css
        update_delete='This page was last edited on'
        lastUpdated=response.css(update_rule).extract_first()
        lastUpdated=lastUpdated.replace(update_delete, '')

        print('URL is: {}'.format(url))
        print('title is: {}'.format(title))
        print('text is: {}'.format(text))
        print('Last updated: {}'.format(lastUpdated))