#신경망의 추론

#신경망 추론 전체 그림
'''
신경망은 간단히 말하면 단순한 '함수'라고 할 수 있다.
신경망도 함수처럼 입력을 출력으로 변환한다.

2차원 데이터를 입력하여 3차원 데이터를 출력하는 함수가 있다고 가정한다.
이 함수를 신경망으로 구현하려면 입력층input_layer에는 뉴런 2개, 출력층output_layer에는\
3개를 각각 준비한다.
은닉층hidden_layer(중간층)에는 적당한 수의 뉴런을 배치한다.

화살표에는 가중치weight가 존재하여, 그 가중치와 뉴런의 값을 각각 곱해서 그 합이\
다음 뉴런의 입력으로 쓰인다.(그 합에 활성화 함수activation function를 적용한 값이 다음 뉴런의 입력이 된다.)
각 층에서 이전 뉴런의 값에 영향받지 않는 정수도 더해진다.(편향bais)

신경망은 인접하는 층의 모든 뉴런과 연결(화살표로 이어진)되어 완전연결 계층fully connected layer라고 한다.


신경망이 수행하는 계산을 수식으로 나타내본다.

h_1=w_1*w_11+x_2*w_21+b_1

입력층의 데이터:(x_1, x_2)
가중치:w_11, w_21
편향:b_1
h_1:은닉층의 첫 번째 뉴런

완전연결 계층이 수행하는 변환은 행렬의 곱을 이용해 정리할 수 있다.

(h_1, h_2, h_3, h_4)=(x_1, x_2)(w_11 w_12 w_13 w_14)+(b_1, b_2, b_3, b_4)

다음처럼 간소화할 수 있다.

h= xW + b 


지금까지는 하나의 샘플 데이터(입력 데이터)만을 대상으로 하지만,\
실제로 신경망의 추론이나 학습에는 다수의 샘플 데이터(미니 배치minibatch)를 한꺼번에 처리한다.
-> 행렬의 행 각각에 샘플 데이터를 하나씩 저장해야 한다.
-> 형상 확인을 통해 각 미니배치가 올바르게 변환되었는지 확인한다.
-> N개의 샘플 데이터가 한번에 완전연결계층에 의해 변환되고, 은닉층에는 N개 분의 뉴런이 함께 계산된다.
'''
import numpy as np

W1=np.random.randn(2,4) #가중치
b1=np.random.randn(4)   #편향
x=np.random.randn(10,2) #입력 데이터(10개의 샘플 데이터를 각각 완전연결계층으로 변환)
h=np.matmul(x,W1)+b1    #b1의 덧셈은 브로트캐스트된다.b1의 형상은 (4,)이지만 자동으로 (10,4)로 복제된다.
print(h)
# [[ 0.19250524  2.13526263 -0.04825555  3.30105481]
#  [ 0.03947488  1.95230512  0.25280997  2.78514467]
#  [ 0.89432969 -1.17342427  1.33437642  1.60983237]
#  [ 0.68748271 -0.96802787  1.43971856  1.3553101 ]
#  [ 0.88885024 -1.45588462  1.52897606  1.32146926]
#  [ 1.39324279 -2.53227122  1.65553851  1.37914122]
#  [-0.35414347  1.97349861  0.69955253  1.93920274]
#  [-1.29059205  4.21474259  0.30279143  2.06967088]
#  [ 0.65143234 -0.15487006  0.94017589  2.07135256]
#  [ 0.5800969  -0.29465675  1.11682832  1.77754822]]
'''
완전연결계층에 의한 변환은 '선형'이다.
여기에 '비선형' 효과를 부여하는 것이 활성화 함수이다.
비선형 활성화 함수를 이용함으로써 신경망의 표현력을 높일 수 있다.
대표적으로 시그모이드sigmoid 함수가 있다.

임의의 실수를 입력받아 0~1 사이의 실수를 출력한다.
'''
def sigmoid(x):
    return 1/(1+np.exp(-x))

#시그모이드 함수를 이용해 은닉층 뉴런을 변환한다.
a=sigmoid(h)
print(a)
'''
활성화 함수의 출력 a(활성화activation)를 또 다른 완전연결계층에 통과시켜 변환한다.
예제에서 은닉층 뉴런은 4개, 출력층 뉴런은 3개이므로 완전연결계층에 사용되는 가중치\
행렬은 4x3 형상으로 설정해야 한다.
'''
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

x=np.random.randn(10,2) #2차원 데이터 10개가 미니배치로 처리된다.
W1=np.random.randn(2,4)
b1=np.random.randn(4)
W2=np.random.randn(4,3) #완전연결된 가중치 행렬은 (4,3)이어야 한다.
b2=np.random.randn(3)

h=np.matmul(x,W1)+b1    #은닉층의 뉴런 계산
a=sigmoid(h)    #활성화(시그모이드 함수)
s=np.matmul(a,W2)+b2    
#형상:(10,3)-> 10개의 데이터가 한번에 처리되었고(미니배치), 각 데이터는 3차원 데이터로 변환되었다.

'''
이 신경망은 3차원 데이터를 출력한다.
-> 각 차원의 값을 이용해서 3 클래스 분류할 수 있다.
-> 출력된 3차원 벡터의 각 차원은 각 클래스에 대응하는 점수score가 된다.
-> 실제로 분류를 한다면 출력층에서 가장 큰 값을 내는 뉴런에 해당하는 클래스가 예측 결과가 된다.
'''