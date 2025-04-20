from typing import Any, Callable, Literal
from time import perf_counter
from functools import wraps


def run_n_times(n: int) -> Callable:
    def deco(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> list[Any]:
            return [func(*args, **kwargs) for i in range(n)]
        return wrapper
    return deco





@run_n_times(3)
def hello():
    print("Hello")

# hello = run_n_times(3)(hello)


r = hello()
print(r)




# def make_calc(op: Literal["+", "*"], initial: int) -> Callable:
#     result = initial
#     def calc(value: int) -> int:
#         nonlocal result
#         if op == "+":
#             result += value
#         if op == "*":
#             result *= value
#         return result

#     return calc





# calc = make_calc("+", initial=0)
# calc2 = make_calc("*", initial=1)
# print(calc(2)) # 2 
# print(calc2(2)) # 2 
# print(calc(5)) # 7 
# print(calc2(5)) # 10



