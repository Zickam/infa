for x in range(1, 10000):
    for s in range(1, 10000):
        s = 100 * s + x
        n = 1
        while s < 2021:
            s = s + 5 * n
            n = n + 1
        if n == 15:
            print(x)

