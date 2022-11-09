def execute(n):
    a, b, c = map(int, list(str(n)))
    tmp_1 = a * b
    tmp_2 = b * c
    sorted_tmp = sorted([tmp_1, tmp_2])
    new_n = int(f"{sorted_tmp[0]}{sorted_tmp[1]}")
    return new_n

for i in range(100, 1000):
    if execute(i) == 621:
        print(i)