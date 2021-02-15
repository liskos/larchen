def fun(a):
    for x in range(1, 300):
        for y in range(1, 300):
            f = (2 * x + y != 100) or (x < y) or (a < x)
            if not f:
                return False
    return True


for a in range(1, 10000):
    if fun(a):
        print(a)