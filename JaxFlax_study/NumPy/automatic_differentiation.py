import jax
from IPython.display import display

def f(x):
    return x ** 2

df = jax.grad(f)

display(df(3.0))