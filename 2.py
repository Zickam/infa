def func(w, x, y, z):
    if ((not y) or x) == ((not x) or w) and (z or x):
        return 1
    else:
        return 0

print(f"w x y z")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if func(w, x, y, z) == 1:
                    print(w, x, y, z, f"| {func(w, x, y, z)}")
