#더 깊은 신경망으로

'''
신경망은 층이 깊을수록 여기에서 사용하는 합성곱 계층은 채널이 더 늘어난다.
또한 풀링 계층을 추가하여 중간 데이터의 공간 크기를 점차 줄여간다.
마지막 단의 완전연결 계층에서는 드롭아웃 계층을 사용한다.

가중치 초깃값으로 He 초깃값을 사용하고, 가중치 매개변수 갱신에는 Adam을 이용한다.

'''
#deep_convent_params.pkl 열기

import pickle 
import os 

model_path=input("Model Path = deep_convent_params")
with open(model_path, "rb") as model :
    load = pickle.load(model, encoding='utf-8')
    new_model_path = model_path.split('.pkl')[0] +'.txt'
    print("creating new file at : ", new_model_path)
    model_readable = open(new_model_path, 'rt')
    model_readable.write(load)
    print("writing model as readable : ", load)
model_readable.close()
model.close()