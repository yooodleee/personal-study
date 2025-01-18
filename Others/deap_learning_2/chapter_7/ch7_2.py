import sys
sys.path.append('..')
from sequence import load_data, get_vocab

(x_train, t_train), (x_test, t_test)=load_data('addition.txt', seed=1984)
char_to_id, id_to_char=get_vocab()

print(x_train.shape, t_train.shape)
#(45000, 7) (45000, 5)
print(x_test.shape, t_test.shape)
#(5000, 7) (5000, 5)

print(x_train[0])
#[ 3  0  2  0  0 11  5]
print(t_train[0])
#[ 6  0 11  7  5]

print(' '.join([id_to_char[c] for c in x_train[0]]))
#7 1 + 1 1 8
print(' '.join([id_to_char[c] for c in t_train[0]]))
#_ 1 8 9