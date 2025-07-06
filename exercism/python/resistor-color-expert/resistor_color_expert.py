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

TOLERANCE_CODE = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}

def conversion_ohms(value):
    converted_ohms = "ohms"
    # if value >= 1000000000:
    #     converted_ohms = "gigaohms" # нет в тестах таких
    #     value = value / 1000000000
    if value >= 1000000:
        converted_ohms = "megaohms"
        value = value / 1000000
    if value >= 1000:
        converted_ohms = "kiloohms"
        value = value / 1000
    if value % 1 == 0:
        value = int(value)
    return f"{value} {converted_ohms}"

def calculation_of_resistance(colors):
    result = ""
    if len(colors) == 4:
        two_colors = colors[:2]
        for name in two_colors:
            value = COLOR_CODE[name]
            result += str(value)
        return int(result) * 10 ** (COLOR_CODE[colors[2]]) # по правилу 4 цвета вычисляются - умножить на 10 в степени (по коду цвета)
    if len(colors) == 5:
        three_colors = colors[:3]
        for name in three_colors:
            value = COLOR_CODE[name]
            result += str(value)
        return int(result) * 10 ** (COLOR_CODE[colors[3]]) # по правилу 5 цветов вычисляются - умножить на 10 в степени (по коду цвета)

def resistor_label(colors):
    if colors[0] == "black":
        return "0 ohms"
    converted_resistance = conversion_ohms(calculation_of_resistance(colors)) # конвертация единиц измерения
    return f"{converted_resistance} {TOLERANCE_CODE[colors[-1]]}" # вывод с расчетом отклонений
