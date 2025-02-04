from random import randint # из модуля рандом импортируем функцию рандинт

random_number = randint(1, 100) # рандомный номер от 1 до 100
print(random_number) # вывод

string = "abcde"
random_index = randint(0, len(string) - 1) # строка имеет длину 5, а индексы идут с 0, поэтому лен()-1
char = string[random_index]
print(random_index)
print(char)

