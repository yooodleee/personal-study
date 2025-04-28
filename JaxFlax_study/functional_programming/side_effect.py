# 부수 효과가 적용된 파이썬 함수

counter = 0

def increment_counter(x):
    global counter
    counter += x
    return counter

print(increment_counter(1))
print(increment_counter(2))
print(increment_counter(3))
print('after_counter: ', counter)