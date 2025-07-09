INDEX = {
    -1 : "wink",
    -2 : "double blink",
    -3 : "close your eyes",
    -4 : "jump",
    # "fifth" : "reverse"
}

def commands(binary_str):
    result_list = []
    for i in range(-1, -5, -1):
        if binary_str[i] == "1":
            result_list.append(INDEX[i])
    if binary_str[-5] == "1":
        return result_list[::-1]
    return result_list



print(commands("00001")) #, ["wink"])