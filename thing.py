

def thing(x):
    return (x ** 3) + (3 * x + 2) ** 3 + (2 * x + 1) ** 3

def thing2(x):
    return (36 * x ** 3) + (66 * x ** 2) + (42 * x) + 9

print(thing(166))
print(thing2(166))

def thing3(x):
    return (((10 ** x) + ((10 ** x - 1) * 2 / 3)) ** 3) + (((10 ** x) * 5) ** 3) + (((10 ** (x+1) - 1) / 3) ** 3)

def thing4(x):
    return (((10 ** x) + ((10 ** x - 1) * 2 / 3)) * 10 ** (2 * x + 2)) + (((10 ** x) * 5) * 10 ** (x + 1)) + (((10 ** (x+1) - 1) / 3))


print(thing4(0))
print(thing3(0))