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

def rule_2(text):
    '''
    If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
    For example:
    "pig" -> "igp" -> "igpay" (starts with single consonant)
    "chair" -> "airch" -> "airchay" (starts with multiple consonants)
    "thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)
    '''
    vowels = ("a", "e", "i", "o", "u")
    index = 0
    for char in text:
        while char not in vowels:
            index += 1
    return text[index:] + text[:index] + "ay"
            # return text[3:]+text[0:3]+"ay"

print(rule_2("pig"))#, "igpay")
print(rule_2("koala"))#, "oalakay")
print(rule_2("xenon"))#, "enonxay")
print(rule_2("qat"))#, "atqay")
print(rule_2("liquid"))#, "iquidlay")
print(rule_2("chair"))#, "airchay")
print(rule_2("therapy"))#, "erapythay")
print(rule_2("thrush"))#, "ushthray")
print(rule_2("school"))#, "oolschay")


# def translate(text):

#     if "qu" in text:
#         qu_index = text.find("qu")
#         print(qu_index)
#         return text[qu_index:] + text[0:qu_index] + "ay"

#     if text[0] not in vowels:
#         return text[1:]+text[0]+"ay"




# print(translate("school")) #, "oolschay")

# print(translate("equal")) #, "equalay")

# print(translate("chair"))#, "airchay")

# print(translate("queen"))#, "eenquay")