#손글씨 숫자 인식
'''
이미 학습된 매개변수를 사용하여 학습 과정은 생략하고, 추론 과정만 구현한다.
-> 신경망의 순전파forward propagation

훈련 데이터(학습 데이터)를 사용해 가중치 매개변수를 학습하고,\
추론 단계에서는 앞서 학습한 매개변수를 사용해 입력 데이터를 분류한다.
'''

#MNIST 데이터셋
'''
MNIST의 이미지 데이터는 28x28x 크기의 회색조 이미지(1채널)이며,\
각 픽셀은 0~255까지의 값을 취한다.
각 이미지에는 또한 '7','2','1'과 같이 그 이미지가 실제 의미하는 숫자가 레이블로 붙어 있다.
'''
import sys, os
sys.path.append(os.pardir)  #부모 디렉터리의 파일을 가져올 수 있도록 설정
from  mnist import load_mnist

(x_train, t_train), (x_test, t_test)=\
    load_mnist(flatten=True, normalize=False)   #load_mnist-> MNIST 데이터셋을 읽음
#최초 연결 시에는 인터넷에 연결된 상태여야 함.
#2 번째부터는 로컬에 저장된 파일(pickle 파일)을 읽기 때문에 순식간에 끝난다.

print(x_train.shape)    #(60000, 784)
print(t_train.shape)    #(60000,)
print(x_test.shape)     #(10000, 784)
print(t_test.shape)     #(10000,)

'''
load_mnist 함수는 읽은 MNIST 데이터를 "(훈련 이미지, 훈련 테이블), (시험 이미지, 시험 레이블)"\
형식으로 변환한다.
인수로는 normalize, flatten, one_hot_label 3가지를 설정할 수 있다.
-> 세 인수 모두 bool 값이다.

*normalize-> 입력 이미지의 픽셀 값을 0.0~1.0 사이의 값으로 정규화할지 정한다.
False로 설정하면 입력 이미지를 원래 값 그대로 0~255 사이의 값을 유지한다.

*flatten-> 입력 이미지를 평탄하게, 1차원 배열로 만들지를 정한다.
False(입력 이미지를 1x28x28의 3차원 배열), True(784개의 원소로 이뤄진 1차원 1배열)

*one_hot_label-> 레이블을 원-핫 인코딩 형태로 저장할지를 정한다.
정답을 뜻하는 원소만 1이고(hot) 나머지는 모두 0인 배열이다.
False이면 '7'이나 '2'와 같이 숫자 형태의 레이블을 저장하고, True일 떄는 레이블을 원-핫 인코딩하여 저장한다.

*pickle
-> 프로그램 실행 중에 특정 객체를 파일로 저장하는 기능.
저장해둔 pickle 파일을 로드하면 실행 당시의 객체를 즉시 복원할 수 있다.
MNIST 데이터셋을 읽는 load_mmist() 함수에서도 pickle을 이용한다.
pickle 덕분에 MNIST 데이터를 순식간에 준비할 수 있다.
'''