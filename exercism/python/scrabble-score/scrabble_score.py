letters = {
    "aeioulnrst" : 1,
    "dg" : 2,
    "bcmp" : 3,
    "fhvwy" : 4,
    "k" : 5,
    "jx" : 8,
    "qz" : 10
}

def score(word):
    word_lowercase = word.lower()
    counter = 0
    for letter, value in letters.items():
        for ch in word_lowercase:
            if ch in letter:
                counter += value
    return counter
