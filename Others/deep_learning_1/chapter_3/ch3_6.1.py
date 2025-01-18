#MNIST 이미지를 화면으로 불러오기(PIL 모듈)
import sys, os
sys.path.append(os.pardir)
import numpy as np
from mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img=Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test)=\
    load_mnist(flatten=True, normalize=False)   
#flatten=True-> 읽어들인 이미지는 1차원 넘파이 배열로 저장됨
#이미지를 표시할 때는 원래 형상인 28x28 크기로 다시 변형해야 한다.

img=x_train[0]
label=t_train[0]
print(label)

print(img.shape)    #(784,)
img=img.reshape(28,28)    #원래 이미지의 모양으로 변형 
#reshape()-> 원하는 형상을 인수로 지정하면 넘파이 배열의 형상을 바꿀 수 있음.
print(img.shape)    #(28,28)

img_show(img)
'''
넘파이로 저장된 이미지 데이터를 PIL 용 데이터 객체로 변환해야 하며, 이 변환은\
Image.fromarray()가 수행함.
'''