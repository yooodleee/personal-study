#정확도accuracy(분류도가 얼마나 올바른가)도 평가해보자.
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
        network=pickle.load(f)  
        #pickle 파일인 sample_weight.pkl에 저장된 '학습된 가중치 매개변수'

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

x,t=get_data()
network=init_network()  #MNIST 데이터셋을 얻고 네트워크를 생성한다.

accuaracy_cnt=0
for i in range(len(x)): 
    #for 문을 돌며 x에 저장된 이미지 데이터를 1장 씩 꺼내 predict() 함수로 분류
    y=predict(network, x[i])    
    p=np.argmax(y)  
    #확률이 가장 높은 원소의 인덱스(예측 확률)를 얻는다./각 레이블의 확률을 넘파이 배열로 반환한다.
    if p ==t[i]:
        accuaracy_cnt+=1    #신경망이 예측한 답변과 정답 레이블을 비교하여 맞힌 숫자를 셈.

print('Accuracy: '+str(float(accuaracy_cnt)/len(x)))    #전체 이미지 숫자로 나눠 정확도를 구함.

'''
데이터를 측정 범위로 변환하는 처리-> 정규화 normalization
신경망의 입력 데이터에 특정 변환을 가하는 것-> 전처리 pre-processing

데이터 전체 평균과 표준 편차를 이용하여 데이터들이 0을 중심을 분포하도록 이동하거나\
데이터의 확산 범위를 제한하는 정규화를 수행한다.
전체 데이터를 균일하게 분포시키는 것-> 데이터 백색화 whitening
'''