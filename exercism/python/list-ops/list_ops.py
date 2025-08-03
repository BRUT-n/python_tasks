from itertools import chain

def append(list1, list2):
    return list1 + list2

# def concat(lists):
    # result = []
    # for ch in lists:
        # result += ch
    # return result

def concat(lists):
    return list(chain(*lists))

# print(concat([[1, 2], [3], [], [4, 5, 6]]))#, [1, 2, 3, 4, 5, 6])

# def filter(function, list):
#     result = []
#     for ch in list:
#         if function(ch):
#             result += [ch]
#     return result

def filter(function, list):
    return [el for el in list if function(el)]

# print(filter(lambda x: x % 2 == 1, []))
# print(filter(lambda x: x % 2 == 1, [1, 2, 3, 5]))

# def length(list):
#     result = 0
#     for ch in list:
#         if ch:
#             result += 1
#     return result

def length(list):
    return sum(1 for _ in list)

# def map(function, list):
    # result = []
    # for ch in list:
        # result += [function(ch)]
    # return result

def map(function, list):
    return [function(el) for el in list]

def foldl(function, list, acc):
    result = acc
    for el in list:
        result = function(result, el)
    return result

# print(foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5)) #, 15)

# def foldr(function, list, acc):
#     result = acc
#     for el in list[::-1]:
#         result = function(result, el)
#     return result

def foldr(function, list, acc):
    return foldl(function, list[::-1], acc)

def reverse(list):
    return list[::-1]
