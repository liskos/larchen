def f(x):
    a = 0
    b = 0
    while x > 0:
        b = b + 1
        if x % 2 != 0:
            a = a + 1

        x = x // 2
    return a,b

for i in range(1,10000):
    a,b=f(i)
    if a==3 and b==9:
        print(i)