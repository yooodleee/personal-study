#통계 기반 기법 개선하기

#상호정보량

'''
동시발생 행렬의 원소는 두 단어가 동시에 발생한 횟수를 나타낸다.
그러나 발생 횟수라는 것은 그리 좋은 특징이 아니다.
고빈도 단어(많이 빈출하는 단어)로 이해하면 그 이유를 알 수 있다.

단순히 등장 횟수만을 본다면 관련성이 훨씬 강하다고 오해할 수 있다.
고빈도 단어라서 강한 관련성을 갖는다고 판단할 수 있다.

이 문제를 해결하기 위해 점별 상호정보량pointwise Mutual information(PMI)라는 척도를 사용한다.
확률 변수 x와 y에 대해 다음 식으로 정의된다.

PMI(x, y)=log_2 P(x, y)/p(x)*p(y)

x가 일어날 확률, y가 일어날 확률, x,y가 동시에 일어날 확률을 의미한다.
이 PMI가 높을수록 관련성이 높다는 의미이다.

위 식을 자연어 예에 적용하면 P(x)는 단어 x가 말뭉치에 등장할 확률을 나타낸다.
10,000개의 단어로 이뤄진 말뭉치에 the가 100번 등장한다면 P(the)=100/10,000=0.01이다.
또한 P(x,y)는 단어 x와 y가 동시발생할 확률로, the와 car가 10번 동시 발생했다면 P('the', 'car')=0.001dlek.

동시발생 행렬(각 원소는 동시발생한 단어의 횟수)을 사용하여 다시 써본다.
C는 동시발생 행렬, C(x,y)는 x,y가 동시발생하는 횟수, C(x), C(y)는 각각 단어의 등장 횟수이다.
이때 말뭉치에 포함된 단어의 수를 N이라 하면

PMI(x,y)=log_2 P(x,y)/P(x)*P(y)=log_2 C(x,y)*N/C(x)*C(y)

-> 단어가 단독으로 출현하는 횟수가 고려되었다.
-> 하지만, PMI는 두 단어의 동시발생 횟수가 0이면 log_2 0=-무한이 된다는 단점이 있다.
-> 실제로 구현할 때는 양의 상호정보량Positive PMI(PPMI)를 사용한다.

PPMI(x,y)=max(0, PMI(x, y))

-> PMI가 음수일 때는 0으로 취급한다.
'''
import numpy as np

def ppmi(C, verbose=False, eps=1e-8):   #동시발생행렬, 진행상황 출력여부 결정하는 플래그
    #voerbose=True일 경우, 중간중간 진행상황을 알려준다.
    #동시발생 행렬에 대해서만 PPMI 행렬을 구할 수 있도록 하고자 단순화했다.
    M=np.zeros_like(C, dtype=np.float32)
    N=np.sum(C)
    S=np.sum(C, axis=0)
    total=C.shape[0]*C.shape[1]
    cnt=0

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            pmi=np.log2(C[i, j]*N/(S[j]*S[i])+eps)  #lot2(0)이 음의 무한대(-inf)가 되는 것을 방지
            M[i, j]=max(0, pmi)

            if verbose: #verbose=False
                cnt+=1
                if cnt%(total//100+1)==0:
                    print('%.1f%% 완료' %(100*cnt/total))
    return M

import sys
sys.path.append('..')
import numpy as np
from util import preprocess, create_co_matrix, cos_similarity

text='You say goodbye and i say hello.'
corpus, word_to_id, id_to_word=preprocess(text)
vocab_size=len(word_to_id)
C=create_co_matrix(corpus, vocab_size)  #단어의 동시발생 행렬
W=ppmi(C)   #동시발생 행렬에 대해 PPMI 실행

np.set_printoptions(precision=3)    #유효자릿수를 세 자리로 표시
print('동시발생 행렬')
print(C)
print('-'*50)
print('PPMI')
print(W)

# #동시발생 행렬
# [[0 1 0 0 0 0 0]
#  [1 0 1 0 1 1 0]
#  [0 1 0 1 0 0 0]
#  [0 0 1 0 1 0 0]
#  [0 1 0 1 0 0 0]
#  [0 1 0 0 0 0 1]
#  [0 0 0 0 0 1 0]]
# --------------------------------------------------
# PPMI
# [[0.    1.807 0.    0.    0.    0.    0.   ]
#  [1.807 0.    0.807 0.    0.807 0.807 0.   ]
#  [0.    0.807 0.    1.807 0.    0.    0.   ]
#  [0.    0.    1.807 0.    1.807 0.    0.   ]
#  [0.    0.807 0.    1.807 0.    0.    0.   ]
#  [0.    0.807 0.    0.    0.    0.    2.807]
#  [0.    0.    0.    0.    0.    2.807 0.   ]]

'''
PPMI 행렬의 각 원소는 0 이상의 실수이다.
더 좋은 척도로 이뤄진 행렬(더 좋은 단어 벡터)를 손에 얻었다.

그러나, 여전히 PPMI에도 문제가 있다.
말뭉치의 어휘 수가 증가함에 따라 각 단어 벡터의 차원 수도 증가한다.
말뭉치의 어휘 수가 10만 개라면 그 벡터의 차원 수도 똑같이 10만이 된다.
-> 10만 차원의 벡터를 다룬다는 것은 그다지 현실적이지 않다.

또한, 위 행렬의 원소 대부분이 0인 것을 알 수 있다.
벡터이 원소 대부분이 중요하지 않다는 뜻이다.
다르게 표현하면 각 원소의 중요도가 낮다는 뜻이다.

더구나 벡터는 노이즈에 약하고 견고하지 못하다는 약점도 존재한다.
이 문제에 대처하고자 자주 수행하는 기법이 벡터의 차원 감소이다.
'''

#차원 감소

'''
차원 감소dimmensionality reduction는 벡터의 차원을 줄이는 방법이다.
그러나 단순히 줄이기만 하는 것이 아니라, 중요한 정보는 최대한 유지하면서 줄이는 게 핵심이다.
-> 데이터의 분포를 고려해 중요한 축을 찾는 일을 수행한다.

ex) 차원 감소: 2차원 데이터를 1차원으로 표현하기 위해 중요한 축(데이터를 넓게 분포시키는 축)을 찾는다.
이때 각 데이터 점의 값은 새로운 축으로 사영된 값으로 변한다.
-> 1차원 값만으로도 데이터의 본질적인 차이를 구별할 수 있어야 한다.
-> 위 작업은 다차원 데이터에 대해서도 수행할 수 있다.

*희소 행렬/희소 벡터sparse matrix/vector

원소 대부분이 0인 행렬, 벡터.
차원 감소의 핵심은 희소 백터에서 중요한 축을 찾아내 더 적은 차원으로 다시 표현하는 것이다.
차원 감소의 결과로 원래의 희소 벡터는 원소 대부분이 0이 아닌 값으로 구성된 밀집 벡터로 변환된다.
-> 이 조밀한 벡터야말로 우리가 원하는 단어의 분산 표현이다.

차원을 감소시키는 방법은 여러가지인데, 여기서는 특잇값분해Singular Value Decomposition(SVD)를 사용한다.
SVD는 임의의 행렬을 세 행렬의 곱으로 분해하며, 수식으로는 다음과 같다.

X=USV^T

SVD는 임의의 행렬 U, S, V라는 세 행렬의 곱으로 분해한다.
여기서 U와 V는 직교행렬orthogonal matrix이고, 그 열벡터는 서로 직교한다.
또한 S는 대각행렬diagonal matrix(대각성분외에는 모두 0)이다.

직교행렬 U는 어떠한 공간의 축(기저)을 형성한다.
여기서 U 행렬을 '단어 공간'이라고 취급할 수 있다.
또한, S는 대각행렬로, 그 대각성분에는 '특잇값singular value'이 큰 순서로 나열되어 있다.

-> 특잇값이란, '해당 축'의 중요도라고 간주할 수 있다.
-> 중요도가 낮은 원소(특잇값이 작은 원소)를 깎아내는 방법을 생각할 수 있다.

행렬 S에서 특잇값이 작다면 중요도가 낮다는 뜻이므로, 행렬 U에서 여분의 열벡터를 깎아내어\
원래의 행렬을 근사할 수 있다.
이를 단어의 PPMI 행렬에 적용해본다면, 행렬 X의 각 행에는 해당 단어 ID의 단어 벡터가 저장되어 있으며,\
그 단어 벡터가 행렬 U라는 차원 감소된 벡터로 표현되는 것이다.
'''