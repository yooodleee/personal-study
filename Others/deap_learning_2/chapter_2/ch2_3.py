#단어의 분산 표현

'''
단어도 벡터로 표현할 수 있을까?
간결하고 이치에 맞는 벡터 표현을 단어라는 영역에서도 구축할 수 있을까?
-> 단어의 의미를 정확하게 파악할 수 있는 벡터 표현(분산 표현distributional represcentation)

단어의 분산 표현은 단어를 고정 길이의 밀집 벡터dense vector로 표현한다.
밀집벡터는 대부분의 원소가 0이 아닌 실수인 벡터를 말한다.
-> 단어의 분산 표현은 어떻게 구축할 것인가를 살펴본다.
'''

#분포 가설

'''
단어의 의미는 주변 단어에 의해 형성된다.
-> 분포 가설distributional hypothesis

단어 자체에는 의미가 없고, 그 단어가 사용된 맥락context이 의미를 형성한다는 것이다.
물론 의미가 같은 단어들은 같은 맥락에서 더 많이 등장한다.
-> 맥락이라 하면 (주목하는 단어)주변에 놓인 단어를 가리킨다.
-> 맥락의 크기 (주변 단어를 몇 개나 포함할지)를 윈도우 크기window size라고 한다.
-> 윈도우 크기가 1이면 좌우 한 단어씩, 윈도우 크기가 2라면 좌우 2단어씩 맥락에 포함된다.
'''

#동시발생 행렬

'''
분포 가설에 기초해 단어를 벡터로 나타내는 방법을 생각해본다.
주변 단어를 세어보는 방법이 자연스럽게 떠오른다.
어떤 단어에 주목했을 때, 그 주변에 어떤 단어가 몇 번이나 등장하는가를 집계하는 방법이다.
-> 통계 기반stastical based 기법이라고 한다.
'''
import sys
sys.path.append('..')
import numpy as np
from util import preprocess

text='You say goodbye and I say hello.'

corpus, word_to_id, id_to_word=preprocess(text)
print(corpus)   #단어의 총 수는 7개
#[0 1 2 3 4 1 5 6]

print(id_to_word)   
#{0: 'you', 1: 'say', 2: 'goodbye', 3: 'and', 4: 'i', 5: 'hello', 6: '.'}

'''
윈도우 크기는 1로 하고, 단어 ID가 0인 'YOU'부터 시작해본다.
단어 'YOU'의 맥락은 'say'라는 단어 하나뿐이다.
-> 'YOU'라는 단어를 [0, 1, 0, 0, 0, 0, 0]이라는 벡터로 표현할 수 있다.

마찬가지로, 'say'에 대해서도 동일한 과정을 수행한다.
-> [1, 0, 1, 0, 1, 1, 0]으로 표현할 수 있다.

모든 단어에 대해 동시발생하는 단어를 정리해본다.
각 행은 해당 단어를 표현한 벡터가 된다.
이 표가 행렬의 형태를 띤다는 뜻에서 동시발생 행렬co-occurrnece matrix라고 한다.

동시발생 행렬을 사용하면 각 단어의 벡터를 얻을 수 있다.
'''
c=np.array([
    [0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0]
], dtype=np.int32)

print(c[0]) #ID가 0인 단어의 벡터 표현
#[0 1 0 0 0 0 0 0]

print(c[4]) #ID가 4인 단어의 벡터 표현
#[0 1 0 1 0 0 0]

print(c[word_to_id['goodbye']]) #'goodbye'의 벡터 표현
#[0 1 0 1 0 0 0]

'''
동시발생 행렬을 수동으로 만들수도 있지만, 자동화할 수도 있다.
말뭉치로부터 공시발생 행렬을 만들어주는 함수를 구현해본다.
'''

def create_co_matrix(corpus, vocab_size, window_size=1):#단어ID의 리스트, 어휘수, 윈도우크기
    corpus_size=len(corpus)
    co_matrix=np.zeros((vocab_size, vocab_size), dtype=np.int32)#0으로 채워진 2차원 배열로 초기화

    for idx, word_id in enumerate(corpus):
        for i in range(1, window_size+1):   #말뭉치의 모든 단어 각각에 대해 윈도우에 포함된 주변 단어를 세어간다.
            left_idx=idx-i  #왼쪽 단어를 비교
            right_idx=idx+i #오른쪽 단어를 비교

            if left_idx>=0:
                left_word_id=corpus[left_idx]
                co_matrix[word_id, left_word_id]+=1

            if right_idx> corpus_size:
                right_word_id=corpus_size[right_idx]
                co_matrix[word_id, right_word_id]+=1
    return co_matrix


#벡터 간 유사도

'''
벡터 사이의 유사도를 측정하는 방법은 다양하다.
단어의 유사도를 나타낼 때는 코사인 유사도cosine similarity를 자주 이용한다.

x=(x1,x2,x3,...,xn)
y=(y1,y2,y3,...,yn)
=> similarity(x,y)=x*y/(||x||*||y||)=(x1*y1+....+xn*yn)/sqrt(x1**2+...+xn**2)*sqrt(y1**2+...+yn**2)

벡터의 분자에는 내적이, 분모에는 각 벨터의 노름norm이 등장한다.
노름은 벡터의 크기를 나타낸 것으로, L2노름을 계산한다.
(L2 노름은 벡터의 각 원소를 제곱해 더한 후 다시 제곱근을 구해 계산한다.)

-> 벡터를 정규화하고 내적을 구하는 것이 핵심이다.
-> 두 벡터가 가리키는 방향이 비슷한 정도를 나타낸다.
-> 1이면 두 벡터의 방향이 완전히 같고, -1이면 서로 다른 방향을 가리킨다.(반대 방향)
'''
def cos_similarity(x, y):
    nx=x/np.sqrt(np.sum(x**2))  #x의 정규화
    ny=y/np.sqrt(np.sum(y**2))  #y의 정규화
    return np.dot(nx, ny)

'''
위 코드에서 인수 x와 y를 넘파이 배열이라고 가정한다.
먼저 벡터 x와 y를 정규화한 후 벡터의 내적을 구한다.
이렇게만 해도 코사인 유사도를 구할 수 있지만, 이 구현에는 문제점이 한가지 있다.
-> 인수로 제로 벡터(원소가 모두 0인 벡터)가 들어오면 '0으로 나누기divide by zero'오류가 발생한다.

이 문제를 해결하는 전통적인 방법은 나눌 때 분모에 작은 값을 더해주는 것이다.
작은 값을 뜻하는 eps를 인수로 받도록 하고, 이 인수의 값을 지정하지 않으면 기본값으로\
le-8(0.00000001)이 설정되도록 수정한다.
'''
def cos_similarity(x, y, eps=1e-8):
    nx=x/(np.sqrt(np.sum(x**2))+eps)
    ny=y/(np.sqrt(np.sum(y**2))+eps)
    return np.dot(nx, ny)

'''
작은 값으로 1e-8을 사용했는데, 이 정도 작은 값이면 일반적으로 부동소수점 계산 시 '반올림'되어\
다른 값에 흡수된다.
이 값이 벡터의 노름에 흡수되기 때문에 대부분의 경우 eps를 더한다고 해서 최종 계산 결과에 영향을\
주지는 않는다.

벡터의 노름이 0일 때는 이 작은 값이 그대로 유지되어 '0으로 나누기' 오류가 나는 사태를 막아준다.
'''
import sys
sys.path.append('..')
from util import preprocess, create_co_matrix, cos_similarity

text='You say goodbye and I say hello.'
corpus, word_to_id, id_to_word=preprocess(text)
vocab_size=len(word_to_id)
C=create_co_matrix(corpus, vocab_size)

c0=C[word_to_id['you']] #you의 단어 벡터
c1=C[word_to_id['i']]   #i의 단어 벡터
print(cos_similarity(c0, c1))   #코사인 유사도
#0.7071067691154799


#유사 단어의 랭킹 표시

'''
어떤 단어가 검색어로 주어지면, 그 검색어와 비슷한 단어를 유사도 순으로 출력하는 함수를 구현한다.
most_similarity(query, word_to_id, id_to_word, word_matrix, top=5)
'''

def most_similarty(query, word_to_id, id_to_word, word_matrix, top=5):#검색어(단어), top=상위 몇 개까지 출력할지 설정
    #(1) 검색어를 꺼낸다.(검색어의 단어 벡터)
    if query not in word_to_id:
        print('%s(을)를 찾을 수 없습니다.'%query)   
        return 
    print('\n[query]'+query)
    query_id=word_to_id[query]  #검색어의 아이디
    query_vec=word_matrix[query_id] #검색어의 단어 벡터

    #(2) 코사인 유사도 계산
    vocab_size=len(id_to_word)
    similarity=np.zeros(vocab_size)
    for i in range(vocab_size):
        similarity[i]=cos_similarity(word_matrix[i], query_vec)
    
    #(3) 코사인 유사도를 기준으로 내림차순으로 출력
    count=0
    for i in (-1*similarity).argsort(): 
        #similarity 배열을 내림차순으로 정렬한 후 상위 원소들(인덱스)을 출력
        #argsort-> 단어의 유사도가 높은 순서로 출력할 수 있음
        if id_to_word[i]==query:
            continue
        print('%s:%s'%(id_to_word[i], similarity[i]))

        count+=1
        if count>=top:
            return 
        

import sys
sys.path.append('..')
from util import preprocess, create_co_matrix, most_similar

text='You say goodbye and I say hello.'
corpus, word_to_id, id_to_word=preprocess(text)
vocab_size=len(word_to_id)
C=create_co_matrix(corpus, vocab_size)

most_similar('you', word_to_id, id_to_word, C, top=5)   #query(검색어):you
# [query] you
#  goodbye: 0.7071067691154799
#  i: 0.7071067691154799
#  hello: 0.7071067691154799
#  say: 0.0
#  and: 0.0

'''
you에 가장 가까운 단어는 차례로 'goodbye', 'i(=I)', 'hello'이다.
'i'와 'you'는 인칭대명사이므로 둘이 비슷하다는 것은 납득이 가나, goodbye와 hello의 유사도가\
높다는 것은 우리의 직관과는 거리가 멀다.
-> 말뭉치의 크기가 너무 작다는 것이 원인이다.
'''