# 순수 효과 파이썬 함수

def not_side_effect_example(counter, x):
    return counter + x

counter = 0

for a in range(3):
    print(not_side_effect_example(counter, a+1))

print('after_counter: ', counter)