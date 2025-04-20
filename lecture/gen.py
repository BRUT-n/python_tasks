def f():
    cur = 0
    while True:
        yield cur
        cur += 1

