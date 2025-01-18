#단순한 계층 구현하기(곱셈 계층)
'''
모든 계층은 forward()와 backward()라는 공통의 메서드(인터페이스)를 갖도록 구현한다.
forward()-> 순전파, backward()-> 역전파
'''
class MultiLayer:
    def __init__(self):
        self.x=None #인스턴스 변수 x,y를 초기화-> 순전파 시의 입력 값을 유지하기 위해 사용함.
        self.y=None
    
    def forward(self, x, y):    #x와 y를 인수로 받고 두 값을 곱해 반환.
        self.x=None
        self.y=None
        out=x*y
        return out
    
    def backward(self, dout):   #상류에서 넘어온 미분(dout)에 순전파의 값을 '서로 바꿔' 곱한 후 하류로 흘림.
        dx=dout*self.y  
        dy=dout*self.x
        return dx, dy

#순전파(forward)
apple, apple_num, tax=100, 2, 1.1

mul_apple_layer=MultiLayer()
mul_tax_layer=MultiLayer()

apple_price=mul_apple_layer.forward(apple, apple_num)
price=mul_tax_layer.forward(apple_price, tax)

print(price)
#220.00000000000003


#역전파(backward)
dprice=1
dapple_price, dtax=mul_tax_layer.backward(dprice)
dapple, dapple_num=mul_apple_layer.backward(dapple_price)

print(dapple, dapple_num, dtax) #2.2 110 200
'''
역전파의 호출 순서는 순전파 때와는 반대.
역전파가 받는 인수는 '순전파의 출력에 대한 미분'임에 주의하자.

mul_apple_layer라는 곱셈 계층은 순전파 때는 apple_price를 출력하지만,\
역전파 떄는 apple_price의 미분 값인 dapple_price를 인수로 받는다.
'''


#덧셈 계층
class AddLayer:
    def __init__(self): #덧셈 계층에서는 초기화가 필요 없다.
        pass
    
    def forward(self, x, y):    #두 인수 x,y를 더해서 반환한다. 
        out=x*y
        return out
    
    def backward(self, dout):   #상류에서 내려온 미분(dout)을 그대로 하류로 보낸다.
        dx=dout*1
        dy=dout*1
        return dx, dy

apple=100
apple_num=2
orange=150
orange_num=3
tax=1.1

#계층들
mul_apple_layer=MultiLayer()
mul_orange_layer=MultiLayer()
add_apple_orange_layer=AddLayer()
mul_tax_layer=MultiLayer()

#순전파(forward)
apple_price=mul_apple_layer.forward(apple, apple_num)   #(1)
orange_price=mul_orange_layer.forward(orange, orange_num)   #(2)
all_price=add_apple_orange_layer.forward(apple_price, orange_price) #(3)
price=mul_tax_layer.forward(all_price, tax) #(4)

#역전파(backward)
dprice=1
dall_price=mul_tax_layer.backward(dprice)   #(4)
dapple_price, dorange_price=add_apple_orange_layer.backward(dall_price)  #(3)
dorange, dorange_num=mul_orange_layer.backward(dorange_price)   #(2)
dapple, dapple_num=mul_apple_layer.backward(apple_price)    #(1)

print(price)
print(dapple_num, dapple, dorange, dorange_num, dtax)   #110 2.2 3.3 165 650