#자연어 처리란

'''
자연어natural language

우리가 평소에 쓰는 말
-> 자연어 처리natural language processing(NLP)는 자연어를 처리하는 분야이고\
우리의 말을 컴퓨터에게 이해시키기 위한 기술(분야)
-> 자연어 처리가 추구하는 목표는 사람의 말을 컴퓨터가 이해하도록 만드는 것.
'''

#단어의 의미

'''
우리의 말은 '문자'로 구성되며, 말의 의미는 '단어'로 구성된다.
단어는 의미의 최소 단위이다.
-> 자연어를 컴퓨터에게 이해시키는 데는 무엇보다 '단어의 의미'를 이해시키는 것이 중요하다.

1) 시소러스를 활용한 기법
2) 통계 기반 기법
3) 추론 기반 기법(word2vec)

시소러스thesaurus(유의어 사전)을 이용하는 방법을 간단히 소개한다.

'단어의 의미'를 나타내는 방법으로는 먼저 사람이 직접 단어의 의미를 정의하는 방식을 생각할 수 있다.
각각의 단어에 그 의미를 설명해 넣을 수 있다.

시소러스란 (기본적으로는) 유의어 사전으로, '뜻이 같은 단어(동의어)'나 '뜻이 비슷한 단어(유의어)'\
가 한 그룹으로 분류되어 있다.

car=auto automobile machine motorcar
-> 동의어의 예(모두 자동차를 뜻하는 동의어이다.)

또한 자연어 처리에 이용되는 시소러스에서는 단어 사이의 '상위와 하위' 혹은 '전체와 부분' 등\
더 세세한 관계까지 정의해둔 경우가 있다.

object-> motor vehicle-> car/go-kart/truck-> SUV/compact/hatch-back

car의 상위 개념으로 motor vehicle(동력차)라는 단어가 존재한다.
car의 하위 개념으로 SUV(스포츠 유틸리티 자동차), compact(소형차), hatch-back 등의 차종이 있다.

이처럼 모든 단어에 대한 유의어 집합을 만든 다음, 단어들의 관계를 그래프로 표현하여 단어 사이의\
연결을 정의할 수 있다.
-> 단어 네트워크를 이용하여 컴퓨터에게 단어 사이의 관계를 가르칠 수 있다.
'''

#WorldNet

'''
WorldNet은 전통 있는 시소러스로, 지금까지 많은 연구와 다양한 자연어 처리 애플리케이션에서\
사용되고 있다.
이를 사용하면 유의어를 얻거나 '단어 네트워크'를 이용할 수 있다.
또한 단어 네트워크를 사용해 단어 사이의 유사도를 구할 수도 있다.
'''

#시소러스의 문제점

'''
시소러스에는 수많은 단어에 대한 동의어와 계층 구조 등의 관계가 정의돼 있다.
하지만 이처럼 사람이 수작업으로 레이블링하는 방식에는 큰 결점이 존재한다.

1) 시대 변화에 대응하기 어렵다.
2) 사람을 쓰는 비용은 크다.
3) 단어의 미묘한 차이를 표현할 수 없다.

-> 이를 해결하기 위해 '통계 기반 기법'과신경망을 사용한 '추론 기반 기법'을 알아본다.
대량의 텍스트 데이터로부터 '단어의 의미'를 자동으로 추출한다.
'''

#통계 기반 기법

'''
말뭉치corpus를 이용한다.
-> 대량의 텍스트
다만, 맹목적으로 수집된 텍스트 데이터가 아닌 자연어 처리 연구나 애플리케이션을 염두에\
두고 수집된 텍스트 데이터를 일반적으로 의미한다.

통계 기반 기법의 목적은 말뭉치에서 효율적으로 그 핵심을 추출하는 것에 있다.
자연어 처리에 사용되는 말뭉치에는 텍스트 데이터에 대한 추가 정보가 포함되는 경우가 있다.

예컨데 텍스트 데이터의 단어 각각에 '품사'가 레이블링될 수 있다.
이럴 경우 말뭉치는 컴퓨터가 다루기 쉬운 형태(트리 구조 등)로 가공되어 주어지는 것이 일반적이다.
'''

#파이썬으로 말뭉치 전처리하기

'''
파이썬의 대화 모드를 이용하여 매우 작은 텍스트 데이터(말뭉치)에 전처리preprocessing를 해본다.
전처리란, 데이터를 단어로 분할하고 그 분할된 단어들을 단어 ID 목록으로 변환하는 일이다.
'''
text='You say goodbye and I say hello.'
text=text.lower()   #모든 문자를 소문자로 변환-> 첫머리의 대문자로 시작하는 단어도 소문자로 취급
text=text.replace('.', ' .')#.(마침표)를 고려해 마침효 앞에 공백을 삽입('.'-> ' .')한 후 분할
print(text)
#you say goodbye and i say hello .

words=text.split(' ')#공백을 기준으로 분할
print(words)
#['you', 'say', 'goodbye', 'and', 'i', 'say', 'hello', '.']

'''
*정규표현식regular expression

정규표현식 모듈 re를 임포트하고 re.split('(W+)?'.text)라고 호출하면 단어 단위로 분할 가능하다.
'''

'''
원래의 문장을 단어 목록 형태로 이용할 수 있게 되었다.
단어 단위로 분할되어 다루기 쉬워진 것은 맞지만, 단어를 텍스트 그대로 조작하기란 아직 불편하다.
-> 단어에 ID를 부여하고, ID의 리스트로 이용할 수 있도록한 번 더 조작한다.
'''
word_to_id={}   #단어-> 단어ID
id_to_word={}   #단어ID-> 단어(키가 단어ID, 값이 단어)

for word in words:
    if word not in word_to_id:  #단어가 word_to_id에 들어 있지 않으면

        new_id=len(word_to_id)  
        #추가 시점의 딕셔너리 길이가 새로운 단어의 ID로 설정0> 단어 ID는 0,1,2,...식으로 증가함
        word_to_id[word]=new_id #새로운 ID를 추가
        id_to_word[new_id]=word #새로운 단어를 추가

print(id_to_word)
#{0: 'you', 1: 'say', 2: 'goodbye', 3: 'and', 4: 'i', 5: 'hello', 6: '.'}

print(word_to_id)
#{'you': 0, 'say': 1, 'goodbye': 2, 'and': 3, 'i': 4, 'hello': 5, '.': 6}

print(id_to_word[1])
#say

print(word_to_id['hello'])
#5

'''
'단어 목록'을 '단어 ID 목록'으로 변경한다.
파이썬의 내포comprehension을 사용하여 단어 목록에서 단어 ID 목록으로 변환한 다음, 넘파이 배열로 변환한다.
'''
import numpy as np

corpus=[word_to_id[w] for w in words]
corpus=np.array(corpus)
print(corpus)
#[0 1 2 3 4 1 5 6]

'''
말뭉치를 이용하기 위한 사전 준비를 모두 마쳤다.
이상의 처리를 한데 모아 preprocess() 함수로 구현해본다.
'''
def preprocess(text):
    text=text.lower()
    text=text.replace('.', ' .')
    words=text.split(' ')

    word_to_id={}
    id_to_word={}
    for word in words:
        if word not in word_to_id:
            new_id=len(word_to_id)
            word_to_id[word]=new_id
            id_to_word[new_id]=word
    
    corpus=np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word

text='You say goodbye and I say hello.'
corpus, word_to_id, id_to_word=preprocess(text)