
def x(i: int) -> int:
    if i < 4:
        return 1
    return x(i - 1) + x(i - 3)



for i in range(1, 10):
    print(f"{i=} {x(i)=}")