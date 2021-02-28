def f(x):
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        if x % 14 != 0:
            b = b * (x % 14)
        x = x // 14
    return a,b


n = 0
for i in range(1,10000):
    a, b = f(i)
    if a == 2 and b == 12:
        n+=1
print(n)