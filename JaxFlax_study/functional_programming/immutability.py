# 부수 효과는 없지만 불변성 또한 없는 함수

def create_counter():
    count = [0]
    
    def counter():
        count[0] += 1
        return count[0]
    
    return counter

counter = create_counter()
print(counter())    # 1
print(counter())    # 2
print(counter())    # 3
print(counter())    # 4
print(counter())    # 5