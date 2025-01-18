#MNIST 데이터셋으로 본 가중치 초기값 비교

'''
std=0.01, Xavier 초깃값, He 초깃값

층별 뉴런 수가 100개인 5층 신경망에서 활성화 함수로 ReLU를 사용했다.
std=0.01일 때 학습은 전혀 이뤄지지 않았다.
앞서 활성화 값의 분포에서 본 것처럼 순전파 때 너무 작은 값(0 근처로 밀집한 데이터)이 흐르기\
때문이다.
그로 인해 역전파 때 기울기도 작아져 가중치가 거의 갱신되지 않았다.

반대로 Xavier 초깃값과 He 초깃값의 경우는 학습이 순조롭게 이뤄지고 있다.
다만 학습 진도는 He 초깃값 쪽이 더 빠르다.

가중치의 초깃값은 신경망에서 아주 중요한 포인트이다.
가중치의 초깃값에 따라 신경망 학습에 영향이 미치기 때문이다.
'''
# coding: utf-8
import os
import sys

sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
from chapter_7.util import smooth_curve
from multi_layer_net import MultiLayerNet
from chapter_8.optimizer import SGD


# 0. MNIST 데이터 읽기==========
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

train_size = x_train.shape[0]
batch_size = 128
max_iterations = 2000


# 1. 실험용 설정==========
weight_init_types = {'std=0.01': 0.01, 'Xavier': 'sigmoid', 'He': 'relu'}
#std(표준편차), Xavier 초깃값(sigmoid 활성화 함수), He 초깃값(ReLU 활성화 함수)
optimizer = SGD(lr=0.01)    #확률적 경사 하강법(SGD), 학습률 lr

networks = {}
train_loss = {}
for key, weight_type in weight_init_types.items():
    networks[key] = MultiLayerNet(input_size=784, hidden_size_list=[100, 100, 100, 100],
                                  output_size=10, weight_init_std=weight_type)
    train_loss[key] = []


# 2. 훈련 시작==========
for i in range(max_iterations):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    for key in weight_init_types.keys():
        grads = networks[key].gradient(x_batch, t_batch)
        optimizer.update(networks[key].params, grads)
    
        loss = networks[key].loss(x_batch, t_batch)
        train_loss[key].append(loss)
    
    if i % 100 == 0:
        print("===========" + "iteration:" + str(i) + "===========")
        for key in weight_init_types.keys():
            loss = networks[key].loss(x_batch, t_batch)
            print(key + ":" + str(loss))


# 3. 그래프 그리기==========
markers = {'std=0.01': 'o', 'Xavier': 's', 'He': 'D'}
x = np.arange(max_iterations)
for key in weight_init_types.keys():
    plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.ylim(0, 2.5)
plt.legend()
plt.show()