from math import log10, ceil

def is_armstrong_number(number): # решение без конвертации в строки
    if number == 0: # для исключения нуля в логорифме
       return True 
    number_for_calculation = number
    result_of_iteration = 0
    digit_count = ceil(log10(number)) #имбовая математика - ceil округление в большую сторону, floor - в нижнюю
    while number_for_calculation:
        result_of_iteration += (number_for_calculation % 10) ** digit_count
        number_for_calculation = number_for_calculation // 10
    return result_of_iteration == number

# def is_armstrong_number(number): # первое решение
#     string_number = str(number)
#     count = 0
#     for num in string_number:
#         num = int(num)
#         f = num ** len(string_number)
#         count += f
#     return count == number
