def f(x):
    L = x - 16
    M = x + 16
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    return M


for i in range(100,1000):
    M = f(i)
    if M==16:
        print(i)