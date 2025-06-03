def square_root(number):
    if number == 1:# решение Итерационной формулой Герона (рекурентная)
        return 1
    testing_number = 1
    int_testing_number= 1
    while int_testing_number * int_testing_number != number:
        testing_number = 0.5 * (testing_number + number / testing_number)
        int_testing_number = int(testing_number)
    return int(testing_number)

print(square_root(16))

# 1e-2 = 0.01

# def square_root(number):
    # if number == 1:
        # return 1
    # first_index = 0 # binary search approach
    # middle_index = 0
    # last_index = number
    # while middle_index * middle_index != number:
        # middle_index = (first_index + last_index) // 2
        # if middle_index * middle_index > number:
            # last_index = middle_index
        # if middle_index * middle_index < number:
            # first_index = middle_index
    # return middle_index

# def square_root(number):
    # sqr_number = 1
    # while sqr_number * sqr_number != number:
        # sqr_number += 1
    # return sqr_number