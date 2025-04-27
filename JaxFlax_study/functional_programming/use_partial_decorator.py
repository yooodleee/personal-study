# JAX에서 partial() 데커레이터를 활용하는 예시

import jax
import jax.numpy as jnp
from functools import partial


@partial(jax.jit, static_argnames=['n'])
def g(x, n):
    for i in range(n):
        x = x ** 2
    return x

g(jnp.arange(4), 3)