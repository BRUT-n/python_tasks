def sum(numbers):
    result = 0
    for num in numbers:
        result += int(num)
    return result

print(sum("12345")) #15