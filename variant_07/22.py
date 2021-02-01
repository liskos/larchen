def f(x):
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 7)
        x = x // 7
    return a,b


for i in range(1,100000):
    a, b = f(i)
    if a == 4 and b == 30:
        print(i)
        break