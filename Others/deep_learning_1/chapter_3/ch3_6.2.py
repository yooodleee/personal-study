#신경망의 추론 처리
'''
입력층 뉴런을 784(28x28)개, 출력층 뉴런을 10(0~9)개로 구성함.
은닉층이 총 2개로, 첫 번째 은닉층에는 50개의 뉴런을, 두 번째 은닉층에는 100개의 뉴런을 배치할 것이다.
'''
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