def response(hey_bob):
    question_mark_answer = "Sure."
    yelling_answer = "Whoa, chill out!"
    yelling_question_answer = "Calm down, I know what I'm doing!"
    silence_answer = "Fine. Be that way!"
    other_answer = "Whatever."
    

    if hey_bob.isspace() or hey_bob == "": # проверка пустой строки
        return silence_answer
    if hey_bob.isupper() and hey_bob.endswith("?"): # все буквы большие и окончание "?"
        return yelling_question_answer
    if hey_bob.strip().endswith("?"):
        return question_mark_answer
    if hey_bob.isupper():
        return yelling_answer
    return other_answer # обработка остальных случаев


    # if hey_bob.isspace() or hey_bob == "": # проверка пустой строки
    #     return silence_answer
    # if all(not char.isalpha() for char in hey_bob): # проверка "все символы не буквенные"
    #     if hey_bob.endswith("?"): # проверка выражения "не буквенных" на оконочание "?"
    #         return question_mark_answer
    #     return other_answer # если "не буквенные" и не оканчиваются на "?"
    # if any(char.isalpha() for char in hey_bob): # проверка "какие то символы буквенные"
    #     if hey_bob == hey_bob.upper() and hey_bob.endswith("?"): # все буквы большие и окончание "?"
    #         return yelling_question_answer 
    #     if hey_bob == hey_bob.upper() and not hey_bob.endswith("?"): # все буквы большие и оконание "?"
    #         return yelling_answer # 
    #     if hey_bob.strip().endswith("?"): # обрезать пробелы и проверить окончание на "?"
    #         return question_mark_answer
    #     return other_answer # обработка остальных случаев