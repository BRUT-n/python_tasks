def normalize_url(adress) -> str:
    cut_adress = adress[0:7] # режем строку на 6 символов для сверки с http://
    if cut_adress == "http://": # сверка с условием, если да
        return(f"https://{adress[7:]}") # то силваем с нужным выводом https:// срезая 6 символов
    elif cut_adress == "https:/": # если выполняется условие с https://
        return(adress) #возвращаем как и было, потому что https:// уже есть 
    else: # если и то и другое False 
        return(f"https://{adress}") # то возвращаем ф-строку сливающую значение адресс с https://


print(normalize_url("github.com"))
 
