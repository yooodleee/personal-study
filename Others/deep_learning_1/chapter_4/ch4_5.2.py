#미니배치 학습 구현하기
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from chapter_5.two_layer_net import TwoLayerNet

(x_train, t_train), (x_test, t_test)=\
    load_mnist(normalize=True, one_hot_label=True)

train_loss_init=[]

#하이퍼 파라미터
iters_num=10000 #반복 횟수
train_size=x_train.shape[0]
batch_size=100 
#미니배치 크기-> 60000개의 훈련 데이터에서 임의로 100개의 데이터(이미지 데이터와 정답 레이블 데이터)를 추려낸다.
learning_rate=0.1

network=TwoLayerNet(input_size=784, hidden_size=50, outout_size=10)

for i in range(iters_num):  #확률적 경사 하강법
    #미니배치 획득
    batch_mask=np.random.choice(train_size, batch_size)
    x_batch=x_train[batch_mask]
    t_batch=t_train[batch_mask]
    
    #기울기 계산
    grad=network.numerical_graident(x_batch, t_batch)

    #매개변수 갱신
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key]-=learning_rate*grad[key]

        #학습 경과 기록
        loss=network.loss(x_batch, t_batch)
        train_loss_init.append(loss)

'''
학습 횟수가 늘어가면서 손실 함수의 값이 줄어든다-> 학습이 잘 되고 있다.
신경망의 가중치 매개변수가 서서히 데이터에 적응하고 있음을 의미함
-> 데이터를 반복해서 학슴함으로써 최적 가중치 매개변수로 서서히 다가서고 있다.
'''