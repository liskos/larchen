def f(d):
    n = 5
    s = 83
    while s <= 1200:
        s = s + d
        n = n + 6
    return n


k = 0
for i in range(1, 100000):
    if f(i)==89:
        k += 1
print(k)