#분포 모델과 샘플 모델
import numpy as np

def sample(dices=2):
    x=0
    for _ in range(dices):
        x+=np.random.choice([1, 2, 3, 4, 5, 6])
    return x

print(sample())
#5
print(sample())
#5
print(sample())
#8


#몬테카를로법 구현
trial=1000 #샘플링 횟수

samples=[]
for _ in range(trial): #샘플링
    s=sample()
    samples.append(s)

V=sum(samples)/len(samples) #평균 계산
print(V)#6.914


#매번 평균 계산
trial=1000

samples=[]
for _ in range(trial):
    s=sample()
    samples.append(s)
    V=sum(samples)/len(samples) #매번 평균 계산
    print(V)


#증분 구현
trial=1000
V,n=0, 0

for _ in range(trial):
    s=sample()
    n+=1
    V+=(s-V)/n #또는 V=V+(s-V)/n
    print(V)