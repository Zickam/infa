# defines maximum base
numeric_alphabet = {10: "A", 11: "B", 12: "C", 13: "D",
                    14: "E", 15: "F", 16: "G", 17: "H", 18: "I"}

numeric_alphabet_r = {}
for key, value in numeric_alphabet.items():
    numeric_alphabet_r[value] = key

def chBaseFromBase_10(num, base_needed):
    new_num = ""
    while num != 0:
        new_part = num % base_needed

        if new_part in numeric_alphabet.keys():
            new_part = numeric_alphabet[new_part]

        else:
            new_part = str(new_part)

        new_num = new_part + new_num
        num //= base_needed

    return new_num


def chBaseToBase_10(num, base_stock):
    new_num = 0
    num = list(num)

    for i in range(len(num)):
        current_pow = len(num) - i - 1
        if num[i] in numeric_alphabet_r.keys():
            curr_num = numeric_alphabet_r[num[i]]

        else:
            curr_num = int(num[i])

        new_num += curr_num * base_stock ** current_pow

    return new_num


num_1_part_1 = "95"
num_1_part_2 = "2"
num_2_part_1 = "458"
for i in range(10):
    num_1 = num_1_part_1 + str(i) + num_1_part_2
    num_2 = str(i) + num_2_part_1
    num_1_base10 = chBaseToBase_10(num_1, 11)
    num_2_base10 = chBaseToBase_10(num_2, 12)

    summa = num_1_base10 + num_2_base10
    if summa % 136 == 0:
        print(i, summa / 136)


