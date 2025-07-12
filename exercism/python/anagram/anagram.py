def find_anagrams(word, candidates):
    word_list = [] # списко для коллекции анагарм
    lower_word = sorted(word.lower()) # сортировка маленьких букв по алфавиту
    for item in candidates: # итерация по кандидатам
        completed_item = sorted(item.lower()) # перевод кандидатов в нижний регистр и сортировка для сравнения
        if completed_item == lower_word and word.lower() != item.lower(): # сравнение сортированных букв И что слово не является самим собой
            word_list.append(item)
    return word_list

# candidates = ["ΒΓΑ", "ΒΓΔ", "γβα", "αβγ"]
# expected = ["ΒΓΑ", "γβα"]
# print(find_anagrams("ΑΒΓ", candidates)) #, expected)

# candidates = ["Banana"]
# expected = []
# print(find_anagrams("BANANA", candidates)) #, expected)

# candidates = ["banana"]
# expected = []
# print(find_anagrams("BANANA", candidates)) #, expected)

greek = [ord(a) for a in "γβα"]
rus = [ord(r) for r in "гва"]
print(sorted("γβα"))
print(sorted("ΑΒΓ"))
print("γβα" == "авг")
print(greek)
print(rus)