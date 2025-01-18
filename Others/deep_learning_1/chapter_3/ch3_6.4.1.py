#배치 처리의 구현
import sys, os
sys.path.append(os.pardir)
import numpy as np
from mnist import load_mnist
from PIL import Image
import pickle

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(a):
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

x, t=get_data()
network=init_network()

batch_size=100  #배치 크기  
accuracy_cnt=0  

for i in range(0, len(x), batch_size):  #range(start,end-1) 반복자 iterator
    x_batch=x[i:i+batch_size]   #배치-> 입력 데이터의 i번째~i+batch_size번째까지 데이터를 묶음
    y_batch=predict(network, x_batch)
    p=np.argmax(y_batch, axis=1)    
    #최댓값의 인덱스를 가져온다, axis-> 100x10의 배열 중 1번째 차원을 구성하는 각 원소에서(1번째 차원을 축으로)
    accuracy_cnt+=np.sum(p==t[i:i+batch_size])

print('Accuracy:'+str((accuracy_cnt)/len(x)))

x=np.array([[0.1,0.8,0.1],[0.3,0.1,0.6],
            [0.2,0.5,0.3],[0.8,0.1,0.1]])
y=np.argmax(x, axis=1)
print(y)

y=np.array([1,2,1,0])   #배치 단위로 분류한 결과를 실제 답과 비교.
t=np.array([1,2,0,0])
print(y==t) #   ==연산자를 사용해 넘파이 배열끼리 비교-> True, False로 구성된 bool 배열
#[True, True, False, True]

np.sum(y==t)    #True의 개수
#3