def string_or_not(object):
    return isinstance(object, str) and "yes" or "no" # true and "yes" дает true, а and возвращает последнее true (т.е. yes)
    # 1 и 1 или 1 если строка,по логике возврат функции - вторая единица, потому что это первое true значение
    # 0 и 1 или 1 если не строка, то по логике в итоге остается 0 или 1, и or возвращает последнее true значение

print(string_or_not("this_is_string"))