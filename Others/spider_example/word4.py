from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string   #구두점이라 생각하는 모든 글자의 리스트

def cleanSentence(sentence):
    sentence=sentence.split(' ')
    sentence=[word.strip(string.punctuation+string.whitespace) for word in sentence]
    sentence=[word for word in sentence if len(word)>1 or (word.lower()=='a' or word.lower()=='i')]

    return sentence

def cleanput(content):  #줄바꿈 문자와 인용 기호를 제거, 마침표 뒤에 공백이 나타나는 것을 기준으로 텍스트를 문장으로 분할
    content=content.upper()
    content=re.sub('\n|[[d+]]', ' ', content)   #줄바꿈 문자 제거
    content=bytes(content, 'UTF-8') #인용 기호 제거
    content=content.decode('ascii', 'ignore')

    sentences=content.split('. ')   #마침표 뒤에 공백이 나타나는 것을 기준으로 문장 분할
    return [cleanSentence(sentence) for sentence in sentences]  
    #cleanSentence-> 문장을 단어로 분할, 구두점과 공백을 제거, 한 글자로 이루어진 단어(i와 a를 제외한)를 제거.

def getNgramsFromSentence(content, n):  
    #n-그램을 만드는 핵심 기능-> getNgrams에서 매 문장마다 호출함-> 문장엘 철치는 n-그램의 생성 방지
    output=[]
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

def getNgrams(content, n):  #기본적인 진입점 역할
    content=cleanput(content)
    ngrams=[]
    for sentence in content:
        ngrams.extend(getNgramsFromSentence(sentence, n))
    return(ngrams)