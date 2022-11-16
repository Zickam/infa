def foo(x, A):
    if (x % A) == 0:
        return 1
    else:
        return 0

for A in range(1, 10**4):
    ok = True
    for x in range(1, 10**4):
        if not (foo(x, A) <= (not (foo(x, 21)) + foo(x, 35))):
            ok = False
            break

    if ok:
        print(A)