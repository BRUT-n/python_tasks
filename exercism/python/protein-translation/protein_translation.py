TRANSLATE_TABLE = {
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "UUC" : "Phenylalanine",
    "UUA" : "Leucine",
    "UUG" : "Leucine",
    "UCU" : "Serine",
    "UCC" : "Serine",
    "UCA" : "Serine",
    "UCG" : "Serine",
    "UAU" : "Tyrosine",
    "UAC" : "Tyrosine",
    "UGU" : "Cysteine",
    "UGC" : "Cysteine",
    "UGG" : "Tryptophan",
    "UAA" : "STOP",
    "UAG" : "STOP",
    "UGA" : "STOP"
}
 # перевернуть словарь и переписать под него

def spliting(text):
    return [text[i: i + 3] for i in range(0, len(text), 3)]

def proteins(strand):
    strand_split = spliting(strand)
    result = []
    for codom in strand_split:
        if TRANSLATE_TABLE[codom] == "STOP":
            return result
        result.append(TRANSLATE_TABLE[codom])
    return result

value = "UGGUAG"
expected = ["Tryptophan"]
print(proteins(value)) #, expected)

