def f(a, b, c):
    print(a, b, c)


f(1, 2, 3)


f(b=2, c=3, a=1)



def f(a, b, c=3):
    print(a, b, c)


f(1, 2, 4)



def f(*args):
    print(args)


f(1, 2, 3, 4, 5, 6)



def f(**kwargs):
    print(kwargs)


f(a=1, b=2, c=3, d=4)



def f(a, *args, d=4, **kwargs):
    print(a, d, args, kwargs)

f(1, b=2, c=3)


def f(*, a, b, c):
    print(a, b, c)

f(a=1, b=2, c=3)




def f(a, /, b, *, c):
    print(a, b, c)

f(1, 2, c=3)