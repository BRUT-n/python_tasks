COLOR_CODE = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

def value(colors):
    result = ""
    only_two_colors = colors[:2]
    for name in only_two_colors:
        value = COLOR_CODE[name]
        result += str(value)
    return int(result)

print(value(["orange", "orange"])) #, 33)