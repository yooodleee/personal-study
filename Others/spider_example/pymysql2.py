from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

#데이터베이스 연결 문자열에 'charset=utf8' 추가됨-> 데이터베이스에 정보를 보낼 때 모두 utf-8로 보내야 함을 의미.
conn=pymysql.connect(host='127.0.0.1', user='root', passwd='@dhalstn1025', db='root', charset='utf8')

cur=conn.cursor()
cur.execute('use scraping')

random.seed(datetime.datetime.now())

#store 메서드-> 문자열 변수 title, content를 받고, insert 문에 추가함.
def store(title, content):
    cur.execute(    #커서(연결 객체)는 insert 문을 실행-> 데이터베이스에 보냄.
        'insert into pages (title, content) values (%s, %s)',
        (title, content)
    )
    cur.connection.commit()

def getLinks(artilceUrl):
    html=urlopen('http://en.wikipedia.org'+artilceUrl)
    bs=BeautifulSoup(html, 'html.parser')
    
    title=bs.find('h1').get_text()
    content=bs.find('div', {'id':'mw-content-text'}).find('p').get_text()
    store(title, content)
    
    return bs.find('div', {'id':'bodyContent-text'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links=getLinks('/wiki/Kevin_Bacon')
try:
    while len(links)>0:
        newArticle=links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links=getLinks(newArticle)
finally:
    #프로그램이 어떻게든 방해를 받거나, 실행 중 예외가 발생하더라도 종료 전에 반드시 커서와 연결 객체를 닫음
    cur.close()
    conn.close()
#데이터 베이스 연결을 열어둔 채 웹 스크레이핑을 할 때는 항상 try...finally 문을 사용하는 게 좋음