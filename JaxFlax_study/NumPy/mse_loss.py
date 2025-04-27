import numpy as np
import jax
import jax.numpy as jnp
from IPython.display import display


def mse_with_aux(pred, target):
    error = pred - target
    mse = np.mean(error ** 2)
    return mse, error   # MSE 결과와 보조 결과인 에러를 반환

# 가정된 예측값과 타깃값
pred = np.array([1.0, 2.0, 3.0])
target = np.array([1.5, 2.5, 3.5])

grad_fun, aux = jax.grad(mse_with_aux)(pred, target)    # TypeError 발생 
