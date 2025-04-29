from math import sqrt

def score(x, y):
    value = sqrt(x ** 2 + y ** 2) # формула вычисления расстояния от точки до центра координат(0, 0) 
    if value <= 1:
        return 10
    if value <= 5:
        return 5
    if value <= 10:
        return 1
    return 0
