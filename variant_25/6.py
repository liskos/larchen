def f(d):
    n = 0
    s = 24
    while s <= 1318:
        s = s + d
        n = n + 15

    return n


for i in range(1,10000):
    if f(i)==195:
        print(i)