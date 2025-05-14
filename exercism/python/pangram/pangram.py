from string import ascii_uppercase

def is_pangram(sentence):
    sentence = set(sentence.upper())
    alphabet = set(ascii_uppercase)
    return sentence >= alphabet
    # sentence = sentence.upper()
    # return all(letter in sentence for letter in ascii_uppercase)
