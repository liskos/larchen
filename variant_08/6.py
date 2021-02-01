def funk(d):
    s, n = 0, 0
    while s < 111:
        s = s + 8
        n = n + d
    return n


for i in range(1,1000000):
    if funk(i) == 28:
        print(i)