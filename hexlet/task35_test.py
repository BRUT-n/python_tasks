def multiply_numbers_from_range(start, finish): # код из теста по теории
    i = start # и равно старту то есть 3
    multiply = 1 # произведение приводиться к 1, чтобы потом умножать на нужное число
    while i <= finish: # пока И меньше или равно заданному числу то есть 5
        multiply *= i # выполнить умножение 1 на число И
        i += 1 # и увеличить И на следующее по порядку
    return multiply
print(multiply_numbers_from_range(3, 5))  # 60