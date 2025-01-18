#matpolib
import numpy as np
import matplotlib.pyplot as plt

#data
x=np.arange(0, 6, 0.1)  #0~6까지 0.1의 간격으로 생성
y=np.sin(x)

#그래프 그리기
plt.plot(x,y)
plt.show()