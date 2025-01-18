#LSTM 클래스의 초기화
import numpy as np

def sigmoid(x):
    return 1/np.exp(-x)

class LSTM:
    def __init__(self, Wx, Wh, b):
        self.params=[Wx, Wh, b]
        self.grads=[np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.cache=None

    def forward(self, x, h_prev, c_prev):
        Wx, Wh, b=self.params
        N, H=h_prev.shape

        A=np.matmul(x, Wx)+np.matmul(h_prev, Wh)+b

        #slice
        f=A[:, :H]
        g=H[:, H:2*H]
        i=A[:, 2*H:3*H]
        o=A[:, 3*H:]

        f=sigmoid(f)
        g=np.tanh(g)
        i=sigmoid(i)
        o=sigmoid(o)

        c_next=f*c_prev+g*i
        h_next=o*np.tanh(c_next)

        self.cache=(x, h_prev, c_prev, i, f, g, o, c_next)
        return h_next, c_next

class TimeLSTM:
    def __init__(self, Wx, Wh, b, stateful=False):
        self.params=[Wx, Wh, b]
        self.grads=[np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.layers=None
        self.h, self.c=None, None
        self.dh=None
        self.stateful=stateful

    def forward(self, xs):
        Wx, Wh, b=self.params
        N,T,D=xs.shape
        H=Wh.shape[0]

        self.layers=[]
        hs=np.empty((N,T,H), dtype='f')

        if not self.stateful or self.h is None:
            self.h=np.zeros((N,H), dtype='f')
        if not self.stateful or self.c is None:
            self.c=np.zeros((N,H), dtype='f')
        
        for t in range(T):
            layer=LSTM(*self.params)
            self.h, self.c=layer.forward(xs[:, t, :], self.h, self.c)
            hs[:, t, :]=self.h

            self.layers.append(layer)
        return hs
    
    def backward(self, dhs):
        Wx, Wh, b=self.params
        N,T,H=dhs.shape
        D=Wx.shape[0]

        dxs=np.empty((N,T,D), dtype='f')
        dh, dc=0, 0

        grads=[0, 0, 0]
        for t in reversed(range(T)):
            layer=self.layers[t]
            dx, dh, dc=layer.backward(dhs[:, t, :]+dh, dc)
            dxs[:, t, :]=dx
            for i, grad in enumerate(layer.grads):
                grads[i]+=grad
            
            for i, grad in enumerate(grads):
                self.grads[i][...]=grad
                self.dh=dh
                return dxs
            
            def set_state(self, h, c=None):
                
                self.h, self.c=h, c
            
            def reset_state(self):
                self.h, self.c=None, None
