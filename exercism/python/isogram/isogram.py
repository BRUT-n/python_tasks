def is_isogram(string):
    cut_lower_string = string.lower().replace(",", "").replace("-", "").replace(" ", "") # можно через translate или через count
    set_of_chars = set(cut_lower_string)
    return len(cut_lower_string) == len(set_of_chars)