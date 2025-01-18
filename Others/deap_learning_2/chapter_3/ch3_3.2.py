#원핫 표현으로 변환
import sys
sys.path.append('..')
from util import preprocess, create_contexts_target, convert_one_hot

text='You say goodbye and I say hello.'
corpus, id_to_word, word_to_id=preprocess(text)#전처리(단어 ID 목록, 딕셔너리)

context, target=create_contexts_target(corpus, window_size=1)#문맥과 타깃 생성(단어 ID 목록, 윈도우 크기)

vocab_size=len(word_to_id)#어휘 수<-word_to_id 딕셔너리만큼
target=convert_one_hot(target, vocab_size)#원핫 표현으로 변환(타깃, 어휘 수)
contexts=convert_one_hot(context, vocab_size)#문맥(문맥, 어휘 수)