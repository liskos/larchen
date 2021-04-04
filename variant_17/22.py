def f(x):
    S = 0
    while x > 0:
        if x % 5 > 0:
            S = S + (x % 5)
        else:
            S = S * (x % 5)
        x = x // 5
    return S


for i in range(1,500):
    S = f(i)
    if S==13:
        print(i)