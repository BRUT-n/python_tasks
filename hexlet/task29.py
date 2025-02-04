def has_upper_case(word) ->str:
    return word != word.casefold() # возвращаю word НЕ РАВНО выполнению метода casefold к word который переводит строку в строчные буквы и сравнивает с тем, что введено

print (has_upper_case('pytHon')) # -> True