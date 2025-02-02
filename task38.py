def filter_string(text, char): # задача функции
    text = text.strip() # убираю пробелы с начала и с конца заданного текста
    result = "" # пустая переменная для складываения в нее результата работы цикла for
    for current_char in text: # текущий символ в заданном тексте
        if current_char.lower() != char.lower(): # если нижний регистр текущего символа не равен символу введенному во втором параметре
            result = result + current_char # то в результат записываем текущий символ (с помощью for проходить весь текст что введет в первом параметре)
    return result.strip() # возвращаем результат с обрезанными пробелами (Ваня, почему-то без метода .trip мое решение не принималось, почему?)

# ВЫВОД ОШИБКИ ПРИ ПРОВЕРКИ РЕШЕНИЯ БЕЗ МЕТОДА:
#  def test():
#     text = 'I look back if you are lost'
#     assert filter_string(text, 'w') == 'I look back if you are lost'
#>       assert filter_string(text, 'I') == 'look back f you are lost'
#E       AssertionError: assert ' look back f you are lost' == 'look back f you are lost'
#E         
#E         - look back f you are lost
#E         +  look back f you are lost
#E         ? +

text = '     I look back if you are lost'
print(filter_string(text, 'i'))  # 'look back f you are lost'
print(filter_string(text, 'O'))  # 'I lk back if yu are lst'
print(filter_string(text, 'x'))  # 'I look back if you are lost'