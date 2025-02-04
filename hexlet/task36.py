def get_substr(string: str, cut_num: int):
    index = 0 # задаю индекс 0 (индекс первого символа)
    cut_str = "" # объявление пустой переменной для записи в нее значания обрез. строки

    while index < cut_num: # условие где индекс меньше введенного числа по второму параметру
        current_s = string[index] # текущий символ = символ введенной фразы [по индексу]
        cut_str = f'{cut_str}{current_s}' # запись в переменную вывода = обрез. строка + текущий символ из результата работы строки выше
        index += 1 # индекс +1 потому что двигаемся по строке слева (индекс 0) направо (индексы 1,2,3... cut_num)
    return cut_str
        
    
    
string = 'If I look back I am lost'
print(get_substr(string, 1))  # => 'I'
print(get_substr(string, 10))  # => 'If I lo'