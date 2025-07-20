import string
UPCASE_ALPHABET = string.ascii_uppercase
LOWER_ALPHABET = string.ascii_lowercase

# def rotate(text, key):
#     if key == 0 or key == 26: # если ключи такие то текст не меняется
#         return text
#     rotated_text = ""
#     for char in text:
#         if char.isalpha():
#             if char.isupper():
#                 old_index = UPCASE_ALPHABET.find(char) 
#                 new_index = old_index + key
#                 if new_index >= len(UPCASE_ALPHABET):
#                     new_index = new_index % len(UPCASE_ALPHABET) # считаем остаток от длины в 26 символов, чтобы не выпадать за индексы алфавита
#                     rotated_text += UPCASE_ALPHABET[new_index] # собираем обработанную строку
#                 else:
#                     rotated_text += UPCASE_ALPHABET[new_index] # если условие пропускается, то просто обрабатываем 
#             if char.islower():
#                 old_index = LOWER_ALPHABET.find(char)
#                 new_index = old_index + key
#                 if new_index >= len(LOWER_ALPHABET):
#                     new_index = new_index % len(LOWER_ALPHABET)
#                     rotated_text += LOWER_ALPHABET[new_index]
#                 else:
#                     rotated_text += LOWER_ALPHABET[new_index]
#         else:
#             rotated_text += char
#     return rotated_text

# убрать дублирование кода

# def rotate(text, key):
#     '''
#     Исключено дублирование кода
#     '''
#     if key == 0 or key == 26: # если ключи такие то текст не меняется
#         return text
#     rotated_text = ""
#     for char in text:
#         if char.isalpha():
#             if char.isupper():
#                 case_for_using = UPCASE_ALPHABET
#             if char.islower():
#                 case_for_using = LOWER_ALPHABET
#             old_index = case_for_using.find(char) 
#             new_index = old_index + key
#             if new_index >= len(case_for_using):
#                 new_index = new_index % len(case_for_using) # считаем остаток от длины в 26 символов, чтобы не выпадать за индексы алфавита
#                 rotated_text += case_for_using[new_index] # собираем обработанную строку
#             else:
#                 rotated_text += case_for_using[new_index] # если условие пропускается, то просто обрабатываем 
#         else:
#             rotated_text += char
#     return rotated_text

UPPER_A = 65
LOWER_A = 97

def rotate(text, key):
    '''
    Алгоритм под таблицу символов
    Заглавные буквы: 65 - 90 лучше в константы 
    Строчные буквы: 97 - 122
    '''
    rotated_text = ""
    for char in text:
        if char.isalpha():
            first_value = UPPER_A if char.isupper() else LOWER_A
            char = chr((ord(char) - first_value + key) % 26 + first_value)
        rotated_text += char
    return rotated_text



# def rotate(text, key):
#     '''
#     Алгоритм под таблицу символов
#     Заглавные буквы: 65 - 90 лучше в константы 
#     Строчные буквы: 97 - 122
#     '''
#     rotated_text = ""
#     for char in text:
#         if char.isalpha():
#             if char.isupper():
#                 char = (ord(char) - UPPER_A + key) % 26 + UPPER_A
#                 rotated_text += chr(char)
#             else:
#                 char = (ord(char) - LOWER_A + key) % 26 + LOWER_A
#                 rotated_text += chr(char)
#         else:
#             rotated_text += char
#     return rotated_text


# print(rotate("o", 13)) #, "a")
print(rotate("z", 1)) #, "a")

# print(rotate("The quick brown fox jumps over the lazy dog.", 13)) # Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
# print(rotate("Let's eat, Grandma!", 21)) #, "Gzo'n zvo, Bmviyhv!")

'''
(ord(char) - 65 + key) % 26 + 65
минус 65 (первая позиция "А"), получаем позицию от 0 до 25 - чистая позиция без таблицы ascii
ключ это смещение шифра, получаем позицию от 0 до 25 но с шифровкой
% 26 это цикличность алфавита:
- 28 % 26 = 2 - то есть позиция пошла с начала
- 5 % 26 = 5 (5 меньше 26, поэтому остаток равен 5).
плюс 65 для получения позиции по таблице но уже со сдвигом
 '''