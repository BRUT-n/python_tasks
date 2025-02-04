def get_age_difference(year1: int, year2: int) -> str: # функция с вводом параметров int и выводом в str
    result = abs(year1-year2) # модуль вычитания значений указанных пользователем
    return "The age difference is " + f'{result}' # возвращение указанного текста с результатом работы функции

actual = get_age_difference(2001, 2018) # условие (если в возвращении указать print, работать почему то не будет)
print(actual)