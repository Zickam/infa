# Solution for rectangle

def lineFunc0(x, y):
    if y < 10:
        return 1
    else:
        return 0

def lineFunc1(x, y):
    if y > 0:
        return 1
    else:
        return 0

def lineFunc2(x, y):
    if x < 10:
        return 1
    else:
        return 0

def lineFunc3(x, y):
    if x > 0:
        return 1
    else:
        return 0

count = 0
for x in range(-(10**2), 10**2):
    for y in range(-(10**2), 10**2):
        if lineFunc0(x, y) and lineFunc1(x, y) and lineFunc2(x, y) and lineFunc3(x, y):
            print(x, y)
            count += 1

print(count)