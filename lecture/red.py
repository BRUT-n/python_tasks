from functools import reduce
from typing import Callable, Iterable, Any


def add(a, b):
    return a + b



lst = [1, 2, 3, 4, 5]
initial = 0

print(
    reduce(add, lst)
)




def my_reduce(func: Callable, iterable: Iterable, initial: Any) -> Any:
    result = initial
    for i in iterable:
        result = func(result, i)
    return result

print(
    my_reduce(add, lst, initial=0)
)


