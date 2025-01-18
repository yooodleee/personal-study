#이미지 표시하기
import matplotlib.pyplot as plt
from matplotlib.image import imread

img=imread('cactus.png')
plt.imshow(img) #이미지를 표시해주는 메서드-> imread()
plt.show()