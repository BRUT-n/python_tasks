from itertools import product

def sum_of_multiples(limit, multiples):
    score = set()
    for item, num in product(multiples, range(1, limit)): # собирает тюпл по-элементно с итераблами в аргументах
        if item and num % item == 0:
            score.add(num)
    return sum(score)

    # score = set()
    # for item in multiples:
    #     for num in range(1, limit):
    #         if item and num % item == 0:
    #             score.add(num)
    # return sum(score)