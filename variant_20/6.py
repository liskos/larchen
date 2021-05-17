def fun(s):
    n = 200
    while s // n >= 2:
        s = s +5
        n = n + 5
    return s


for s in range(1, 10000):
    if 100 <= fun(s) <= 999:
        print(s)