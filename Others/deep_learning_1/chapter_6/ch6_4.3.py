#드롭아웃

'''
오버피팅을 억제하는 방식으로 손실 함수에 가중치의 L2 노름을 더한 가중치 감소를 사용했다.
그러나 신경망 모델이 복잡해지면 가중치 감소만으로는 대응하기 어려워진다.
-> 드롭아웃dropout 기법을 사용한다.

뉴런을 임의로 삭제하면서 학습하는 방법이다.
훈련 때 은닉층의 뉴런을 무작위로 골라 삭제한다.
삭제된 뉴런은 신호를 전달하지 않게 된다.
-> 훈련 때는 데이터를 흘릴 때마다 삭제할 때마다 삭제할 뉴런을 무작위로 선택하고,\
시험 때는 모든 뉴런에 신호를 전달한다.
-> 단, 시험 때는 각 뉴런의 출력에 훈련 때 삭제 안 한 비율을 곱해 출력한다.
'''
import os, sys
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
from multi_layer_net_extend import MultiLayerNetExtend
from trainer import Trainer

class Dropout:
    def __init__(self, dropout_ratio=0.5):
        self.dropout_ratio=dropout_ratio
        self.mask=None  #훈련 시에는 순전파 때마다 self.mask에 삭제할 뉴런을 False로 표시한다.
    
    def forward(self, x, train_flg=True):   
        #전처리할 때 train_flg=True일 때만 잘 계산해두면 시험 때는 단순히 데이터를 흘리기만 하면 된다.
        #삭제 안 한 비율은 곱하지 않아도 좋다.-> 실제로 딥러닝 프레임워크들도 비율을 곱하지 않는다.
        if train_flg:
            self.mask=np.random.rand(*x.shape)>self.dropout_ratio   
            #self.mask는 x와 형상이 같은 배열을 무작위로 생성하고, 그 값이 dropout_ratio보다 큰 원소만 True로 설정한다.
            #순전파 때 신호를 통과시키는 뉴런은 역전파 때도 신호를 그대로 통과시키고, 순전파 때 통과시키지 않은 뉴런은 역전파 때도 신호를 차단한다. 
            return x*self.mask
            #순전파 때 신호를 통과시키는 뉴런
        else:
            return x*(1.0-self.dropout_ratio)
            #드롭아웃된 뉴런(x*삭제 안 한 비율)
        
    
    def backward(self, dout):
        return dout*self.mask
        #순전파 때 통과시킨 뉴런은 역전파 때도 신호를 그대로 통과.

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

# 오버피팅을 재현하기 위해 학습 데이터 수를 줄임
x_train = x_train[:300]
t_train = t_train[:300]

# 드롭아웃 사용 유무와 비울 설정 ========================
use_dropout = True  # 드롭아웃을 쓰지 않을 때는 False
dropout_ratio = 0.2
# ====================================================

network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100, 100],
                              output_size=10, use_dropout=use_dropout, dropout_ration=dropout_ratio)
trainer = Trainer(network, x_train, t_train, x_test, t_test,
                  epochs=301, mini_batch_size=100,
                  optimizer='sgd', optimizer_param={'lr': 0.01}, verbose=True)
trainer.train()

train_acc_list, test_acc_list = trainer.train_acc_list, trainer.test_acc_list

# 그래프 그리기==========
markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, marker='o', label='train', markevery=10)
plt.plot(x, test_acc_list, marker='s', label='test', markevery=10)
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()