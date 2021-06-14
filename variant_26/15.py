def func(a):
    for x in range(0, 200):
        for y in range(0, 200):
            f = (69 != y + 2 * x) or (a < x) or (a < y)
            if not f:
                return False
    return True


for a in range(0, 1000):
    if func(a):
        print(a)
