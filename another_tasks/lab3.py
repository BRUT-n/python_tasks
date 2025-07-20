'''from math import sqrt 
# lab_1
# x1 = 1
# x2 = 1/8 * (-1)

# def x(i: int) -> int:
#     if i == 1:
#         return 1
#     if i == 2:
#         return -1 / 8
#     return ((i - 1) * x(i - 1) / 3) + ((i - 2) * x(i - 2) / 4)

# print(x(2))
'''

'''
# def x(i: int) -> int:
#     if i < 4:
#         return 0
#     return x(i-1) + x(i-3)

# print(x(10))
'''

'''
def a(k):
    if k == 1:
        return 1
    return 0.5 * (sqrt(b(k-1) + 0.5 * sqrt(a(k-1))))

def b(k):
    if k == 1:
        return 1
    return 1.5 * sqrt(b(k-1)) + 0.5 * (a(k-1))**2

for k in range(1, 6):
    print(a(k), b(k))
'''



'''
def count(lst: list):
    if isinstance(lst, list):
        if len(lst) == 0:
            return 0
        if len(lst) == 1:
            return count(lst[0])
        else:
            return count(lst[0]) + count(lst[1:])
    return 1


print(len([[[1, 2, 3]]]))

print(count([])) # -> 0

print(count([1, 2, 3])) # -> 3

print(count(["x", "y", ["z"]])) # -> 4

print(count([1, 2, [3, 4, [5]]])) # -> 7
'''

def is_palindrome(text: str | list):
        if text[0] == text[-1]:
            return is_palindrome(text[1:]) == is_palindrome(text[:-1])
        return False


         


print(is_palindrome([1, 2, 3, 2, 1])) #True

print(is_palindrome('spam')) #False

print(is_palindrome('аааааа'))

# lst = [1, 2, 4, 6, 7]
# print(lst[0:])
# print(lst[:-1])