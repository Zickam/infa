def ability1(pile_x, pile_y):
    return (pile_x + 1, pile_y)

def ability2(pile_x, pile_y):
    return (pile_x, pile_y + 1)

def ability3(pile_x, pile_y):
    return (pile_x * 3, pile_y)

def ability4(pile_x, pile_y):
    return (pile_x, pile_y * 3)

def useAllAbilities(pile_x, pile_y):
    results = []
    for ability in abilities:
        results.append(ability(pile_x, pile_y))

    return results

abilities = [ability1, ability2, ability3, ability4]

def step19(pile_x, pile_y, n):
    if n == 1 and pile_x + pile_y >= ttl_need:
        return True
    elif n == 1 and pile_x + pile_y < ttl_need:
        return False
    else:
        result = False
        for res in useAllAbilities(pile_x, pile_y):
            result = result or step19(res[0], res[1], n + 1)
        return result

def step20(pile_x, pile_y, n):
    if n == 2 and pile_x + pile_y >= ttl_need:
        return True
    elif n == 2 and pile_x + pile_y < ttl_need:
        return False
    else:
        result = False
        for res in useAllAbilities(pile_x, pile_y):
            result = result or step20(res[0], res[1], n + 1)
        return result

def step21(pile_x, pile_y, n):
    if n == 3 and pile_x + pile_y >= ttl_need:
        return True
    elif n == 3 and pile_x + pile_y < ttl_need:
        return False
    else:
        result = False
        for res in useAllAbilities(pile_x, pile_y):
            result = result or step21(res[0], res[1], n + 1)
        return result


def solve(l_bound, r_bound, pile_x, pile_y):

    answer_19 = 0
    answer_20 = []
    answer_21 = 0
    tree = {} # use if for optimization
    for s in range(l_bound, r_bound + 1):
        pile_y = s
        res19 = step19(pile_x, pile_y, 0)
        res20 = step20(pile_x, pile_y, 0)
        res21 = step21(pile_x, pile_y, 0)

        if res19 and not answer_19:
            answer_19 = s
                                          # 0 is starting n
                                          # P1 V1 P2 V2 etc...
                                          # 1  2  3  4  etc...

        if res20 and len(answer_20) < 2:
            answer_20.append(s)

        if res21 and not answer_21:
            answer_21 = s

    print(f"Answer for 19: {answer_19}")
    print(f"Answer for 20: {answer_20}")
    print(f"Answer for 21: {answer_21}")

if __name__ == "__main__":
    ttl_need = 68
    pile_x, pile_y = 6, -1
    l_bound, r_bound = 1, ttl_need - pile_x - 1
    solve(l_bound, r_bound, pile_x, pile_y)