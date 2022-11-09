import itertools

letters = "ABCDEX"
# letters *= len(letters)
# letters *= 3
variants = itertools.product(letters, repeat=4)

words = set()

for i in variants:

    # # check if each letter used only once in the word
    # for j in letters:
    #     if not i.count(j) < 2:
    #         ok = False

    index = "".join(i).find("X")
    count = i.count("X")
    if count == 1 and (index == 0 or index == len(i) - 1):
        words.add(i)


print(len(words))


