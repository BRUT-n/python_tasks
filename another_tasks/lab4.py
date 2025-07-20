# ДЗ
# 1) Декоратор для кэширования результатов выполнения функций. 
# 2) Класс от сани. 3)Замыкание реализующее последовательность Фибоначчи. 
# Чтобы каждый вызов функции выдавал следующее значение с первого по последний элемент. Код в скрине.
# 4) досматриваю саню. 5) если останется время то экзерцизм

# ==============
# ФУНЦКИЯ-ДЕКОРАТОР, ПРИМЕР НАПИСАНИЕ И ЕГО РАБОТА
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something befor func")
#         print(args)
#         print(kwargs)
#         result = func(*args, *kwargs)
#         print("Something after func")
#         return result
#     return wrapper
# ==============

# ===============
# # СТАНДАРТНАЯ ФУНКЦИЯ ДЛЯ ВЫЧИСЛЕНИЯ ФИБОНАЧЧИ
# def fib(n): # вычисление последовательности Фибоначчи
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# for i in range(1, 11):
#     print(f"Число {i}. Работа функции {fib(i)}")

# # fib = make_fib() # 
# print(fib()) # 1
# print(fib()) # 1
# print(fib()) # 2
# print(fib()) # 3
# print(fib()) # 5
# ==============

# ==============
# КУШИРУЮЩИЙ ДЕКОРАТОР
# def cache_fib(func):
#     result_cache = {} # пустой словарь для создания кеша
#     def wrapper(*args):
#         if args in result_cache: # если переданный аргумент есть в словаре
#             return result_cache[args] # возвращаем значение из словаря по аргументу
#         else:
#             result = func(*args) # иначе выполняем функцию
#             result_cache[args] = result # заносим результат работы функции в словарь аргумент=результат
#         return result
#     return wrapper
# ==============

# ==============
# ИСПОЛЬЗОВАНИЕ КЕШИРУЮЩЕГО ДЕКОРАТОРА
# @cache_fib
# def fib(n): # вычисление последовательности Фибоначчи
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(9))
# H = fib(9)
# print(H)
# ==============


# ==============
# ПРИМЕР ФУНКЦИИ-ЗАМЫКАНИЯ
# def outer(): # внешняя функция
#     count = 5 # локальная переменная для функции аутер (лексическое окружение)
#     def inner(): # внутренняя функция (локальная)
#         nonlocal count # объявление того что переменная не локальная и берется из лексического окружения
#         count += 1
#         return count # возврат нонлокал переменной после += 1
#     return inner # внешняя функция возвращает результат работы внутренней функции

# c = outer()
# print(c())
# print(c())
# print(c())
# ==============


# ==============
# ПОПЫТКИ НАПИСАТЬ ЗАМЫКАНИЕ ДЛЯ РЕКУРСИВНОЙ ФУНКЦИИ
# def param_outer():
#     n = 9
#     def fib(n):
#         nonlocal n
#         if n <= 2:
#             return 1
#         return fib(n-1) + fib(n-2) с рекурсией
#     return fib

# def param_outer():
#     n = 9
#     def fib(n):
#         nonlocal n
#         if n <= 2:
#             return 1
#         return fib(n-1) + fib(n-2) написать без рекурсии
#     return fib

# def fib_counter(): # определение функции замыкания
#     count_value = 0 # переменная счетчика значений от выполнения функции
#     def fib(n): # сама функция
#         nonlocal count_value
#         count_value = (n - 1) + (n - 2)
#         return count_value
#     return fib
# ==============

# def fibonacci_not_rec(number):
#     if number <= 2:
#         return 1
#     else:
#         i = 0
#         first_num = 0
#         second_num = 1
#         while i != number - 1:
#              sum_num = first_num + second_num
#              first_num = second_num
#              second_num = sum_num
#              i += 1
#         return sum_num

def fibonacci_not_rec(number):
    if number == 0:
        return 0
    first = 0
    second = 1
    sum = 1
    for i in range(1, number):
        sum = first + second
        first = second
        second = sum
    return sum

for g in range(11):
    print(g, fibonacci_not_rec(g))

# print(fibonacci_not_rec(1))

# def closure(): # функция-замыкание
#     def fibonacci_not_rec(number): # вложенная в замыкание функция для Фибоначчи
#         if number <= 2: # если требуется вывести первое или второе число - это 1
#             sum_num = 1
#             return sum_num
#         else:
#             i = 0 # счетчик итераций для расчета чисел по порядку
#             first_num = 0 # первое число 0 по списку чисел
#             second_num = 1 # второе число 1 по списку чисел
#             while i != number - 1: # пока количество итераций не равно номеру числа по порядку
#                 sum_num = first_num + second_num # вычисляется сумма чисел первого и второго
#                 first_num = second_num # обновляем первое число сделав его вторым
#                 second_num = sum_num # второе число делаем вычисленным числом (по определению Фибоначчи)
#                 i += 1 # увеличиваем счетчик инераций
#             return sum_num # возвращаем полученный результат после цикла
#     return fibonacci_not_rec # возвращаем внутреннюю функцию для работы самого замыкания


def closure(): # функция-замыкание
    def fibonacci_not_rec(number):
        if number == 0:
            return 0
        first = 0
        second = 1
        sum = 1
        for i in range(1, number):
            sum = first + second
            first = second
            second = sum
        return sum
    return fibonacci_not_rec # возвращаем внутреннюю функцию для работы самого замыкания



c1 = closure() # замыкание для дальнейшего использования
c2 = closure() # независимые замыкания с тем же поведением
c3 = closure() # независимые замыкания с тем же поведением
print(c1(8)) # Вызов внутреннюю функции с аргументом
print(c2(5))
print(c3(5))