#오버피팅overfitting

'''
오버피팅: 신경망이 훈련 데이터에만 지나치게 적응되어 그 외의 데이터에는\
제대로 대응하지 못하는 상태.
기계 학습은 범용 성능을 지향한다.
-> 훈련 데이터에는 포함되지 않는, 아직 보지 못하는 데이터가 주어져도 바르게 식별해내는 모델이 바람직하다.

1) 매개변수가 많고 표현력이 높은 모델
2) 훈련 데이터가 적음

오버피팅은 위 2가지 경우에 주로 발생한다.
'''
# coding: utf-8
import os
import sys

sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
from multi_layer_net import MultiLayerNet
from chapter_8.optimizer import SGD

(x_train, t_train), (x_test, t_test)=load_mnist(normalize=True)
#오버피팅을 재현하기 위해 학습 데이터 수를 줄임
x_train=x_train[:300]
t_train=t_train[:300]

network=MultiLayerNet(input_size=784, hidden_size_list=[100,100,100,100,100,100], output_size=10)
optimizer=SGD(lr=0.01)  #학습률lr=0.01인 SGD로 매개변수 갱신

max_epochs=201
train_size=x_train.shape[0]
batch_size=100

train_loss_list=[]
train_acc_list=[]
test_acc_list=[]

iter_per_epoch=max(train_size/batch_size, 1)
epoch_cnt=0

for i in range(100000000):
    batch_mask=np.random.choice(train_size, batch_size)
    x_batch=x_train[batch_mask]
    t_batch=t_train[batch_mask]

    grads=network.gradient(x_batch, t_batch)
    optimizer.update(network.params, grads)

    if i%iter_per_epoch==0:
        train_acc=network.accuracy(x_train, t_train)
        test_acc=network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)

        epoch_cnt+=1
        if epoch_cnt>=max_epochs:
            break

'''
훈련 데이터를 사용하여 측정한 정확도는 100 에폭을 지나는 무렵부터 거의 100%이다.
그러나 시험 데이터에 대해서는 큰 차이를 보인다.
-> 정확도가 크게 벌어지는 것은 훈련 데이터에만 적응fitting해버린 결과이다.

훈련 때 사용하지 않은 범용 데이터(시험 데이터)에는 제대로 대응하지 못한다.
'''