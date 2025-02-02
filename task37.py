def has_char(string, char):
    index = 0 # обнуления индекса 
    while index < len(string): # сравнение индекса с длиной строки
        if string[index] == char.lower() or string[index] == char.upper(): # сравнение символ(индекс) с малым и большим регистром
            return True # если условия выше true возвращаю true
        index += 1 # если условия не выполнены увеличиваю индекс на 1 и цикл начинает сравление следующего знака по индексу
    return False # если условия после всех проверок не выполнено то возвращается false

print(has_char('Hexlet', 'H'))  # => True
print(has_char('Hexlet', 'h'))  # => True
print(has_char('Awesomeness', 'd'))  # => False