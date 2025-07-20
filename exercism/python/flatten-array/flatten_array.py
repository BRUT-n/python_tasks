def flatten(iterable):
    elemets = []
    def rec_lst(iterable):
        for ch in iterable:
            if isinstance(ch, list):
                rec_lst(ch)
            else:
                elemets.append(ch)
    rec_lst(iterable)
    clean_lst = [value for value in elemets if value is not None]
    return clean_lst

# переписать в одну функцию, решить вопрос обнуляемой переменной