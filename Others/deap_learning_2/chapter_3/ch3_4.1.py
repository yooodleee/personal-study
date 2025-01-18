#학습 코드 구현
import sys
sys.path.append('..')
from trainer import Trainer
from simple_cbow import SimpleCBOW
from optimizer import Adam
from util import preprocess, create_contexts_target, convert_one_hot

window_size=1
hidden_size=5
batch_size=3
max_epoch=1000

text='You say goodbye and I say hello.'
corpus, id_to_word, word_to_id=preprocess(text)

vocab_size=len(word_to_id)
contexts, target=create_contexts_target(corpus, window_size)
target=convert_one_hot(target, vocab_size)
contests=convert_one_hot(contexts, vocab_size)

model=SimpleCBOW(vocab_size, hidden_size)
optimizer=Adam()
trainer=Trainer(model, optimizer)

trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()

word_vecs=model.word_vecs
for word_id, word in id_to_word.items():
    print(word, word_vecs[word_id])

