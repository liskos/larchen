def f(s):
    n = 80
    while s + n < 160:
        s = s + 15
        n = n - 10
    return n

for i in range(1,100000):
    if n<100:
        print(i)