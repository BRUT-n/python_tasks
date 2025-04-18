def squares_generator(list_of_numbers):
    for number in list_of_numbers:
        yield number ** 2 # похож на ретерн обычной функции, то имеет конец исполнения с ошибкой StopIteration

a = squares_generator([3, 4])
# print(next(a)) #9
# print(next(a)) #16
# print(next(a)) #StopIteration

# for result in a:
#     print(result)

def infinite_sequence(): # бесконечный генератор
    current_number = 0
    while True:
        yield current_number # возврат значения генератора
        current_number += 1

lets_try = infinite_sequence()
# print(next(lets_try))
# print(next(lets_try))
