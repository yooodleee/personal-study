# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from datetime import datetime
from wikiSpider.wikiSpider.items import Article
from string import whitespace

class wikispiderPipeline(object):
    def process_item(self, article, spider):    
        #process_item은 Article 객체를 가져와서 lastUpdated열을 ISO 표준 문자열로 변환, text를 문자열 리스트에서 문자열 하나로 결합
        #모든 파이프라인 클래스에 필수 메서드-> 스파이더가 수집한 Items를 비동기적으로 전달
        #반환하는 파싱된 Article 객체는 로그에 기록/JSON, CSV로 저장하면 해당 형식으로 저장됨.
        dateStr=article['lastUpdated']  
        dateStr=dateStr.replace('This page was ;ast edited on ', '')
        dateStr=dateStr.strip() #strip-> 문자열 사이에 공백 지워줌
        dateStr=datetime.strptime(dateStr, '%d %B %Y, at %H:%H')
        dateStr=dateStr.strptime('%Y-%m-%d %H:%M:%S')
        article['lastUpdated']=dateStr

        texts=article['text'][0:50]
        texts=[line for line in texts if line not in whitespace]
        article['text']=''.join(texts)
        return article
    
    # def process_item(self, item, spider):
    #     if isinstance(item, Article):
    #         #항목별로 고유한 데이터를 처리한다.