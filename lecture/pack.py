def add(a, b):
    return a + b


t = {"x": 1, "y": 2}

c1 = add(**t)

c2 = add(a=1, b=2)

print(c1, c2)