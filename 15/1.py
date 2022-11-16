def foo(x, y, A):
    if (x * y < 140) or (y > A) or (x > A):
        return 1
    else:
        return 0

"""Make bounds smaller or run via PyPy/Jit"""
for A in range(10 ** 4):
    ok = True
    for x in range(10 ** 4):
        if not ok:
            break
        for y in range(10 ** 4):
            if not foo(x, y, A):
                ok = False
                break

    if ok:
        print(A)