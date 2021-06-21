def f(d):
    n = 33
    s = 4
    while s <= 1725:
        s = s + d
        n = n + 8
    return n


for i in range(1,10000):
    if f(i)==153:
        print(i)