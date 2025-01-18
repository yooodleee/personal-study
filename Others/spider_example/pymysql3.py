from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
from random import shuffle

conn=pymysql.connect(host='127.0.0.1', user='root', passwd='@dhalstn1025', db='mysql', charset='utf8')

cur=conn.cursor()
cur.execute('use wikipedia')

#insertPageIfNotExists-> 새 페이지를 발견할 때마다 저장함(페이지를 중복 저장하는 것을 방지함)
def insertPageIfNotExists(url):
    cur.execute('select * from pages where url=%s', (url))
    if cur.rowcount==0: #새 페이지를 발견하면
        cur.execute('insert into pages (url) values (%s)', (url))  #insert로 저장
        conn.commit()

        return cur.lastrowid
    else:
        return cur.fetchone()[0]

#loadPages-> 새 페이지에 방문해야 하는지 결정할 수 있도록 데이터베이스에 저장된 페이지를 모두 리스트에 담아 반환.
#페이지 수집은 프로그램이 동작할 때만 이루어지므로 데이터베이슬스를 완전히 비워놓고 프로그램을 한 번만 실행하면 이론적으로
#메서드가 필요 없을 수도 있다.
def loadPages():
    cur.execute('select * from pages')
    pages=[row[1] for row in cur.fetchall()]    
    
    return pages

#insertLink-> 데이터베이스에 링크를 기록, 이미 존재하는 링크는 다시 만들지 않음
#같은 연결고리를 나타내는 똑같은 링크가 둘 이상 존재하더라도, 하나로 보아야 함.
#프로그램을 여러 번 실행하더라도 데이터베이스의 무결점을 보장함.
def insertLink(fromPageId, toPageId):
    cur.execute('select * from links where fromPageId=%s and topageId=%s', (int(fromPageId), int(toPageId)))
    if cur.rowcount==0: #링크가 존재하지 않으면 insert로 기록
        cur.execute('insert into links (fromPageId, toPageId) values (%s, %s)',
                    (int(fromPageId), int(toPageId)))
        conn.commit()
    
def pageHasLinks(pageId):
    cur.execute('select * from links where fromPageId=%s', (int(pageId)))
    rowcount=cur.rowcount
    if rowcount==0: #페이지를 방문하고 외부 링크를 모두 기록해야만 True로 바꾸는 방식을 사용
        #링크를 통해 방문할 수 있는 페이지들이 기록되지 않는 것을 방지
        return False
    return True

def getLinks(pageUrl, recursionLevel, pages):   
    #recursionLevel 변수를 getLinks 함수에 남겨 호출될 때마다 recursionLevel을 +1하여 몇 번째 재귀인지 센다.
    if recursionLevel>4:    #재귀가 4번 넘어가면(5가 되면) 자동으로 검색을 멈춘다.-> 스택 오버플로우는 생기지 않음
        return
    
    pageId=insertPageIfNotExists(pageUrl)
    html=urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs=BeautifulSoup(html, 'html.parser')
    links=bs.find('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links=[link.attrs['href'] for link in links]

    for link in links:
        linkId=insertPageIfNotExists(link)
        insertLink(pageId, linkId)
        if not pageHasLinks(linkId):
            #새 페이지를 만났으니 추가하고 링크를 검색한다.
            print('page has no links: {}'.format(link))
            pages.append(link)
            getLinks(link, recursionLevel+1, pages)

getLinks('/wiki/Kevin_Bacon', 0, loadPages)
cur.close()
conn.close()