def reverse_string(string):
    index = len(string) - 1 # впеременную записывается индекс последнего символа строки
    reversed_string = '' # переменная для записи результата работы цикла

    while index >= 0: # условие где повторяется блок цикла пока индекс не дошел до 0 (первого символа)
        current_char = string[index] # берется из строки символ по текущему индексу
        reversed_string = reversed_string + current_char # строка-результат + новый символ
        # То же самое через интерполяцию
        # reversed_string = f'{reversed_string}{current_char}'
        index = index - 1 # обновляем счетчик

    return reversed_string # возвращение строки результата

print(reverse_string('Game Of Thrones'))  # 'senorhT fO emaG'
# Проверка нейтрального элемента
reverse_string('')  # ''