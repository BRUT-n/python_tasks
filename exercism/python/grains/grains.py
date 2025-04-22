def square(number):
    grains = 1
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        grains = 1
    else:
        while number != 1:
            grains *= 2
            number -= 1
            if number == 0:
                continue
    return grains


def total():
    total_result = 0
    for number in range(1,65):
        total_result += square(number)
    return total_result