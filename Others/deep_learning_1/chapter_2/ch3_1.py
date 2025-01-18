#AND 게이트 퍼셉트론 구현
def AND(x1, x2):    #x1, x2 인수
    w1, w2, theta=0.5, 0.5, 0.7 #w1, w2 가중치, theta:임계값
    tmp=x1*w1+x2*w2

    if tmp<=theta:  #입력값*가중치의 총합<=임계값
        return 0
    elif tmp>theta: #입력값*가중치의 총합>임계값
        return 1
    
AND(0,0)    #0
AND(1,0)    #0
AND(0,1)    #0
AND(1,1)    #1