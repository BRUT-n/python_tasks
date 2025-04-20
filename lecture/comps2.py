def sqr(x):
    return x * x


def f(x):
    return x ** 4 + x / 3.14

lst = [sqr(i) for i in range(1, 10) if i % 2]
print(lst)



if (x := f(4)) > 100:
    x -= 1

print(x)



lst = [s for i in range(1, 10) if (s := sqr(i)) % 2]
print(lst)





print(
    list(
        filter(lambda x: x % 2, range(1, 10))
    )
)