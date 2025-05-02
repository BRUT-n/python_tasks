def find(search_list, value):
    first_index = 0
    last_index = len(search_list) - 1
    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        if search_list[middle_index] == value:
            return middle_index
        if search_list[middle_index] < value:
            first_index = middle_index + 1
        if search_list[middle_index] > value:
            last_index = middle_index - 1
    raise ValueError("value not in array")



print(find([1, 3, 4, 6, 8, 9, 11], 6)) #, 3)

print(find([1, 3, 4, 6, 8, 9, 11], 1)) #, 0)

print(find([1, 3, 4, 6, 8, 9, 11], 11)) #, 6)

print(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144)) #, 9

print(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21)) #, 5)