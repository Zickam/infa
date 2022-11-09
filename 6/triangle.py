# Solution for triangle

def lineFunc0(x, y):
    if y < (1 / (3 ** 0.5)) * x:
        return 1
    else:
        return 0

def lineFunc1(x, y):
    if y > (-1 / (3 ** 0.5)) * x:
        return 1
    else:
        return 0

def lineFunc2(x, y):
    if x < 75 ** 0.5:
        return 1
    else:
        return 0

count = 0
for x in range(9):
    for y in range(-5, 5 + 1):
        if lineFunc0(x, y) and lineFunc1(x, y) and lineFunc2(x, y):
            print(x, y)
            count += 1

print(count)