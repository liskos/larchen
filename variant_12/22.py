def f(x):
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        b = b * (x%9)
        x = x//9
    return a,b


for i in range(1,10000):
    a, b = f(i)
    if a == 3 and b == 18:
        print(i)
