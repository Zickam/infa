import math
import time

count = 0

"""Bounds are stupidly-defined by yourself"""
for x in range(int(10**9/2.85), 10**10):
    iters_count = math.ceil((354261000 - 987 - x) / 3)
    n = 987 + iters_count * 8

    res = n // 1000
    print(res)
    if res == 231:
        count += 1

    elif res < 231:
        break

print("res:", count)
