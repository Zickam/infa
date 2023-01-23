a = 125 * 2 ** 0.5

def line1(x, y):
    x_start = 0
    y_start = 0
    x_start_1 = a
    y_start_1 = a
    k = (y_start_1 - y_start) / (x_start_1 - x_start)
    b = y_start - k * x_start

    if y < k * x + b:
        return 1
    else:
        return 0

def line2(x, y):
    x_start = 2 * a
    y_start = 0
    x_start_1 = a
    y_start_1 = a
    k = (y_start_1 - y_start) / (x_start_1 - x_start)
    b = y_start - k * x_start

    if y < k * x + b:
        return 1
    else:
        return 0

def line3(x, y):
    x_start = 0
    y_start = 0
    x_start_1 = a
    y_start_1 = -a
    k = (y_start_1 - y_start) / (x_start_1 - x_start)
    b = y_start - k * x_start

    if y > k * x + b:
        return 1
    else:
        return 0

def line4(x, y):
    x_start = a
    y_start = -a
    x_start_1 = 2 * a
    y_start_1 = 0
    k = (y_start_1 - y_start) / (x_start_1 - x_start)
    b = y_start - k * x_start

    if y > k * x + b:
        return 1
    else:
        return 0

count = 0
for x in range(10 ** 3):
    for y in range(10 ** 3):
        res = line1(x, y) and line2(x, y) and line3(x, y) and line4(x, y)

        if res:
            # print(x, y)
            count += 1

print("res")
print(count)