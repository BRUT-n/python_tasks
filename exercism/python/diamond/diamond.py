from string import ascii_uppercase
ALPHABET = ascii_uppercase

def rows(letter):
    # if letter == "A":
    #     return ["A"]

    dimond = []
    letter_index = ALPHABET.index(letter) # индекс буквы для итерации по алфавиту
    dimond_width = letter_index * 2 + 1 # ширина алмаза (буквы и пробелы)
    spaces = dimond_width # переменная для изменения пробелов
    
    # while letter_index > 0:
    #     new_sting = ALPHABET[letter_index] + (" " * (spaces - 2)) + ALPHABET[letter_index]
    #     dimond.append(new_sting.center(dimond_width, " "))
    #     letter_index -= 1
    #     spaces -= 2

    for i in range(letter_index, 0, -1): # новый код
        new_sting = ALPHABET[i] + (" " * (spaces - 2)) + ALPHABET[i]
        dimond.append(new_sting.center(dimond_width, " "))
        spaces -= 2

    dimond.append("A".center(dimond_width, " "))

    return dimond[::-1] + dimond[1:]
