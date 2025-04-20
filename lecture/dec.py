from time import perf_counter
from functools import wraps



def my_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} took {perf_counter() - start} s.")
        return result
    return wrapper




@my_deco # hello = my_deco(hello)
def hello():
    print("Hello")


# @my_deco
# def sqr(x):
#     """calculates ..."""
#     return 12345 ** 1233454


hello()
# r = sqr(2)
# print()


from typing import Callable, Literal


def make_calc(op: Literal["+", "*"], initial: int) -> Callable:
    result = initial
    def calc(value: int) -> int:
        nonlocal result
        if op == "+":
            result += value
        if op == "*":
            result *= value
        return result

    return calc





calc = make_calc("+", initial=0)
calc2 = make_calc("*", initial=1)
print(calc(2)) # 2 
print(calc2(2)) # 2 
print(calc(5)) # 7 
print(calc2(5)) # 10



