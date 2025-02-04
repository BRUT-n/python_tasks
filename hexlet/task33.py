def get_number_explanation(number: int): # функция принимает только int
    match number: # введенный int принимается на проверку условий
        case 666:
            return "devil number" # возврат значение если int 666
        case 42:
            return "answer for everything"
        case 7:
            return "prime number"
        case _:
            return "just a number" # возврат если ни одно из условий выше не выполнено

print(get_number_explanation(7))
