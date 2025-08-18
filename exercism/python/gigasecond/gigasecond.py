from datetime import timedelta

def add(moment): # moment в тестах уже в нужном формате
    gigasec = timedelta(seconds = 1_000_000_000) # timedelta требуется для вычисления интервалов, включает в себя различные аргументы
    return moment + gigasec
