#배치 처리(입력 데이터와 가중치 매개변수의 '형상')
import sys, os
sys.path.append(os.pardir)
import numpy as np
from mnist import load_mnist
from PIL import Image
import pickle

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a

    return y

def get_data():
    (x_train, t_train), (x_test, t_test)=\
        load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open('sample_weight.pkl', 'rb') as f:
        network=pickle.load(f)  #pickle 파일인 sample_weight.pkl에 저장된 '학습된 가중치 매개변수'

        return network

def predict(network, x):
    W1, W2, W3=network['W1'], network['W2'], network['W3']
    b1, b2, b3=network['b1'], network['b2'], network['b3']

    a1=np.dot(x,W1)+b1
    z1=sigmoid(a1)
    a2=np.dot(z1, W2)+b2
    z2=sigmoid(a2)
    a3=np.dot(z2, W3)+b3
    y=softmax(a3)

    return y

x,_=get_data()
network=init_network()
W1, W2, W3=network['W1'], network['W2'], network['W3']

x.shape
#(10000, 784)

x[0].shape
#(784,)

W1.shape
#(784, 50)

W2.shape
#(50, 100)

W3.shape
#(100, 10)

'''
다차원 배열의 대응하는 차원의 수가 일치함을 확인할 수 있다(편향은 생략)
다차원 배열의 대응하는 차원의 원소 수가 일치한다.
최종 결과로는 원소가 10개인 1차원 배열 y가 출력된다.

x:      X       W1      W2      W3      ->      Y

형상:   784   784x50  50x100  100x10            10

전체적으로 보면 원소 784개로 구성된 1차원 배열(원래는 28x28인 2차원 배열)이\
입력되어 마지막에는 원소가 10개인 1차원 배열이 출력된다.
이는 이미지 데이터를 1장만 입력했을 때의 처리 흐름이다.

이미지를 여러 장을 한번에 입력하는 경우(100장)
-> 이미지 100개를 묶어 predict() 함수에 한 번에 넘긴다.
x의 형상을 100x784로 바꿔 100장 분량의 데이터를 하나의 입력 데이터로 표현하면 된다.

        X       W1      W2      W3      ->      Y

형상: 100x784 784x50  50x100  100x10          100x10

입력 데이터의 형상은 100x784, 출력 데이터의 형상은 100x10.
100장 분량의 입력 데이터의 결과가 한 번에 출력됨을 나타낸다.
x[0]와 y[0]에는 0번 째 이미지와 그 추론 결과가, x[1]과 y[1]에는 1번 째의 이미지와 그 결과가\
저장되는 식이다.

하나의 묶은 입력 데이터를 배치batch라고 한다.
이미지가 지폐처럼 다발로 묶여있음을 의미한다.
'''