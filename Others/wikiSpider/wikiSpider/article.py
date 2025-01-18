import scrapy

class ArticleSpider(scrapy.Spider): #wikispider는 ArticleSpider보다 더 넓은 범주-> 다른 페이지 유형을 검색
    name='article'  #스파이더 이름-> 고유해야 함

    def start_requests(self):   
        #스크레이피가 웹 사이트를 크롤링할 때 사용하는 Request 객체를 생성하는 프로그램을 스크레이피가 정의하는 진입점
        urls=[
            'http://en.wikipedia.org/wiki/Python%28programming_language%29',
            'http://en.wikipedia.org/wiki/Functional_programming',
            'http://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]
    
    def parse(self, response):  #parse:callback=self.parse를 사용하여 Requests 객체로 전달됨
        url=response.url
        title=response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))

