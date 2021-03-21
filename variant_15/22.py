def f(x):
    s = 5
    while x > 0:
        if x % 8 > 4:
            s = s + (x % 8)
        else:
            s = s * (x % 8)
        x = x // 8
    return s


for i in range(1,100000):
    s = f(i)
    if s%100==0 and s>=100:
        print(i)