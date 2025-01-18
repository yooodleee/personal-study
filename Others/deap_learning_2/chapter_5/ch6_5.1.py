import sys
sys.path.append('..')
from optimizer import SGD
from trainer import RnnlmTrainer
from util import eval_perplexity
from ptb import load_data
from better_rnnlm import BetterRnnlm

#하이퍼파라미터 설정
batch_size=20
wordvec_size=650
hidden_size=650
time_size=35
lr=20.0
max_epoch=40
max_grad=0.25
dropout=0.5

#학습 데이터 읽기
corpus, word_to_id, id_to_word=load_data('train')
corpus_val,_,_=load_data('val')
corpus_test,_,_=load_data('test')

vocab_size=len(word_to_id)
xs=corpus[:-1]
ts=corpus[1:]

model=BetterRnnlm(vocab_size, wordvec_size, hidden_size, dropout)
optimizer=SGD()
trainer=RnnlmTrainer(model, optimizer)

best_ppl=float('inf')
for epoch in range(max_epoch):
    trainer.fit(xs, ts, max_epoch=1, batch_size=batch_size, time_size=time_size, max_grad=max_grad)
    model.reset_state()
    ppl=eval_perplexity(model, corpus_val)
    print('검증 퍼플렉서티: ', ppl)

    if best_ppl>ppl:
        best_ppl=ppl
        model.save_params()
    else:
        lr/=4.0
        optimizer.lr=lr
        
        model.reset_state()
        print('-'*50)