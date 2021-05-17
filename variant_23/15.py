def func(a):
    for x in range(1, 100):
        f = not (x % a == 0) or ((x % 15 == 0) and (x % 6 == 0))
        if not f:
            return False
    return True



for a in range(1, 10000):
    if func(a):
        print(a)
        break