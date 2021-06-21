def f(x):
    L = x
    M = 55
    if L %2==0:
        M = 44
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    return M


for i in range(100,1000):
    M = f(i)
    if M==22:
        print(i)