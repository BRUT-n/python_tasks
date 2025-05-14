def is_armstrong_number(number):
    string_number = str(number)
    count = 0
    for num in string_number:
        num = int(num)
        f = num ** len(string_number)
        count += f
    return count == number