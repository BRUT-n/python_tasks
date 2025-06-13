def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number in (1, 2):
        return "deficient"
    total_sum = 0
    divisor_counter = 0
    new_number = number // 2
    while divisor_counter <= new_number:
        divisor_counter += 1
        if number % divisor_counter == 0:
            total_sum += divisor_counter
    if total_sum == number:
        return "perfect"
    if total_sum > number:
        return "abundant"
    return "deficient"
    

print(classify(2))