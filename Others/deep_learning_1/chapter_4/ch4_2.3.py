#미니배치 학습
'''
기계학습 문제는 훈련 데이터를 사용해 학습한다.
-> 훈련 데이터에 대한 손실 함수의 값을 구하고, 그 값을 최대한 줄여주는 매개변수를 찾아낸다.
-> 모든 훈련 데이터를 대상으로 손실 함수 값을 구해야 한다.

E=-(1/N) sigma sigma {(t_n*k)*(log y_n*k)}

데이터가 N개라면 t_nk는 n 번째 데이터의 k번째 값을 의미한다.
(y_nk는 신경망의 출력, t_nk는 정답 레이블)

수식이 복잡해보이지만 데이터 하나에 대한 손실 함수를 단순히 N개의 데이터로 확장한 것이다.
N으로 나눔으로써 '평균 손실 함수'를 구하는 것이다.
-> 평균을 구해 사용하면 데이터 개수와 관계없이 언제든 통일된 지표를 얻을 수 있다.

하지만 데이터가 수없이 많은 경우 데이터 일부를 추려 전체의 '근사치'로 이용할 수 있다.
신경망 학습에서도 훈련 데이터로부터 일부만 골라 학습을 수행한다.
이 일부를 미니배치mini-batch라고 한다.
'''
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset import load_mnist  

(x_train, y_train), (x_test, y_test)=\
    load_mnist(normalize=True, one_hot_label=True)  #정답 위치의 원소만 1(원-핫 인코딩)
    #load_mnist-> MNIST 데이터셋을 읽어 오는 함수(훈련데이터, 시험데이터를 읽음)

print(x_train.shape)    #(60000, 784)-> 훈련 코드는 60000개, 입력데이터는 784열(28x28)
print(y_train.shape)    #(60000, 10)-> 훈련 데이터에서 무작위로 10장만 빼래려면