#markov-> 특정 사건이 다른 특정 사건에 뒤이어, 일정 확률로 일어나는 대규모 무작위 분포를 분석

'''
각 노드에서 출발하는 확률의 합은 반드시 100%.
시스템이 아무리 복잡하더라도, 반드시 항상 다음 단계로 넘어가야 한다.

구현되는 모델은 무한히 길어질 수 있다.
다음 단계에 영향을 미치는 것은 오직 현재 노드의 상태 뿐이다.

특정 노드는 다른 노드에 비해 도달하기 어렵다.

'''
from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum=0
    for word, value in wordList.items():
        sum+=value
    return sum

def retrieveRandomWord(wordList):
    randIndex=randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex-=value
        if randIndex<=0:
            return word

def buildWordDict(text):
    #줄바꿈 문자와 따옴표를 제거한다.
    text=text.replace('\n', ' ')
    text=text.replace('"', '')

    #구두점 역시 단어로 취급해서 마르코프 체인에 들어가도록 한다.
    punctuation=[',', '.', ';', ':']
    for symbol in punctuation:
        text=text.replace(symbol, '{} '.format(symbol)) 
        #따옴표를 제외한 다른 구두점 주위에 공백을 넣어 단어로 취급.
    
    word=text.split(' ')
    #빈 단어를 제거한다.
    words=[word for word in words if word!='']  

    wordDict={} #2차원 딕셔너리-> 딕셔너리의 딕셔너리
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            #이 단어에 필요한 새 딕셔너리를 만든다.
            wordDict[words[i-1]]={}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]]=0
        wordDict[words[i-1]][word[i]]+=1
    return wordDict

speech='http://pythonscraping.com/files/inaugurationSpeech.txt'
text=str(urlopen(speech).read(), 'utf-8')
wordDict=buildWordDict(text)

#길이가 100인 마르코프 체인을 생성한다.
length=100
chain=['I']

for i in range(0, length):
    newWord=retrieveRandomWord(wordDict[chain[-1]])
    chain.append(newWord)

print(' '.join(chain))