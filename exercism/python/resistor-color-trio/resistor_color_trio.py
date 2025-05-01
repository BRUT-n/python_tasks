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


def label(colors):
    string_value = f"{COLOR_CODE[colors[0]]}{COLOR_CODE[colors[1]]}{'0' * COLOR_CODE[colors[2]]}"
    value = int(string_value)
    converted_ohms = "ohms"
    if value >= 1000000000:
        converted_ohms = "gigaohms"
        value = value // 1000000000
    if value >= 1000000:
        converted_ohms = "megaohms"
        value = value // 1000000
    if value >= 1000:
        converted_ohms = "kiloohms"
        value = value // 1000
    return f"{value} {converted_ohms}"

print(label(["orange", "orange", "black"])) # 33 ohms
print(label(["blue", "grey", "brown"])) # 680 ohms
print(label(["white", "white", "white"])) # 99 gigaohms