# tuples
main_numbers = { # основные римские символы и спец. комбинации
    1000 : "M",
    900 : "CM",
    500 : "D",
    400 : "CD",
    100 : "C",
    90 : "XC",
    50 : "L",
    40 : "XL",
    10 : "X",
    9 : "IX",
    5 : "V",
    4 : "IV",
    1 : "I"
}

def roman(number):
    result = ""
    while number != 0: # цикл вычитания из исходного числа наибольшего из словаря
        for key, value in main_numbers.items():
            while number >= key: # на случай если разряд после одно вычитания не изменился, вычитается еще раз
                number -= key
                result += value
    return result
