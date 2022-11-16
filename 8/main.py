import itertools

letters = "КОР"
lenght = 5
variants = itertools.product(letters, repeat=lenght)

words = set()

sorted_variants = sorted(variants)
for i in range(len(sorted_variants)):
    print(i + 1, sorted_variants[i])




print(len(words))


