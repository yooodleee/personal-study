import jax
import jax.numpy as jnp
from IPython.display import display


def mse_loss(y_true, y_pred):
    return jnp.mean((y_true - y_pred) ** 2)

# 임의의 예측값과 실젯값
y_true = jnp.array([1.0, 2.0, 3.0])
y_pred = jnp.array([1.5, 1.5, 1.5])

# 손실 함수와 그레이디언트를 동시에 계산하기 위한 함수 정의
value_and_grad_mse_loss = jax.value_and_grad(mse_loss, argnums=1)

# 손실값과 그레이디언트 동시에 계산
loss_value, gradient = value_and_grad_mse_loss(y_true, y_pred)

display('Loss Value: ', loss_value)
display('Gradient: ', gradient)