def square_root(number):
    if number == 1:
        return 1
    first_index = 0 # binary search approach
    middle_index = 0
    last_index = number
    while middle_index * middle_index != number:
        middle_index = (first_index + last_index) // 2
        if middle_index * middle_index > number:
            last_index = middle_index
        if middle_index * middle_index < number:
            first_index = middle_index
    return middle_index

# def square_root(number):
    # sqr_number = 1
    # while sqr_number * sqr_number != number:
        # sqr_number += 1
    # return sqr_number