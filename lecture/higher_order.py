# def sqr(x):
#     return x * x


# def plus_2(x):
#     return x + 2


# def compose(f, g):
#     def composition(x):
#         return f(g(x))
#     return composition


# c = compose(plus_2, sqr)



# res = c(3)
# print(res)



from random import choice


def make_greeter(name = "stranger"):
    def greet():
        greetings = [
            "Hi, ",
            "Hello, ",
            "Nice to meet you, "
        ]
        return choice(greetings) + name
    return greet


vasya = make_greeter("Vasya")
anon = make_greeter()


def make_counter():
    start = 0
    def f():
        nonlocal start
        start += 1
        return start
    return f



counter = make_counter()

print(counter()) # 1
print(counter()) # 2
print(counter()) # 3
print(counter()) # 4