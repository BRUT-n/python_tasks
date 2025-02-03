import random
from random import randint # импорт нужной функции из модуля

def choice_from_range(string, index_begin, index_end):
    rand_index = randint(index_begin, index_end) # рандомный индекс через функцию рандинт(введенные идексы)
    char = string[rand_index] # срез символа по рандомному индексу который выпал выше
    return char # возвращение итога работы функции с рандомным символом

print(choice_from_range('abcdef', 3, 5)) 


