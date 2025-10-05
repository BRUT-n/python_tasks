def decode(string):
    result = ""
    index = 0 # для хранения обработанных индексов
    numbers_counter = ""  # счетчик цифр из аргумента
    while index < len(string): # пока индекс не длинее стринги
        if string[index].isdigit() and string[index + 1].isdigit(): # проверка двухзначных чисел
            numbers_counter += string[index] + string[index + 1] # сбор в переменную двух чисел
            result += int(numbers_counter) * string[index + 2] # запись в результат двухзнач. число * символ
            numbers_counter = "" # обнуление счетчика
            index += 3 # увеличение на количество обработанных символов
        elif string[index].isdigit(): # если однознач. число
            result += int(string[index]) * string[index+1] # число * символы += результат
            index += 2 # перескок на 2 индекса
        else:
            result += string[index] # просто символ в результат
            index += 1
    return result

# раскидать декод на любое количество чисел

def encode(string):
    if len(string) < 2:
        return string
    result = ""
    repeats = 1
    for i in range(1, len(string) + 1):
        if i == len(string) or string[i] != string[i - 1]:
            if repeats > 1:
                result += str(repeats)
            result += string[i - 1]
            repeats = 1
        else:
            repeats += 1
    return result


print(encode("  hsqq qww  ")) #, "2 hs2q q2w2 ")
print(encode("aabbbcccc")) #, "2a3b4c")

