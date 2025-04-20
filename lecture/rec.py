from functools import lru_cache

# n! = 1 * 2 * 3 * ... * n


def fact(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# n! = 1 * 2 * 3 * ... * (n-1) * n

# n! = (n-1)! * n

def fact_r(n: int) -> int:
    return n * fact_r(n - 1) if n > 1 else 1


# 1) recursive branch
# 2) terminal branch


if __name__ == "__main__":

    for i in range(1, 6):
        print(f"{i=} {fact(i)=}")
        print(f"{i=} {fact_r(i)=}")




# def x(i: int) -> float:



@lru_cache
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(1, 40):
    print(i, fib(i))




fib = make_fib()
print(fib()) # 1
print(fib()) # 1
print(fib()) # 2
print(fib()) # 3
print(fib()) # 5
