CHAR_DICT = {")" : "(" , "}" : "{" , "]" : "["}

def is_paired(input_string):
    stack = []
    for ch in input_string: # итерация по каждому символу
        if ch in CHAR_DICT.values(): # если символ проходит по значениям открытых скобок
            stack.append(ch) # кладем в стек
        if ch in CHAR_DICT:
            if not stack or stack.pop() != CHAR_DICT[ch]:
                return False
    return not stack

    #     elif stack and ch == char_dict[stack[-1]]: # иначе если стек не пуст и символ является закрывающим по ключу стека из словаря
    #         stack.pop() # убираем из стека
    #     elif ch in char_dict.values(): # иначе если символ является уже закрывающим
    #         return False # то уже не сбалансировано
    # return not stack # проверка пустоты стека