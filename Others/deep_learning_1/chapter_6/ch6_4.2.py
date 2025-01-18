#가중치 감소
'''
오버피팅 억제용으로 이용하는 방법-> 가중치 감소weight decay
큰 가중치에 대해서는 그에 상응하는 큰 패널티를 부과하여 오버피팅을 억제한다.
원래 오버피팅은 가중치 매개변수 값이 커서 발생하는 경우가 발생하는 경우가 많다.

신경망 학습의 목적은 손실 함수의 값을 줄이는 것이다.
가중치의 제곱 노름norm(L2 노름)을 손실 함수에 더한다.
-> 가중치가 커지는 것을 억제할 수 있다.
-> 가중치 세기를 조절하는 하이퍼파라미터.
-> 람다를 크게 설정할수록 큰 가중치에 대한 패널티가 커진다.

*L2 노름

각 원소의 제곱들을 더한 것에 해당한다.
L2노름 외에 L1 노름과 L limit 노름도 있다.

L1 노름은 절댓값의 합에 해당하고, L limit 노름은 Max 노름이라고도 하며, 각 원소의 절댓값 중\
가장 큰 것에 해당한다.
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

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

# 오버피팅을 재현하기 위해 학습 데이터 수를 줄임
x_train = x_train[:300]
t_train = t_train[:300]

# weight decay（가중치 감쇠） 설정 =======================
#weight_decay_lambda = 0 # weight decay를 사용하지 않을 경우
weight_decay_lambda = 0.1
# ====================================================

network = MultiLayerNet(input_size=784, hidden_size_list=[100, 100, 100, 100, 100, 100], output_size=10,
                        weight_decay_lambda=weight_decay_lambda)
optimizer = SGD(lr=0.01) # 학습률이 0.01인 SGD로 매개변수 갱신

max_epochs = 201
train_size = x_train.shape[0]
batch_size = 100

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)
epoch_cnt = 0

for i in range(1000000000):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    grads = network.gradient(x_batch, t_batch)
    optimizer.update(network.params, grads)

    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)

        print("epoch:" + str(epoch_cnt) + ", train acc:" + str(train_acc) + ", test acc:" + str(test_acc))

        epoch_cnt += 1
        if epoch_cnt >= max_epochs:
            break


# 그래프 그리기==========
markers = {'train': 'o', 'test': 's'}
x = np.arange(max_epochs)
plt.plot(x, train_acc_list, marker='o', label='train', markevery=10)
plt.plot(x, test_acc_list, marker='s', label='test', markevery=10)
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()