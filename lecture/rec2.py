def sum_list(lst: list[int]) -> int:
    # return sum(lst)
    result = 0
    for i in lst:
        result += i
    return result



def sum_list_rec(lst: list[int]) -> int:
    if not lst:
        return 0
    return lst[0] + sum_list_rec(lst[1:])


# sum = lst[0] + lst[1] + ... + lst[len(lst) - 2] + lst[len(lst) - 1]


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    print(f"{l=} {sum_list_rec(l)=}")
