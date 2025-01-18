#RNNLM의 학습 코드
import sys
sys.path.append('..')
import matplotlib.pyplot as plt
import numpy as np
from optimizer import SGD
from ptb import load_data
from simple_rnnlm import SimpleRnnlm

#하이퍼 파라미터 설정
batch_size=10
wordvec_size=100
hidden_size=100
#RNN의 은닉 상태 벡터의 원소 수
time_size=5
#Truncated BPTT가 한 번에 펼치는 시간 크기
lr=0.1
max_epoch=100

#학습 데이터 읽기(전체 중 1000개만)
corpus, word_to_id, id_to_word=load_data('train')
corpus_size=100
corpus=corpus[:corpus_size]
vocab_size=int(max(corpus)+1)

xs=corpus[:-1]#입력
ts=corpus[1:]#출력(정답 레이블)
data_size=len(xs)
print('말뭉치 크기: %d, 어휘 수: %d' %(corpus_size, vocab_size))

#학습 시 사용하는 변수
max_iters=data_size//(batch_size*time_size)
time_idx=0
total_loss=0
loss_count=0
ppl_list=[]

#모델 생성
model=SimpleRnnlm(vocab_size, wordvec_size, hidden_size)
optimizer=SGD(lr)

#각 미니배치에서 샘플을 읽기 시작 위치를 계산
jump=(corpus_size-1)//batch_size
offsets=[i*jump for i in range(batch_size)]

for epoch in range(max_epoch):
    for iter in range(max_iters):

        #미니배치 획득
        batch_x=np.empty((batch_size, time_size), dtype='i')
        batch_t=np.empty((batch_size, time_size), dtype='i')
        for t in range(time_size):
            for i, offset in enumerate(offsets):
                batch_x[i, t]=xs[(offset+time_idx)%data_size]
                batch_t[i, t]=ts[(offset+time_idx)%data_size]
            time_idx+=1
        
        #기울기를 구하여 매개변수 갱신
        loss=model.forward(batch_x, batch_t)
        model.backward()
        optimizer.update(model.params, model.grads)
        total_loss+=loss
        loss_count+=1
    
    #에폭마다 퍼플렉서티 평가
    ppl=np.exp(total_loss/loss_count)
    print('| 에폭 %d | 퍼플렉서티 %.2f' %(epoch+1, ppl))
    ppl_list.append(float(ppl))
    total_loss, loss_count=0,0

# 퍼플렉서티 변화 그래프 그리기
plt.plot(np.arange(len(ppl_list)), ppl_list, label='Perplexity')
plt.xlabel('Epochs')
plt.ylabel('Perplexity')
plt.title('Perplexity over Epochs')
plt.legend()
plt.grid(True)
plt.show()
    
from trainer import RnnlmTrainer

...
model=SimpleRnnlm(vocab_size, wordvec_size, hidden_size)
optimizer=SGD()
trainer=RnnlmTrainer(model, optimizer)

trainer.fit(xs, ts, max_epoch, time_size)