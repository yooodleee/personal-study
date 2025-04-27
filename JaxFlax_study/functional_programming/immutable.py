# 부수 효과도 없으며 불변성을 유지하는 함수

counter = 0
def immutable_example(state, x):
    counter = state
    return counter + x


for a in range(3):
    print(immutable_example(0, a + 1))
    print('counter: ', counter)