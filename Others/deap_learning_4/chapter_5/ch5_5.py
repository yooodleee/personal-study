#몬테카를로법을 이용해 기댓값 E_π[x] 구하기
import numpy as np

x=np.array([1,2,3]) #확률 번수
pi=np.array([0.1, 0.1, 0.8]) #확률 분포

#기댓값의 참값 계산
e=np.sum(x*pi)
print('참값(E_pi[x]): ', e)

#몬테카를로법으로 계산
n=100 #샘플 개수
samples=[]
for _ in range(n):
    s=np.random.choice(x, p=pi) #pi를 이용한 샘플링
    samples.append(s)
    mean=np.mean(samples) #샘플들의 평균
    var=np.var(samples) #샘플들의 분산
    print('몬테카를로법:{:.2f}'.format(mean, var))


#중요도 샘플링을 이용하여 기댓값 계산
b=np.array([1/3, 1/3, 1/3]) #확률 분포
n=100 #샘플 개수
samples=[]

for _ in range(n):
    idx=np.arange(len(b)) #b의 인덱스([0, 1, 2])
    i=np.random.choice(idx, p=b) #b를 사용하여 샘플링
    s=x[i]
    rho=pi[i]/b[i] #가중치
    samples.append(rho*s) #샘플 데이터에 가중치를 곱해 저장

mean=np.mean(samples)
var=np.var(samples)
print('중요도 샘플링: {:.2f} (분산: {:.2f})'.format(mean, var))
#중요도 샘플링: 2.96 (분산: 10.58)


#두 확률 분포(b와 π)를 가깝게 만든다.
b=np.array([0.2, 0.2, 0.6]) #확률 분포 변경(앞에서는 [1/3, 1/3, 1/3])
n=100
samples=[]

for _ in range(n):
    idx=np.arange(len(b)) #[0, 1, 2]
    i=np.random.choice(idx, p=b)
    s=x[i]
    rho=pi[i]/b[i]
    samples.append(rho*s)

mean=np.mean(samples)
var=np.var(samples)
print('중요도 샘플링: {:.2f} (분산: {:.2f})'.format(mean, var))
#중요도 샘플링: 2.73 (분산: 2.53)