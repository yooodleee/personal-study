import numpy as np
import matplotlib.pyplot as plt

N, H, T=2, 3, 20
#미니배치의 크기, 은닉 상태 벡터의 차원 수, 시계열 데이터의 길이

dh=np.ones((N,H))
np.random.seed(3)
#재현할 수 있도록 난수의 시드 고정
Wh=np.random.randn(H,H)*0.5

norm_list=[]
for t in range(T):
    dh=np.matmul(dh, Wh.T)
    norm=np.sqrt(np.sum(dh**2))/N
    norm_list.append(norm)

plt.plot(np.arange(len(norm_list)), norm_list)
plt.xticks([0,4,9,14,19],[1,5,10,15,20])
plt.rc('font', family='Malgun Gothic')
plt.xlabel('time step')
plt.ylabel('norm')
plt.show()

# Wh=np.random.randn(H,H)
# Wh=np.random.randn(H,H)*0.5