import string
ALPHABET = string.ascii_lowercase
REV_ALPHABET = ALPHABET[::-1]

# String Methods

# исходный вариант, но убран лишний елиф

# def encode(plain_text):
#     lower_text = plain_text.lower()
#     encoding = ""
#     for ch in lower_text:
#         if ch.isalpha():
#             encoding += REV_ALPHABET[ALPHABET.index(ch)]
#         if ch.isdigit():
#             encoding += ch
#     spacing = ""
#     counter = 0
#     for new_ch in encoding:
#         spacing += new_ch
#         counter += 1        
#         if counter == 5:
#             spacing += " "
#             counter = 0
#     return spacing.strip()

# def decode(ciphered_text):
#     decoding = ''
#     for ch in ciphered_text:

#         if ch.isalpha():
#             decoding += ALPHABET[REV_ALPHABET.index(ch)]
#         if ch.isdigit():
#             decoding += ch
#     return decoding

# сделать функцию под одинаковый код

def first_step(text, is_ciphered = True):
    lower_text = text.lower()
    result = ""
    if is_ciphered:
        en_alphabet = ALPHABET
        de_alphabet = REV_ALPHABET
    else:
        en_alphabet = REV_ALPHABET
        de_alphabet = ALPHABET
    for ch in lower_text:
        if ch.isalpha():
            result += en_alphabet[de_alphabet.index(ch)]
        if ch.isdigit():
            result += ch
    return result

def encode(plain_text):
    encoding = first_step(plain_text, is_ciphered=False)
    spacing = ""
    counter = 0
    for new_ch in encoding:
        spacing += new_ch
        counter += 1        
        if counter == 5:
            spacing += " "
            counter = 0
    return spacing.strip()

def decode(ciphered_text):
    return first_step(ciphered_text, is_ciphered=True)

# print(encode("yes")) #, "bvh")
# print(encode("mindblowingly")) #, "nrmwy oldrm tob")
# print(encode("Truth is fiction.")) #, "gifgs rhurx grlm")
# print(encode("Testing,1 2 3, testing.")) #, "gvhgr mt123 gvhgr mt")

# написать по кодам букв алфавита

'''
(ord(char) - 65 + key) % 26 + 65
минус 65 (первая позиция "А"), получаем позицию от 0 до 25 - чистая позиция без таблицы ascii
ключ это смещение шифра, получаем позицию от 0 до 25 но с шифровкой
% 26 это цикличность алфавита:
- 28 % 26 = 2 - то есть позиция пошла с начала
- 5 % 26 = 5 (5 меньше 26, поэтому остаток равен 5).
плюс 65 для получения позиции по таблице но уже со сдвигом
'''

LOWER_A = 97
LOWER_Z = 122

def first_step(text, is_ciphered = True):
    lower_text = text.lower()
    result = ""
    if is_ciphered:
        en_alphabet = ALPHABET
        de_alphabet = REV_ALPHABET
    else:
        en_alphabet = REV_ALPHABET
        de_alphabet = ALPHABET
    for ch in lower_text:
        if ch.isalpha():
            result += en_alphabet[de_alphabet.index(ch)]
        if ch.isdigit():
            result += ch
    return result

def encode(plain_text):
    pass

def decode(ciphered_text):
    pass
