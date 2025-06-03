def rule_1(text):
    '''
    If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.
    For example:
    "apple" -> "appleay" (starts with vowel)
    "xray" -> "xrayay" (starts with "xr")
    "yttria" -> "yttriaay" (starts with "yt")
    '''

    vowels = ("a", "e", "i", "o", "u")
    starts_with_prefix = ("xr", "yt")
    if text.startswith(vowels) or text.startswith(starts_with_prefix): #starts with method
        return text+"ay"
    return None

# print(rule_1("apple"))#, "appleay")
# print(rule_1("ear"))#, "earay")
# print(rule_1("igloo"))#, "iglooay")
# print(rule_1("object"))# "objectay")
# print(rule_1("under"))#, "underay")


def rule_2_and_3(text):
    '''
    If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
    For example:
    "pig" -> "igp" -> "igpay" (starts with single consonant)
    "chair" -> "airch" -> "airchay" (starts with multiple consonants)
    "thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)
    OR
    If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word,
    and then add an "ay" sound to the end of the word.
    For example:
    "quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding consonants)
    "square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")
    '''

    vowels = ("a", "e", "i", "o", "u")
    index = 0
    qu_chek_index = text.find("qu") + 1
    if any(ch in vowels for ch in text[:qu_chek_index]) or qu_chek_index == 0:
        while index < len(text) and text[index] not in vowels:
            index += 1
        return text[index:] + text[:index] + "ay"
    else:
        return text[qu_chek_index + 1:] + text[:qu_chek_index - 1] + "qu" + "ay"

# print(rule_2_and_3("pig"))#, "igpay")
# print(rule_2_and_3("koala"))#, "oalakay")
# print(rule_2_and_3("xenon"))#, "enonxay")
# print(rule_2_and_3("qat"))#, "atqay")
# print(rule_2_and_3("liquid"))#, "iquidlay") тут есть QU, под правило подходит так как не все буквы согласные, ПРАВИЛО 2
# print(rule_2_and_3("chair"))#, "airchay")
# print(rule_2_and_3("therapy"))#, "erapythay")
# print(rule_2_and_3("thrush"))#, "ushthray")
# print(rule_2_and_3("school"))#, "oolschay")
# print(rule_2_and_3("square"))#, "aresquay") тут есть QU, под правило НЕ подходит так как все буквы согласные, ПРАВИЛО 3
# print(rule_2_and_3("queen"))#, "eenquay") ПРАВИЛО 3


def rule_4(text):
    '''
    If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, 
    and then add an "ay" sound to the end of the word.
    Some examples:
    "my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
    "rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")
    '''
    vowels = ("a", "e", "i", "o", "u")
    y_chek_index = text.find("y")
    if text[0] == "y":
        return text[1:] + "y" + "ay"
    if all(ch not in vowels for ch in text[:y_chek_index]):
        return text[y_chek_index:] + text[:y_chek_index] + "ay"

# print(rule_4("yellow"))#, "ellowyay")
# print(rule_4("rhythm"))#, "ythmrhay")
# print(rule_4("my"))#, "ymay")


def all_rules_for_phrase(text):
    if " " in text:
        text = text.split()
        phrase = ""
        for word in text:
            print(word)
            if rule_1(word):
                phrase += f"{rule_1(word)} "
            if rule_4(word):
                phrase += f"{rule_4(word)} "
            if rule_2_and_3(word):
                phrase += f"{rule_2_and_3(word)} "
        return phrase.strip()
    return None

# print(all_rules_for_phrase("quick fast run"))#, "ickquay astfay unray")


def translate(text):
    if all_rules_for_phrase(text):
        return all_rules_for_phrase(text)
    if rule_1(text):
        return rule_1(text)
    if rule_4(text):
        return rule_4(text)
    if rule_2_and_3(text):
        return rule_2_and_3(text)
