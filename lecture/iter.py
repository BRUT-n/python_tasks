from typing import Iterable, Callable

# obj = [1, 2, 3]

# for c in obj:
#     print(c)


# def my_for(obj: Iterable, iteration_logic: Callable) -> None:
#     if not isinstance(obj, Iterable):
#         raise ValueError(f"'{obj.__class__.__name__}' object is not iterable")
#     iterator = iter(obj)
#     while True:
#         try:
#             item = next(iterator)
#         except StopIteration:
#             break
#         iteration_logic(item)

# my_for(obj, lambda item: print(item))



class MyIterable:
    def __init__(self, n: int):
        self.cur_idx = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        i = self.cur_idx
        self.cur_idx += 1
        if self.cur_idx > self.n:
            raise StopIteration
        return i



for i in MyIterable(5):
    print(i)


