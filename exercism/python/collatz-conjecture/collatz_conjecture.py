def steps(number):
    step = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        number = number * 3 + 1 if number % 2 else number // 2 # тернарное выражение (краткий способ записи условного оператора в одну строку)
        step += 1
    return step


    #     if number % 2 == 0:
    #         number = number // 2 # целочисленное деление
    #     else:
    #         number = number * 3 + 1
    #     step += 1
    # return step
