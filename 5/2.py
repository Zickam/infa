# n = int(input())

def execute(n):
    n_bin = bin(n)[2:]
    num_one_count = n_bin.count("1")
    if num_one_count % 2 == 0:
        n_bin += "1"

    else:
        n_bin += "0"

    num_one_count = n_bin.count("1")
    if num_one_count % 2 == 0:
        n_bin += "1"

    else:
        n_bin += "0"


    return n_bin


for i in range(0, 10000):
    r = int(execute(i), 2)
    if r > 54:
        print(r, i)
