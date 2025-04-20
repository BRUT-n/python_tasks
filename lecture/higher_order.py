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

