def equilateral(sides):
    return sides[0] == sides[1] == sides[2] and all(value > 0 for value in sides)

def isosceles(sides):
    a, b, c = sides
    return is_triangle(a, b, c) and (a == b or a == c or b == c)
    # if a + b >= c and b + c >= a and a + c >= b: # условие того что может быть треугольником
    #     return a == b or a == c or b == c
    # return False


def scalene(sides):
    a, b, c = sides
    return is_triangle(a, b, c) and a != b and a != c and b != c
    # if a + b >= c and b + c >= a and a + c >= b: # условие того что может быть треугольником
    #     return a != b and a != c and b != c
    # return False

def is_triangle(a, b, c):
    return a + b >= c and b + c >= a and a + c >= b