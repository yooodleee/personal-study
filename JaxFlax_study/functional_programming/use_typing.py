# typing.Any()를 활용한 예시

from typing import Any, Callable, Tuple
from flax import linen as nn
import jax.numpy as jnp


ModuleDef = Any

class ResNetBlock(nn.Module):
    """잔차 블록 선언"""
    filters: int
    conv: ModuleDef
    norm: ModuleDef
    act: Callable
    strides: Tuple[int, int] = (1, 1)