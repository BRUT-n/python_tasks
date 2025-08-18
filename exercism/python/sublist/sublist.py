"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_sublist(list_one, list_two):
    for i in range(len(list_two)):
        if list_one == list_two[i:i + len(list_one)]:
            return True
    return False


def sublist(list_one, list_two):
    '''
    1. Списки равны: Список A равен списку B, если они содержат одни и те же элементы в том же порядке.
    2. A - суперсписок B: Список A является суперсписком списка B, если A содержит непрерывную подпоследовательность 
    элементов, равную B. (То есть, B содержится в A как последовательность идущих подряд элементов).
    A = [1, 2, 3, 4, 5], B = [2, 3, 4] -> "superlist" (B содержится в A)
    3. A - подсписок B: Список A является подсписком списка B, если B содержит непрерывную подпоследовательность 
    элементов, равную A. (То есть, A содержится в B как последовательность идущих подряд элементов).
    A = [1, 2, 3], B = [1, 2, 3, 4, 5] -> "sublist" (A содержится в B)
    A = [3, 4, 5], B = [1, 2, 3, 4, 5] -> "sublist" (A содержится в B)
    4. Списки неравны (не связаны): Ни одно из вышеперечисленных утверждений не верно.
    '''
    if list_one == list_two:
        return EQUAL
    if list_two == []:
        return SUPERLIST
    if list_one == []:
        return SUBLIST
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    # if len(list_one) < len(list_two): # логика функции описанной отдельно
    #     i = 0
    #     while i < len(list_two):
    #         if list_one == list_two[i:i + len(list_one)]:
    #             return SUBLIST
    #         i += 1
    # if len(list_one) > len(list_two):
    #     i = 0
    #     while i < len(list_one):
    #         if list_two == list_one[i: i + len(list_two)]:
    #             return SUPERLIST
    #         i += 1
    return UNEQUAL

