def sqr(x):
    return x * x


lst = []
for i in range(1, 10):
    lst.append(sqr(i))

# for цель in объект:
#     pass



lst = [sqr(i) for i in range(1, 10)] # list comprehension

print(lst)



s = {sqr(i) for i in range(1, 10)} # set comprehension
print(s)


d = {i: sqr(i) for i in range(1, 10)} # dict comprehension
print(d)

t = (sqr(i) for i in range(1, 10)) # NO TUPLE COMP IN PYTHON!!
print(t)



print(
    list(
        map(lambda x: x * x, range(1, 10))
    )
)



