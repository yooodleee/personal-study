#배치 정규화의 효과
'''
배치 정규화를 사용할 때의 학습 진도가 빠른 것으로 나타난다.
실제로 배치 정규화를 사용하지 않고 초깃값이 잘 분포되어 있지 않으면 학습이 전혀 진행되지\
않을 수도 있다.
->배치 정규화를 사용하면 학습이 빨라지며, 가중치 초깃값에 크게 의존하지 않아도 된다.
'''
# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
from multi_layer_net import MultiLayerNetExtend
from chapter_8.optimizer import SGD, Adam

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

# 학습 데이터를 줄임
x_train = x_train[:1000]
t_train = t_train[:1000]

max_epochs = 20 #epoch(에폭) 최댓값=20
train_size = x_train.shape[0]   #행렬의 차원(0)
batch_size = 100    
learning_rate = 0.01    #학습률 lr


def __train(weight_init_std):
    #batch norm을 사용하는 경우-> 학습 향상
    bn_network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100], output_size=10, 
                                    weight_init_std=weight_init_std, use_batchnorm=True)
    #batch norm을 사용하지 않는 경우-> 학습 더딤
    network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100], output_size=10,
                                weight_init_std=weight_init_std)
    optimizer = SGD(lr=learning_rate)   #경사하강법(SGD)
    
    train_acc_list = []
    bn_train_acc_list = []
    
    iter_per_epoch = max(train_size / batch_size, 1)
    epoch_cnt = 0
    
    for i in range(1000000000):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]
    
        for _network in (bn_network, network):
            grads = _network.gradient(x_batch, t_batch) #기울기
            optimizer.update(_network.params, grads)    
    
        if i % iter_per_epoch == 0: #i가 epoch
            train_acc = network.accuracy(x_train, t_train)  #batch norm을 사용하지 않는 경우
            bn_train_acc = bn_network.accuracy(x_train, t_train)    #batch norm을 사용하는 경우
            train_acc_list.append(train_acc)
            bn_train_acc_list.append(bn_train_acc)
    
            print("epoch:" + str(epoch_cnt) + " | " + str(train_acc) + " - " + str(bn_train_acc))
    
            epoch_cnt += 1
            if epoch_cnt >= max_epochs: #epoch이 epoch의 최댓값=20일때 반복 탈출
                break
                
    return train_acc_list, bn_train_acc_list


# 그래프 그리기==========
weight_scale_list = np.logspace(0, -4, num=16)  #설정한 범위에서 로그로 분할한 위치 값 출력
x = np.arange(max_epochs)   #20

for i, w in enumerate(weight_scale_list):
    print( "============== " + str(i+1) + "/16" + " ==============")
    train_acc_list, bn_train_acc_list = __train(w)
    
    plt.subplot(4,4,i+1)    #행과 열 수 입력, 그래프 그리기
    plt.title("W:" + str(w))
    if i == 15:
        plt.plot(x, bn_train_acc_list, label='Batch Normalization', markevery=2)
        plt.plot(x, train_acc_list, linestyle = "--", label='Normal(without BatchNorm)', markevery=2)
    else:
        plt.plot(x, bn_train_acc_list, markevery=2)
        plt.plot(x, train_acc_list, linestyle="--", markevery=2)

    plt.ylim(0, 1.0)
    if i % 4:
        plt.yticks([])  #눈금 표시
    else:
        plt.ylabel("accuracy")
    if i < 12:
        plt.xticks([])
    else:
        plt.xlabel("epochs")
    plt.legend(loc='lower right')
    
plt.show()