#신경망으로 문제를 풀다.

#스파이럴 데이터셋
import sys
sys.path.append('..')   #부모 디렉터리를 임포트의 검색 경로에 추가
from dataset import spiral
import matplotlib.pyplot as plt

x, t=spiral.load_data() #데이터를 읽어 온다.(x는 입력 데이터, t는 정답 테이블)
print(x, x.shape)   #(300,2), 300개의 샘ㅍㄹ 데이터를 담으며, 2차원 데이터
print(t, t.shape)   #(300,3), 3차원 데이터, 원핫 벡터(정답에 해당하는 클래스만 1)

N = 100
CLS_NUM = 3
markers = ['o', 'x', '^']
for i in range(CLS_NUM):
    plt.scatter(x[i*N:(i+1)*N, 0], x[i*N:(i+1)*N, 1], s=40, marker=markers[i])
plt.show()
'''
직선만으로는 클래스들을 분리할 수 없다.
-> 비선형 분리를 학습해야 한다.
-> 비선형인 시그모이드 함수를 활성화 함수로 사용하는 은닉층이 있는
'''