def factors(value):
    factor = 2
    result = []
    number = value
    while number != 1:
        if number % factor == 0:
            number = number / factor
            result.append(factor)
        else:
            factor += 1
    return result