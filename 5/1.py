max = 255
for i in range(max + 1):
    i_bin = bin(i)[2:]
    while len(i_bin) != 8:
        i_bin = "0" + i_bin

    i_bin_inverted = ""
    for letter in i_bin:
        if letter == "0":
            i_bin_inverted += "1"
        elif letter == "1":
            i_bin_inverted += "0"

    decimal_i_final = int(i_bin_inverted, 2)
    result = decimal_i_final - i
    if result == 111:
        print(i)