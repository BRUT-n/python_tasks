def is_palindrome(text):
    result = "" # пустая переменная для складывания в нее обратной строки
    if text == "": # сразу проверка пустой строки
        return True # если она пустая функция сразу выдает результат и цикл заканчивается
    for char in text: # цикл для каждого символа в тексте 
        result = char + result # запись в результат текста В ОБРАТНОМ ПОРЯДКЕ
        if result == text: # если обратно записанный текст равен введенному исходному тексту
            return True  # то текст является палиндромом - вывод тру
    return False # иначе не является палиндровов - вывод фолс

print(is_palindrome(''))  # True пустая строка тоже считается палиндромом
print(is_palindrome('radar')) # True
print(is_palindrome('a')) # True
print(is_palindrome('abs')) # False
print(is_palindrome('ишак ищет у тещи каши')) # True