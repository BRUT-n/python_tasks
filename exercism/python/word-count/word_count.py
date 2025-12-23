def count_words(sentence):
    clear_string = ""
    for ch in sentence.lower():
        if ch.isalpha() or ch.isdigit() or ch == " " or ch =="'":
            clear_string += ch
        else:
            clear_string += " "
    clear_string = clear_string.split() # сплит без аргументов обрезает лишние пробелы
    result = {}
    for element in clear_string:
        clear_element = element.strip("'") # обрезает лишние ' при необходимости
        if len(clear_element): # проверка после обрезки на пустоту элемента
            result[clear_element] = result.get(clear_element, 0) + 1 # если элемента нет, то значение по умолчанию 0 и к нему прибавляется 1 для добавления в словарь и последуюего подсчета
    return result

#dicts