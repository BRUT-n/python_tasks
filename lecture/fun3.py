# LEGB - Local, Enclosing, Global, Built-in


x = 1

def f1():
    x = 2
    print(x)

    def f2():
        nonlocal x
        x += 1
        print(x)

    f2()
f1()
print(x)
