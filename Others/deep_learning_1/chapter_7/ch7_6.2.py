#층의 깊이에 따른 추출 정보 변화

'''
1번째 층의 합성곱 계층에서는 에지나 블롭 등의 저수준 정보가 추출되지만,
겹겹이 쌓인 CNN의 각 계층에서는 어떤 정보가 추출되는가?

딥러닝 시각화에 관한 연구에 따르면 계층이 깊어질수록 추출되는 정보(강하게 반응하는 뉴런)는\
더 추상화된다는 것을 알 수 있다.

합성곱 계층을 여러 겹 쌓으면, 층이 깊어지면서 더 복잡하고 추상화된 정보가 추출된다.
처음 층은 단순한 에지에 반응하고, 이어서 텍스처에 반응하고, 더 복잡한 사물의 일부에 반응하도록 변화한다.
-> 층이 깊어지면서 뉴런이 반응하는 대상이 단순한 모양에서 '고급' 정보로 변화해간다.
-> 사물의 '의미'를 이해하도록 변화한다.
'''
#대표적인 CNN

'''
1) LeNet

손글씨 숫자를 인식하는 네트워크.
합성곱 계층과 풀링 계층(단순히 '원소를 줄이기'만 하는 서브 샘플링 계층)을 반복하고,\
마지막으로 완전연결 계층을 거치면서 결과를 출력한다.

LeNet은 시그모이드 함수를 사용하지만, CNN은 ReLU를 사용한다.
LeNet은 서브샘플링하여 중간 데이터의 크기를 줄이지만 현재는 최대 풀링이 주류이다.

2) AlexNet

합성곱 계층과 풀링 계층을 거듭하며 마지막으로 완전연결 계층을 거쳐 결과를 출력한다.
LeNet에서 큰 구조는 바뀌지 않았지만, 활성화 함수로 ReLU를 사용하고,\
LRN(Local Response Normalization)이라는 국소적 정규화를 실시하는 계층을 이용하며\
드롭아웃을 사용한다.

대량의 데이터를 누구나 얻을 수 있게 되었고, 병렬 계산에 특화된 GPU가 보급되면서 대량의 연산을\
고속으로 수행할 수 있게 되었다.
'''