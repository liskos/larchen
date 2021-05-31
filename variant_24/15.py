def func(a):
    for x in range(0, 1000):
        f = (x & 39 == 0) or (not (x & 11 == 0) or (x & a != 0))
        if not f:
            return False
    return True


for a in range(0, 100000):
    if func(a):
        print(a)
        break
