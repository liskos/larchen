def f(x):
    s=0
    while x > 0:
        if x%2>0:
            s = s + (x%7)
        else:
            s = s -(x%7)
        x = x // 7
    return s

for i in range(50,10000):
    s = f(i)
    if s == 1:
        print(i)