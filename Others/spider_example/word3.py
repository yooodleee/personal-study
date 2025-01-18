#위키백과 항목에서 찾은 2-그램 항목을 반환한다.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# def getNgrams(content, n): 
#     #ngrams 함수는 입력 문자열을 받고, 모든 단어가 공백으로 구분되었다고 가정하여 연속된 단어로 나눈 다음 n-그램 배열(2-그램)을 만들어 반환한다.
#     content=content.split(' ')
#     output=[]
    
#     for i in range(len(content)-n+1):
#         output.append(content[i:i+n])
#     return output

def getNgrams(content, n):
    content=re.sub('\n|[[d+\]]', ' ', content)  
    #정규표현식-> \n(이스케이프 문자)를 제거, 유니코드 문자도 제거(인용표시)
    content=bytes(content, 'UTF-8') #연속된 공백을 제거해서 빈 문자열을 없앰.
    #컨텐츠 인코딩을 'utf-8'로 바꾸어 이스케이프 문자를 없앰.
    content=content.decode('ascii', 'ignore')
    content=content.split(' ')
    content=[word for word in content if word!='']

    output=[]
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

html=urlopen('http://en.wikipedia.org/python_(programming_language)')
bs=BeautifulSoup(html, 'html.parser')
content=bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams=getNgrams(content, 2)    
print(ngrams)
print('2-grams count is: '+str(len(ngrams)))
