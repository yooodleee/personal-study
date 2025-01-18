#다층 퍼셉트론이 충돌한다면-> XOR 게이트 구현하기
def XOR(x1, x2):
    s1=NAND(x1, x2)
    s2=OR(x1, x2)
    y=AND(s1, s2)   #XOR=(NAND+OR)+AND
    return y

XOR(0, 0)   #0
XOR(1, 0)   #1
XOR(0, 1)   #1
XOR(1, 1)   #0