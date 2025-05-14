def to_rna(dna_strand):
    dna_to_rna = {"G":"C", "C":"G", "T":"A", "A":"U"}
    return "".join(dna_to_rna[letter] for letter in dna_strand)
    
    # dna_to_rna_converting = {"G":"C", "C":"G", "T":"A", "A":"U"} # решение через словарь
    # converting_table = dna_strand.maketrans(dna_to_rna_converting) # создание таблицы преобразования к строке на основе словаря
    # rna = dna_strand.translate(converting_table) # использование таблицы преобразования к строке
    # return rna

    # решение через две строки для создания словаря
    # dna_nucleotides = "GCTA"
    # rna_nucleotides = "CGAU"
    # replacing_table_for_dna = dna_strand.maketrans(dna_nucleotides, rna_nucleotides)
    # rna_stand = dna_strand.translate(replacing_table_for_dna)
    # return rna_stand