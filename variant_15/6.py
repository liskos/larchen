def f(d):
    n = 10
    s = 101
    while d < s + n:
        s = s -  2 * d
        n = n + d
    return n


for i in range(1, 100000):
    if f(i)==100:
        print(i)