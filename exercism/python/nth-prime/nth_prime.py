# generators

def is_prime(num):
    '''
    имеет ли оно ровно два натуральных делителя: 1 и само себя
    Для этого разделите число на все натуральные числа
    от 2 до его квадратного корня. Если ни одно из этих 
    чисел не делит исходное число без остатка, то число 
    простое
    '''
    if num < 2:
        return False
    for i in range(2, round(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    pr_numbers = [] # для простых чисел
    count = 0 # счетчик простых чисел
    current_num = 2 # текущее число для проверки на простоту

    while count != number: # пока счетчик не равен указанному аргументу
        if is_prime(current_num):
            count += 1 # счетчик простых числен
            pr_numbers.append(current_num) # добавить простое число в список
            current_num += 1 # проверка следующего числа на простоту
        else:
            current_num += 1
            continue

    return pr_numbers[-1]

# убрать список и проверять курент нумбер, короче можно проверять номер итерации и идти по нечетным числам (курент нумбер +2_)