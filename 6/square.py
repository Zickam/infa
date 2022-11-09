# Solution for square

def lineFunc0(x, y):
    if y < 12:
        return 1
    else:
        return 0

def lineFunc1(x, y):
    if y > 0:
        return 1
    else:
        return 0

def lineFunc2(x, y):
    if x < 12:
        return 1
    else:
        return 0

def lineFunc3(x, y):
    if x > 0:
        return 1
    else:
        return 0

count = 0
for x in range(12):
    for y in range(0, 12 + 1):
        if lineFunc0(x, y) and lineFunc1(x, y) and lineFunc2(x, y) and lineFunc3(x, y):
            print(x, y)
            count += 1

print(count)