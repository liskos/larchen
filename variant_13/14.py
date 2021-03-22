def f(x):
    y = 3 * 7**(x+1) + 13 * (7**(x+2)) + 31 * 7**(3*x) + 7 **(2*x)
    s = 0
    while y > 0:
        s = y % 7 + s
        y = y // 7
    return s

for x in range(0, 1000):
    if f(x)==18:
        print(x)
        break