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

def color_code(color):
    return COLOR_CODE[color]
    # color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    # return color_list.index(color)


def colors():
    return [key for key in COLOR_CODE.keys()]
    # return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
