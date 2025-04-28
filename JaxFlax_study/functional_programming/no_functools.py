# functools.partial을 사용하지 않은 함수

def add_mul(x, y, z):
    return x + y * z

print('not_using_partial: ', add_mul(2, 3, 1))
print('not_using_partial: ', add_mul(3, 4, 1))
print('not_using_partial: ', add_mul(6, 8, 1))


# partial을 사용한 함수
from functools import partial


add_2 = partial(add_mul, z = 1)

print('using_partial: ', add_2(2, 3))
print('using_partial: ', add_2(3, 4))
print('using_partial: ', add_2(6, 8))