from symbols import is_vowel # импорт во заданию

def count_vowels(text):
    count = 0 # обнуляю счетчик гласных
    for char in text: # сравнение каждого символа в тексте
        if is_vowel(char): # если функция буквы true 
            count += 1 # счетчик гласных +1
    return count # вернуть посчитанные гласные

print(count_vowels("one")) # => 2