from itertools import permutations, combinations

numbers_to_use = [1, 2, 3, 4, 5] * 5
numbers_should_be_used = [1, 1, 1]
length = 5
count = 0

for i in combinations(numbers_to_use, 5):
    number_1 = i.count(1)
    if number_1 >= 3:
        count += 1

print(count)