import string
UPCASE_ALPHABET = string.ascii_uppercase
LOWER_ALPHABET = string.ascii_lowercase

def rotate(text, key):
    if key == 0 or key == 26: # если ключи такие то текст не меняется
        return text
    rotated_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                old_index = UPCASE_ALPHABET.find(char) 
                new_index = old_index + key
                if new_index >= len(UPCASE_ALPHABET):
                    new_index = new_index % len(UPCASE_ALPHABET) # считаем остаток от длины в 26 символов, чтобы не выпадать за индексы алфавита
                    rotated_text += UPCASE_ALPHABET[new_index] # собираем обработанную строку
                else:
                    rotated_text += UPCASE_ALPHABET[new_index] # если условие пропускается, то просто обрабатываем 
            if char.islower():
                old_index = LOWER_ALPHABET.find(char)
                new_index = old_index + key
                if new_index >= len(LOWER_ALPHABET):
                    new_index = new_index % len(LOWER_ALPHABET)
                    rotated_text += LOWER_ALPHABET[new_index]
                else:
                    rotated_text += LOWER_ALPHABET[new_index]
        else:
            rotated_text += char
    return rotated_text

print(rotate("n", 13)) #, "a")
print(rotate("The quick brown fox jumps over the lazy dog.", 13)) # Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
print(rotate("Let's eat, Grandma!", 21)) #, "Gzo'n zvo, Bmviyhv!")