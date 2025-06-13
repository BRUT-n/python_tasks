def is_valid(isbn):
    clear_isbn = isbn.replace("-","") # убираем лишние знаки в строке
    # lats_char_verify = ("X", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9") # разрешенные последние символы
    if len(clear_isbn) != 10: # обработка если длина не проходит
        return False
    last_char = clear_isbn[-1]
    # if clear_isbn[-1] not in lats_char_verify: # обработка если не проходит по последнему символу
    #     return False
    if not last_char.isdigit() and last_char != "X":
        return False
    total = 0 # счетчик суммы
    factor = 10 # множитель из формулы
    for index in range(9): # все индексы кроме последнего символа
        if not clear_isbn[index].isdigit(): # если какое-то значение по индексу = текст, то сразу в отказ
            return False
        total += int(clear_isbn[index]) * factor # добавление в сумму значения по индексу на множитель
        factor -= 1 # множитель -1 
    if last_char == "X": # проверка последнего символа на Х, добавляем 10 просто, потому что 10*1 это 10
        total += 10
    else: # иначе добавляем к сумме само число, потому что число*1 это число
        total += int(last_char)
    return total % 11 == 0
