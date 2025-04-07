# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something befor func")
#         print(args)
#         print(kwargs)
#         result = func(*args, *kwargs)
#         print("Something after func")
#         return result
#     return wrapper


# 1) Декоратор для кэширования результатов выполнения функций. 
# 2) Класс от сани. 3)Замыкание реализующее последовательность Фибоначчи. 
# Чтобы каждый вызов функции выдавал следующее значение с первого по последний элемент. Код в скрине.
# 4) досматриваю саню. 5) если останется время то экзерцизм

def fib(n): # вычисление последовательности Фибоначчи
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# for i in range(1, 11):
    # print(f"Число {i}. Работа функции {fib(i)}")

# fib = make_fib() # 
# print(fib()) # 1
# print(fib()) # 1
# print(fib()) # 2
# print(fib()) # 3
# print(fib()) # 5



def cache_fib(func):
    result_cache = {} # пустой словарь для создания кеша
    def wrapper(*args):
        if args in result_cache: # если переданный аргумент есть в словаре
            return result_cache[args] # возвращаем значение из словаря по аргументу
        else:
            result = func(*args) # иначе выполняем функцию
            result_cache[args] = result # заносим результат работы функции в словарь аргумент=результат
        return result
    return wrapper


@cache_fib
def fib(n): # вычисление последовательности Фибоначчи
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

H = fib(9)
print(H)