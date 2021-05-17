def func(a):
    for x in range(0, 1000):
        f = (x & 51 == 0) or (x & 42 != 0) or (x & a != 0)
        if not f:
            return False
    return True



for a in range(0, 1000):
    if func(a):
        print(a)
        break