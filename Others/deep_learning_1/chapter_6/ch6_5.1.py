#검증 데이터
'''
훈련 데이터에만 지나치게 적응되어 있는 것이 아닌지(오버피팅되어 있는가)\
범용 성능은 어느 정도인지를 평가할 수 있었다.

하이퍼 파라미터의 성능을 평가할 때는 시험 데이터를 사용해서는 안 된다.
-> 시험 데이터를 사용하여 하이퍼 파라미터를 조정하면 하이퍼 파라미터 값이 시험 데이터에\
오버피팅된다.
-> 다른 데이터에는 적응하지 못하니 범용 성능이 떨어지게 된다.

하이퍼 파라미터를 조정할 때는 전용 확인 데이터가 필요하다.
하이퍼 파라미터 조정용 데이터를 일반적으로 검증 데이터validation data라고 한다.

*훈련 데이터는 매개변수(가중치와 편향)의 학습에 이용하고,\
검증 데이터는 하이퍼 파라미터의 성능을 평가한다.
시험 데이터는 범용 성능을 확인하기 위해 마지막에(이상적으로는 한 번만) 이용한다.

데이터셋에 따라서는 훈련 데이터, 검증 데이터, 시험 데이터를 미리 분리해둔 것도 있지만\
MNIST 데이터셋은 훈련 데이터와 시험 데이터로만 분리했다.
이런 경우(필요하면) 사용자가 직접 데이터를 분리해야 한다.
-> MNIST 데이터셋에서 검증 데이터를 얻는 방법은 훈련 데이터 중 20% 정도를 검증 데이터로\
먼저 분리한다.
'''
import numpy as np
from mnist import load_mnist

def shuffle_dataset(x, t):
    """데이터셋을 뒤섞는다.

    Parameters
    ----------
    x : 훈련 데이터
    t : 정답 레이블
    
    Returns
    -------
    x, t : 뒤섞은 훈련 데이터와 정답 레이블
    """
    permutation = np.random.permutation(x.shape[0])
    x = x[permutation,:] if x.ndim == 2 else x[permutation,:,:,:]
    t = t[permutation]

    return x, t

(x_train, t_train), (x_test, t_test)=load_mnist()

#훈련 데이트를 뒤섞는다.(shuffle_dataset)<= 데이터 셋 안의 데이터가 치우쳐 있을수도 있다.
x_train, t_train=shuffle_dataset(x_train, t_train)

validation_rate=0.20    #검증 확률=0.20(훈련 데이터 중 20% 정도를 검증 데이터로 분리한다.)
validation_num=int(x_train.shape[0]*validation_rate)

x_val=x_train[:validation_num]  #validation은 20%의 훈련 데이터
t_val=t_train[:validation_num]
x_train=x_train[validation_num:]    #훈련 데이터는 20%를 제외한 데이터
t_train=t_train[validation_num:]