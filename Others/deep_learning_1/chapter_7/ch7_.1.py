#전체 구조

'''
*합성곱 신경망convolutional neural network, CNN

이미지 인식 분야에서 딥러닝을 활용한 기법은 거의 CNN을 기초로 한다.
CNN도 지금까지 본 신경망과 같이 레고 블록처럼 계층을 조합하여 만들 수 있다.
다만, 합성곱 계층convolutional layer과 폴링 계층pooling layer이 새롭게 등장한다.

지금까지 본 신경망은 인접하는 계층의 모든 뉴런과 결합되어 있다-> 완전 연결fully-connected(전결합)
완전히 연결된 계층-> Affine 계층

완전연결 신경망은 Affine 계층 뒤에 활성화 함수를 갖는 ReLU 계층(혹은 sigmoid계층)이 이어진다.
Affine_ReLU 조합이 4개가 쌓였고, 마지막 Affie 계층에 이어 소프트맥스 계층에 최종 결과(확률)를 출력한다.

CNN에서는 새로운 '합성곱 계층Conv'과 '풀링 계층Pooling'이 추가된다.
CNN의 계층은 'Conv-ReLU-(Pooling)' 흐름으로 연결된다.
풀링 계층은 생략하기도 한다.
-> 지금까지의 Affine-ReLU' 연결이 'Conv-ReLU-(Pooling)'으로 바뀌었다.

출력에 가까운 층에서는 지금까지의 'Affine-ReLU' 구성을 사용할 수 있다.
마지막 출력 계층에서는 'Affine-Softmax' 조합을 그대로 사용한다.
'''
