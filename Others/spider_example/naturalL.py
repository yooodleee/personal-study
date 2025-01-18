#데이터 요약
#불필요한 단어들을 자동으로 걸러내는 방법
from urllib.request import urlopen
import re
import string
from collections import Counter

def cleanSentence(sentence):
    sentence=sentence.split(' ')
    sentence=[word.strip(string.punctuation+string.whitespace) for word in sentence]
    sentence=[word for word in sentence if len(word)>1 or word.lower()=='a' or word.lower()=='i']

    return sentence

def cleanInput(content):
    content=content.upper() #대문자로 
    content=re.sub('\n', ' ', content)  #이스케이프 문자
    content=bytes.decode('ascii', 'ignore') 
    
    sentences=content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]

def getNgramsFromSentence(content, n):
    output=[]
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    
    return output

def getNgrams(content, n):
    content=cleanInput(content)
    ngrams=Counter()
    ngrams_list=[]
    for sentence in content:
        newNgrams=[' '.join(ngram) for ngram in getNgramsFromSentence(sentence, n)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)
    return(ngrams)

speech='http://pythonscraping.com/files/inaugurationSpeech.txt'
content=str(urlopen(speech).read(), 'utf-8')
ngrams=getNgrams(content, 2)
print(ngrams)