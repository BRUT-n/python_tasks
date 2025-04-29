def is_pangram(sentence):
    sentence = sentence.upper()
    alphabet = "BCDFGHJKLMNPQRSTVWXZAEIOU"
    return all(letter in sentence for letter in alphabet)
