l_bound = 312614
r_bound = 312651

def findDivisors(num):
    divisors = set()

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.add(i)

    return divisors

def solve(l, r):
    for i in range(l, r + 1):
        divisors = findDivisors(i)

        if len(divisors) == 6:
            print(f"All divisors for {i}: {sorted(divisors)}")

if __name__ == "__main__":
    solve(l_bound, r_bound)