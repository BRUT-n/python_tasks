VOWELS = ("a", "e", "i", "o", "u")

def rule_1(text):
    '''
    Если слово начинается с гласной буквы, или начинается с "xr" или "yt", добавьте звук "ay" в конец слова.
    Примеры:
    "apple" -> "appleay" (начинается с гласной)
    "xray" -> "xrayay" (начинается с "xr")
    "yttria" -> "yttriaay" (начинается с "yt")
    '''

    starts_with_prefix = ("xr", "yt")
    if text.startswith(VOWELS + starts_with_prefix):
        return f"{text}ay"
    return None


def consonants_counter(word): # вычисление количества согласных
    vowels = VOWELS # гласные
    count_of_consonants = 0 # счетчик согласных
    if not word.startswith("y"): # если не начинается с У то добавляем к согласным У
        vowels += ("y", )
    while count_of_consonants < len(word) and word[count_of_consonants] not in vowels: # пока согласных меньше длины слова и буква по индексу не в гласных
        count_of_consonants += 1
    return count_of_consonants


def rule_2(word):
    '''
    Если слово начинается с одной или нескольких согласных букв, сначала переместите эти согласные в 
    конец слова, а затем добавьте звук "ay" в конец слова.
    Примеры:
    "pig" -> "igp" -> "igpay" (начинается с одной согласной)
    "chair" -> "airch" -> "airchay" (начинается с нескольких согласных)
    "thrush" -> "ushthr" -> "ushthray" (начинается с нескольких согласных)
    '''
    index = consonants_counter(word)
    if index >= 1:
        return f"{word[index:]}{word[:index]}ay"


def rule_3(word):
    '''
    Если слово начинается с нуля или более согласных букв, за которыми следует "qu", сначала 
    переместите эти согласные (если они есть) и часть "qu" в конец слова, а затем добавьте звук "ay" в конец слова.
    Примеры:
    "quick" -> "ickqu" -> "ickquay" (начинается с "qu", нет предшествующих согласных)
    "square" -> "aresqu" -> "aresquay" (начинается с одной согласной, за которой следует "qu")
    '''
    qu_chek_index = word.find("qu") # ищем КУ в слове
    if qu_chek_index > -1: # если КУ найдено
        cons_result = consonants_counter(word[:qu_chek_index]) # применяем счет согласных к слову до букв КУ
        # if cons_result == 0:
        #     index = qu_chek_index + 2
        if cons_result < qu_chek_index: # проверка что все буквы до КУ согласные (то есть количество согласных меньше индекса "qu", значит до "qu" только согласные)
            index = cons_result
        else:
            index = cons_result + 2
        return f"{word[index:]}{word[:index]}ay"


def translate_word(word):
    if rule_1(word):
        return rule_1(word)
    if rule_3(word):
        return rule_3(word)
    if rule_2(word):
        return rule_2(word)


def translate(text):
    return " ".join(translate_word(word) for word in text.split())


#---------------
#---------------
# МОЙ ИСХОДНЫЙ ВАРИАНТ
#---------------
#---------------

# def rule_1(text):
#     '''
#     If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.
#     For example:
#     "apple" -> "appleay" (starts with vowel)
#     "xray" -> "xrayay" (starts with "xr")
#     "yttria" -> "yttriaay" (starts with "yt")
#     '''

#     vowels = ("a", "e", "i", "o", "u")
#     starts_with_prefix = ("xr", "yt")
#     if text.startswith(vowels) or text.startswith(starts_with_prefix): #starts with method
#         return text+"ay"
#     return None


# def rule_2_and_3(text):
#     '''
#     If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
#     For example:
#     "pig" -> "igp" -> "igpay" (starts with single consonant)
#     "chair" -> "airch" -> "airchay" (starts with multiple consonants)
#     "thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)
#     OR
#     If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word,
#     and then add an "ay" sound to the end of the word.
#     For example:
#     "quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding consonants)
#     "square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")
#     '''

#     vowels = ("a", "e", "i", "o", "u")
#     index = 0
#     qu_chek_index = text.find("qu") + 1
#     if any(ch in vowels for ch in text[:qu_chek_index]) or qu_chek_index == 0:
#         while index < len(text) and text[index] not in vowels:
#             index += 1
#         return text[index:] + text[:index] + "ay"
#     else:
#         return text[qu_chek_index + 1:] + text[:qu_chek_index - 1] + "qu" + "ay"


# # print(rule_2_and_3("liquid"))#, "iquidlay") тут есть QU, под правило подходит так как не все буквы согласные, ПРАВИЛО 2
# # print(rule_2_and_3("square"))#, "aresquay") тут есть QU, под правило НЕ подходит так как все буквы согласные, ПРАВИЛО 3
# # print(rule_2_and_3("queen"))#, "eenquay") ПРАВИЛО 3


# def rule_4(text):
#     '''
#     If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, 
#     and then add an "ay" sound to the end of the word.
#     Some examples:
#     "my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
#     "rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")
    # Если слово начинается с одной или нескольких согласных букв, за которыми следует "y", сначала переместите согласные, 
    # предшествующие "y", в конец слова, а затем добавьте звук "ay" в конец слова.
    # Примеры:
    # "my" -> "ym" -> "ymay" (начинается с одной согласной, за которой следует "y")
    # "rhythm" -> "ythmrh" -> "ythmrhay" (начинается с нескольких согласных, за которой следует "y")
#     '''
#     vowels = ("a", "e", "i", "o", "u")
#     y_chek_index = text.find("y")
#     if text[0] == "y":
#         return text[1:] + "y" + "ay"
#     if all(ch not in vowels for ch in text[:y_chek_index]):
#         return text[y_chek_index:] + text[:y_chek_index] + "ay"


# def all_rules_for_phrase(text):
#     if " " in text:
#         text = text.split()
#         phrase = ""
#         for word in text:
#             print(word)
#             if rule_1(word):
#                 phrase += f"{rule_1(word)} "
#             if rule_4(word):
#                 phrase += f"{rule_4(word)} "
#             if rule_2_and_3(word):
#                 phrase += f"{rule_2_and_3(word)} "
#         return phrase.strip()
#     return None

# # print(all_rules_for_phrase("quick fast run"))#, "ickquay astfay unray")

# def translate(text):
#     if all_rules_for_phrase(text):
#         return all_rules_for_phrase(text)
#     if rule_1(text):
#         return rule_1(text)
#     if rule_4(text):
#         return rule_4(text)
#     if rule_2_and_3(text):
#         return rule_2_and_3(text)