def func(a):
    for x in range(0, 200):
        for y in range(0, 200):
            f = x & 51 == 0 or ((x&41 == 0) != (x & a  !=0))
            if not f:
                return False
    return True


for a in range(0, 1000):
    if func(a):
        print(a)
