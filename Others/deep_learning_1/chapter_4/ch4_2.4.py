#(배치용)교차 엔트로피 오차 구현하기
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset import load_mnist

(x_train, y_train), (x_test, y_test)=\
    load_mnist(normalize=True, one_hot_label=True)

train_size=x_train.shape[0]
batch_size=10
batch_mask=np.random.choice(train_size, batch_size)

x_batch=x_train[batch_mask]
y_batch=y_train[batch_mask]

def cross_entropy_error(y, t):
    if y.ndim==1:   #y가 1차원일 때(데이터 하나당 교차 엔트로피 오차를 구하는 경우)
        t=t.reshape(1, t.size)  #데이터 형상을 바꿔준다.
        y=y.reshape(1, y.size)

    batch_size=y.shape[0]   
    return -np.sum(t*np.log(y+1e-7))/batch_size 
    #배치의 크기(10)로 나눠 정규화, 이미지 1장당 평균 교차 엔트로피 오차를 계산

    #정답 레이블이 원-핫 인코딩이 아니라 '2'나 '7'처럼 숫자 레이블로 주어질 경우
    #return -np.sum(np.log(y[np.arange(batch_size),t]+1e-7))/batch_size
    '''
    원-핫 인코딩일 때 t가 0인 원소는 교차 엔트로피 오차도 0이므로, 그 계산은 무시해도 좋다.
    -> 정답에 해당하는 신경망의 출력만으로 교차 엔트로피 오차를 계산할 수 있다.

    원-핫 인코딩 시 t*np.log(y)였던 부분을 레이블 표현일 때는 np.log(y[np.arrange(batch_soze),t])로 구현
    -> np.arrange(batch_size)는 0부터 batch_size-1까지 넘파이 배열을 생성.

    t에는 레이블이 저장되어 있어 각 데이터의 정답 레이블에 해당하는 신경망의 출력을 추출한다.
    '''